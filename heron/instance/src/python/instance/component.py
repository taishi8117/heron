# Copyright 2016 Twitter. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

from heron.common.src.python.utils.misc import PythonSerializer, OutgoingTupleHelper
from heron.instance.src.python.instance.stream import Stream, Grouping, GlobalStreamId
from heron.proto import tuple_pb2, topology_pb2

import heron.common.src.python.constants as constants

class Component(object):
  """The base class for heron bolt/spout instance

  Implements the following functionality:
  1. Basic output collector API and pushing tuples to Out-Stream
  2. Run tasks continually

  :ivar pplan_helper: Physical Plan Helper for this component
  :ivar in_stream:    In-Stream Heron Communicator
  :ivar output_helper: Outgoing Tuple Helper
  :ivar serializer: Implementation of Heron Serializer
  """

  DEFAULT_STREAM_ID = "default"
  make_data_tuple = lambda _ : tuple_pb2.HeronDataTuple()

  def __init__(self, pplan_helper, in_stream, out_stream, looper,
               sys_config, serializer=PythonSerializer()):
    self.pplan_helper = pplan_helper
    self.in_stream = in_stream
    self.serializer = serializer
    self.output_helper = OutgoingTupleHelper(self.pplan_helper, out_stream)
    self.looper = looper
    self.sys_config = sys_config

    # will set a root logger here
    self.logger = logging.getLogger()


  @classmethod
  def get_python_class_path(cls):
    return cls.__module__ + "." + cls.__name__

  def log(self, message, level=None):
    """Log message, optionally providing a logging level

    It is compatible with StreamParse API.

    :type message: str
    :param message: the log message to send
    :type level: str
    :param level: the logging level,
                  one of: trace (=debug), debug, info, warn or error (default: info)
    """
    if level is None:
      _log_level = logging.INFO
    else:
      if level == "trace" or level == "debug":
        _log_level = logging.DEBUG
      elif level == "info":
        _log_level = logging.INFO
      elif level == "warn":
        _log_level = logging.WARNING
      elif level == "error":
        _log_level = logging.ERROR
      else:
        raise ValueError(level + " is not supported as logging level")

    self.logger.log(_log_level, message)

  def admit_data_tuple(self, stream_id, data_tuple, tuple_size_in_bytes):
    self.output_helper.add_data_tuple(stream_id, data_tuple, tuple_size_in_bytes)

  def admit_control_tuple(self, control_tuple, tuple_size_in_bytes, is_ack):
    self.output_helper.add_control_tuple(control_tuple, tuple_size_in_bytes, is_ack)

  def get_total_data_emitted_in_bytes(self):
    return self.output_helper.total_data_emitted_in_bytes

  ##################################################################
  # The followings are to be implemented by Spout/Bolt independently
  ##################################################################

  def start(self):
    """Do the basic setup for Heron Instance"""
    raise NotImplementedError()

  def stop(self):
    """Do the basic clean for Heron Instance

    Note that this method is not guaranteed to be invoked
    """
    # TODO: We never actually call this method
    raise NotImplementedError()

  def process_incoming_tuples(self):
    """Should be called when a tuple was buffered into in_stream"""
    raise NotImplementedError()

  def _read_tuples_and_execute(self):
    """Read tuples from a queue and process the tuples"""
    raise NotImplementedError()

  def _activate(self):
    """Activate the instance"""
    raise NotImplementedError()

  def _deactivate(self):
    """Deactivate the instance"""
    raise NotImplementedError()

