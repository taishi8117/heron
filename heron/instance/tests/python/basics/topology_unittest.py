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

# pylint: disable=missing-docstring
# pylint: disable=protected-access
import unittest

from heron.common.src.python.utils.misc import default_serializer
from heron.instance.src.python.basics import Topology, HeronComponentSpec, Stream, Grouping
from heron.instance.src.python.basics.topology import TopologyType
from heron.proto import topology_pb2

class TestSane(Topology):
  config = {"topology.wide.config.1": "value",
            "spout.overriden.config": True}
  spout = HeronComponentSpec(None, "sp_class", True, 3, inputs=None,
                             outputs=["word", "count",
                                      Stream(fields=['error_msg'], name='error_stream')],
                             config={"spout.specific.config.1": "value",
                                     "spout.specific.config.2": True,
                                     "spout.specific.config.3": -12.4,
                                     "spout.specific.config.4": [1, 2, 3],
                                     "spout.overriden.config": False})
  bolt = HeronComponentSpec(None, "bl_class", False, 4,
                            inputs={spout: Grouping.SHUFFLE, spout['error_stream']: Grouping.ALL})

class TopologyTest(unittest.TestCase):
  def test_sane_topology(self):
    self.assertEqual(TestSane.topology_name, "TestSaneTopology")

    # topology-wide config
    expecting_topo_config = TopologyType.DEFAULT_TOPOLOGY_CONFIG
    expecting_topo_config.update({"topology.wide.config.1": "value",
                                  "spout.overriden.config": "true"})
    self.assertEqual(TestSane._topo_config, expecting_topo_config)

    self.assertEqual(len(TestSane._protobuf_bolts), 1)
    self.assertEqual(len(TestSane._protobuf_spouts), 1)

    self.assertEqual(len(TestSane._heron_specs), 2)
    for spec in TestSane._heron_specs:
      if spec.is_spout:
        self.assertEqual(spec.name, "spout")
        self.assertEqual(spec.python_class_path, "sp_class")
        self.assertEqual(spec.parallelism, 3)
      else:
        self.assertEqual(spec.name, "bolt")
        self.assertEqual(spec.python_class_path, "bl_class")
        self.assertEqual(spec.parallelism, 4)

    self.assertTrue(isinstance(TestSane.protobuf_topology, topology_pb2.Topology))

    proto_topo = TestSane.protobuf_topology

    ### spout protobuf ###
    self.assertEqual(len(proto_topo.spouts), 1)
    spout = proto_topo.spouts[0]
    self.assertEqual(spout.comp.name, "spout")
    self.assertEqual(spout.comp.spec, topology_pb2.ComponentObjectSpec.Value("PYTHON_CLASS_NAME"))
    self.assertEqual(spout.comp.class_name, "sp_class")
    expecting_spout_config = {"topology.component.parallelism": "3",
                              "spout.specific.config.1": "value",
                              "spout.specific.config.2": "true",
                              "spout.specific.config.3": "-12.4",
                              "spout.specific.config.4": default_serializer.serialize([1, 2, 3]),
                              "spout.overriden.config": "false"}
    self.assertEqual(len(spout.comp.config.kvs), len(expecting_spout_config))
    for conf in spout.comp.config.kvs:
      value = expecting_spout_config[conf.key]
      if conf.type == topology_pb2.ConfigValueType.Value("STRING_VALUE"):
        self.assertEqual(value, conf.value)
      elif conf.type == topology_pb2.ConfigValueType.Value("PYTHON_SERIALIZED_VALUE"):
        self.assertEqual(value, conf.serialized_value)
      else:
        self.fail()

    # output stream
    self.assertEqual(len(spout.outputs), 2)
    for out_stream in spout.outputs:
      if out_stream.stream.id == "default":
        self.assertEqual(out_stream.stream.component_name, "spout")
        self.assertEqual(len(out_stream.schema.keys), 2)
      else:
        self.assertEqual(out_stream.stream.id, "error_stream")
        self.assertEqual(out_stream.stream.component_name, "spout")
        self.assertEqual(len(out_stream.schema.keys), 1)


    ### bolt protobuf ###
    self.assertEqual(len(proto_topo.bolts), 1)
    bolt = proto_topo.bolts[0]
    self.assertEqual(bolt.comp.name, "bolt")
    self.assertEqual(bolt.comp.spec, topology_pb2.ComponentObjectSpec.Value("PYTHON_CLASS_NAME"))
    self.assertEqual(bolt.comp.class_name, "bl_class")
    expecting_bolt_config = {"topology.component.parallelism": "4"}
    self.assertEqual(len(bolt.comp.config.kvs), len(expecting_bolt_config))
    conf = bolt.comp.config.kvs[0]
    self.assertEqual(conf.type, topology_pb2.ConfigValueType.Value("STRING_VALUE"))
    self.assertEqual(conf.value, expecting_bolt_config[conf.key])

    # out stream
    self.assertEqual(len(bolt.outputs), 0)

    # in stream
    self.assertEqual(len(bolt.inputs), 2)
    for in_stream in bolt.inputs:
      if in_stream.stream.id == "default":
        self.assertEqual(in_stream.stream.component_name, "spout")
        self.assertEqual(in_stream.gtype, topology_pb2.Grouping.Value("SHUFFLE"))
      else:
        self.assertEqual(in_stream.stream.id, "error_stream")
        self.assertEqual(in_stream.stream.component_name, "spout")
        self.assertEqual(in_stream.gtype, topology_pb2.Grouping.Value("ALL"))

    # state change
    self.assertEqual(proto_topo.state, topology_pb2.TopologyState.Value("RUNNING"))
    TestSane.deploy_deactivated()
    self.assertEqual(proto_topo.state, topology_pb2.TopologyState.Value("PAUSED"))