class HeronComponentSpec(object):
  def __init__(self, name, python_class_path, is_spout, par,
               inputs=None, outputs=None, config=None):
    self.name = name
    self.python_class_path = python_class_path
    self.is_spout = is_spout
    self.parallelism = par
    self.inputs = inputs
    self.outputs = outputs
    self.custom_config = config

    # serializer used for serializing configuration
    self.config_serializer = PythonSerializer()

  def get_protobuf(self):
    """Returns protobuf message (Spout or Bolt) of this component"""
    if self.is_spout:
      return self._get_spout()
    else:
      return self._get_bolt()

  def _get_spout(self):
    """Returns Spout protobuf message"""
    spout = topology_pb2.Spout()
    spout.comp.CopyFrom(self._get_base_component())

    # Add output streams
    self._add_out_streams(spout)
    return spout

  def _get_bolt(self):
    """Returns Bolt protobuf message"""
    bolt = topology_pb2.Bolt()
    bolt.comp.CopyFrom(self._get_base_component())

    # Add streams
    self._add_in_streams(bolt)
    self._add_out_streams(bolt)
    return bolt

  def _get_base_component(self):
    """Returns Component protobuf message"""
    comp = topology_pb2.Component()
    comp.name = self.name
    comp.spec = topology_pb2.ComponentObjectSpec.Value("PYTHON_CLASS_NAME")
    comp.class_name = self.python_class_path
    comp.config.CopyFrom(self._get_comp_config())
    return comp

  def _get_comp_config(self):
    """Returns component-specific Config protobuf message

    It first adds ``topology.component.parallelism``, and is overriden by
    a user-defined component-specific configuration, specified by spec().
    """
    proto_config = topology_pb2.Config()

    # first add parallelism
    key = proto_config.kvs.add()
    key.key = constants.TOPOLOGY_COMPONENT_PARALLELISM
    key.value = str(self.parallelism)
    key.type = topology_pb2.ConfigValueType.Value("STRING_VALUE")

    # iterate through self.custom_config
    if self.custom_config is not None:
      sanitized = self._sanitize_config(self.custom_config)
      for key, value in sanitized.iteritems():
        if isinstance(value, str):
          kvs = proto_config.kvs.add()
          kvs.key = key
          kvs.value = value
          kvs.type = topology_pb2.ConfigValueType.Value("STRING_VALUE")
        else:
          # need to serialize
          kvs = proto_config.kvs.add()
          kvs.key = key
          kvs.serialized_value = self.config_serializer.serialize(value)
          kvs.type = topology_pb2.ConfigValueType.Value("PYTHON_SERIALIZED_VALUE")

    return proto_config

  @staticmethod
  def _sanitize_config(custom_config):
    """Checks whether a given custom_config and returns a sanitized dict <str -> (str|object)>

    It checks if keys are all strings and sanitizes values of a given dictionary as follows:

    - If string, number or boolean is given as a value, it is converted to string.
      For string and number (int, float), it is converted to string by a built-in ``str()`` method.
      For a boolean value, ``True`` is converted to "true" instead of "True", and ``False`` is
      converted to "false" instead of "False", in order to keep the consistency with
      Java configuration.

    - If neither of the above is given as a value, it is inserted into the sanitized dict as it is.
      These values will need to be serialized before adding to a protobuf message.
    """
    if not isinstance(custom_config, dict):
      raise TypeError("Component-specific configuration must be given as a dict type, given: "
                      + str(type(custom_config)))
    sanitized = {}
    for key, value in custom_config.iteritems():
      if not isinstance(key, str):
        raise TypeError("Key for component-specific configuration must be string, given: " +
                        str(type(key)) + ":" + str(key))

      if isinstance(value, bool):
        sanitized[key] = "true" if value else "false"
      elif isinstance(value, (str, int, float)):
        sanitized[key] = str(value)
      else:
        sanitized[key] = value

    return sanitized

  def _add_in_streams(self, bolt):
    """Adds inputs to a given protobuf Bolt message"""
    if self.inputs is None:
      return
    # sanitize inputs and get a map <GlobalStreamId -> Grouping>
    input_dict = self._sanitize_inputs()

    for global_streamid, gtype in input_dict.iteritems():
      in_stream = bolt.inputs.add()
      in_stream.stream.CopyFrom(self._get_stream_id(global_streamid.component_id,
                                                    global_streamid.stream_id))
      if isinstance(gtype, Grouping.FIELDS):
        # it's a field grouping
        in_stream.gtype = gtype.gtype
        in_stream.grouping_fields.CopyFrom(self._get_stream_schema(gtype.fields))
      else:
        in_stream.gtype = gtype

  def _sanitize_inputs(self):
    """Sanitizes input fields and returns a map <GlobalStreamId -> Grouping>"""
    ret = {}
    if self.inputs is None:
      return

    if isinstance(self.inputs, dict):
      # inputs are dictionary, must be either <HeronComponentSpec -> Grouping> or
      # <GlobalStreamId -> Grouping>
      for key, grouping in self.inputs.iteritems():
        if not Grouping.is_grouping_sane(grouping):
          raise ValueError('A given grouping is not supported')
        if isinstance(key, HeronComponentSpec):
          # use default streamid
          global_streamid = GlobalStreamId(key.name, Stream.DEFAULT_STREAM_ID)
          ret[global_streamid] = grouping
        elif isinstance(key, GlobalStreamId):
          ret[key] = grouping
        else:
          raise ValueError(str(key) + " is not supported as a key to inputs")
    elif isinstance(self.inputs, (list, tuple)):
      # inputs are lists, must be either a list of HeronComponentSpec or GlobalStreamId
      # will use SHUFFLE grouping
      for input_obj in self.inputs:
        if isinstance(input_obj, HeronComponentSpec):
          global_streamid = GlobalStreamId(input_obj.name, Stream.DEFAULT_STREAM_ID)
          ret[global_streamid] = Grouping.SHUFFLE
        elif isinstance(input_obj, GlobalStreamId):
          ret[input_obj] = Grouping.SHUFFLE
        else:
          raise ValueError(str(input_obj) + " is not supported as an input")
    else:
      raise TypeError("Inputs must be a list, dict, or None, given: " + str(self.inputs))

    return ret

  def _add_out_streams(self, spbl):
    """Adds outputs to a given protobuf Bolt or Spout message"""
    if self.outputs is None:
      return

    # sanitize outputs and get a map <stream_id -> out fields>
    output_map = self._sanitize_outputs()

    for stream_id, out_fields in output_map.iteritems():
      out_stream = spbl.outputs.add()
      out_stream.stream.CopyFrom(self._get_stream_id(self.name, stream_id))
      out_stream.schema.CopyFrom(self._get_stream_schema(out_fields))

  def _sanitize_outputs(self):
    """Sanitizes output fields and returns a map <stream_id -> list of output fields>"""
    ret = {}
    if self.outputs is None:
      return

    for output in self.outputs:
      if not isinstance(output, (str, Stream)):
        raise TypeError("Outputs must be a list of strings or Streams, given: " + str(output))

      if isinstance(output, str):
        # it's a default stream
        if Stream.DEFAULT_STREAM_ID not in ret:
          ret[Stream.DEFAULT_STREAM_ID] = list()
        ret[Stream.DEFAULT_STREAM_ID].append(output)
      else:
        # output is a Stream object
        ret[output.stream_id] = output.fields
    return ret

  @staticmethod
  def _get_stream_id(comp_name, id):
    """Returns a StreamId protobuf message"""
    stream_id = topology_pb2.StreamId()
    stream_id.id = id
    stream_id.component_name = comp_name
    return stream_id

  @staticmethod
  def _get_stream_schema(fields):
    """Returns a StreamSchema protobuf message"""
    stream_schema = topology_pb2.StreamSchema()
    for field in fields:
      key = stream_schema.keys.add()
      key.key = field
      key.type = topology_pb2.Type.Value("OBJECT")

    return stream_schema

