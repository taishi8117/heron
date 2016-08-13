# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stmgr.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import stats_pb2
import topology_pb2
import physical_plan_pb2
import tuple_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stmgr.proto',
  package='heron.proto.stmgr',
  serialized_pb='\n\x0bstmgr.proto\x12\x11heron.proto.stmgr\x1a\x0c\x63ommon.proto\x1a\x0bstats.proto\x1a\x0etopology.proto\x1a\x13physical_plan.proto\x1a\x0btuple.proto\"M\n\x16NewPhysicalPlanMessage\x12\x33\n\tnew_pplan\x18\x01 \x02(\x0b\x32 .heron.proto.system.PhysicalPlan\"u\n\x17RegisterInstanceRequest\x12.\n\x08instance\x18\x01 \x02(\x0b\x32\x1c.heron.proto.system.Instance\x12\x15\n\rtopology_name\x18\x02 \x02(\t\x12\x13\n\x0btopology_id\x18\x03 \x02(\t\"w\n\x18RegisterInstanceResponse\x12*\n\x06status\x18\x01 \x02(\x0b\x32\x1a.heron.proto.system.Status\x12/\n\x05pplan\x18\x02 \x01(\x0b\x32 .heron.proto.system.PhysicalPlan\"O\n\x1cNewInstanceAssignmentMessage\x12/\n\x05pplan\x18\x01 \x02(\x0b\x32 .heron.proto.system.PhysicalPlan\">\n\x0cTupleMessage\x12.\n\x03set\x18\x01 \x02(\x0b\x32!.heron.proto.system.HeronTupleSet\"O\n\x12StrMgrHelloRequest\x12\x15\n\rtopology_name\x18\x01 \x02(\t\x12\x13\n\x0btopology_id\x18\x02 \x02(\t\x12\r\n\x05stmgr\x18\x03 \x02(\t\"A\n\x13StrMgrHelloResponse\x12*\n\x06status\x18\x01 \x02(\x0b\x32\x1a.heron.proto.system.Status\"U\n\x12TupleStreamMessage\x12\x0f\n\x07task_id\x18\x01 \x02(\x05\x12.\n\x03set\x18\x02 \x02(\x0b\x32!.heron.proto.system.HeronTupleSet\"i\n\x18StartBackPressureMessage\x12\x15\n\rtopology_name\x18\x01 \x02(\t\x12\x13\n\x0btopology_id\x18\x02 \x02(\t\x12\r\n\x05stmgr\x18\x03 \x02(\t\x12\x12\n\nmessage_id\x18\x04 \x02(\t\"h\n\x17StopBackPressureMessage\x12\x15\n\rtopology_name\x18\x01 \x02(\t\x12\x13\n\x0btopology_id\x18\x02 \x02(\t\x12\r\n\x05stmgr\x18\x03 \x02(\t\x12\x12\n\nmessage_id\x18\x04 \x02(\tB.\n\x1d\x63om.twitter.heron.proto.stmgrB\rStreamManager')




_NEWPHYSICALPLANMESSAGE = _descriptor.Descriptor(
  name='NewPhysicalPlanMessage',
  full_name='heron.proto.stmgr.NewPhysicalPlanMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_pplan', full_name='heron.proto.stmgr.NewPhysicalPlanMessage.new_pplan', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=111,
  serialized_end=188,
)


_REGISTERINSTANCEREQUEST = _descriptor.Descriptor(
  name='RegisterInstanceRequest',
  full_name='heron.proto.stmgr.RegisterInstanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance', full_name='heron.proto.stmgr.RegisterInstanceRequest.instance', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topology_name', full_name='heron.proto.stmgr.RegisterInstanceRequest.topology_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topology_id', full_name='heron.proto.stmgr.RegisterInstanceRequest.topology_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=190,
  serialized_end=307,
)


_REGISTERINSTANCERESPONSE = _descriptor.Descriptor(
  name='RegisterInstanceResponse',
  full_name='heron.proto.stmgr.RegisterInstanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='heron.proto.stmgr.RegisterInstanceResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pplan', full_name='heron.proto.stmgr.RegisterInstanceResponse.pplan', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=309,
  serialized_end=428,
)


_NEWINSTANCEASSIGNMENTMESSAGE = _descriptor.Descriptor(
  name='NewInstanceAssignmentMessage',
  full_name='heron.proto.stmgr.NewInstanceAssignmentMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pplan', full_name='heron.proto.stmgr.NewInstanceAssignmentMessage.pplan', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=430,
  serialized_end=509,
)


_TUPLEMESSAGE = _descriptor.Descriptor(
  name='TupleMessage',
  full_name='heron.proto.stmgr.TupleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='set', full_name='heron.proto.stmgr.TupleMessage.set', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=511,
  serialized_end=573,
)


_STRMGRHELLOREQUEST = _descriptor.Descriptor(
  name='StrMgrHelloRequest',
  full_name='heron.proto.stmgr.StrMgrHelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topology_name', full_name='heron.proto.stmgr.StrMgrHelloRequest.topology_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topology_id', full_name='heron.proto.stmgr.StrMgrHelloRequest.topology_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stmgr', full_name='heron.proto.stmgr.StrMgrHelloRequest.stmgr', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=575,
  serialized_end=654,
)


_STRMGRHELLORESPONSE = _descriptor.Descriptor(
  name='StrMgrHelloResponse',
  full_name='heron.proto.stmgr.StrMgrHelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='heron.proto.stmgr.StrMgrHelloResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=656,
  serialized_end=721,
)


_TUPLESTREAMMESSAGE = _descriptor.Descriptor(
  name='TupleStreamMessage',
  full_name='heron.proto.stmgr.TupleStreamMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='heron.proto.stmgr.TupleStreamMessage.task_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set', full_name='heron.proto.stmgr.TupleStreamMessage.set', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=723,
  serialized_end=808,
)


_STARTBACKPRESSUREMESSAGE = _descriptor.Descriptor(
  name='StartBackPressureMessage',
  full_name='heron.proto.stmgr.StartBackPressureMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topology_name', full_name='heron.proto.stmgr.StartBackPressureMessage.topology_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topology_id', full_name='heron.proto.stmgr.StartBackPressureMessage.topology_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stmgr', full_name='heron.proto.stmgr.StartBackPressureMessage.stmgr', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='heron.proto.stmgr.StartBackPressureMessage.message_id', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=810,
  serialized_end=915,
)


_STOPBACKPRESSUREMESSAGE = _descriptor.Descriptor(
  name='StopBackPressureMessage',
  full_name='heron.proto.stmgr.StopBackPressureMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topology_name', full_name='heron.proto.stmgr.StopBackPressureMessage.topology_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topology_id', full_name='heron.proto.stmgr.StopBackPressureMessage.topology_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stmgr', full_name='heron.proto.stmgr.StopBackPressureMessage.stmgr', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='heron.proto.stmgr.StopBackPressureMessage.message_id', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=917,
  serialized_end=1021,
)

_NEWPHYSICALPLANMESSAGE.fields_by_name['new_pplan'].message_type = physical_plan_pb2._PHYSICALPLAN
_REGISTERINSTANCEREQUEST.fields_by_name['instance'].message_type = physical_plan_pb2._INSTANCE
_REGISTERINSTANCERESPONSE.fields_by_name['status'].message_type = common_pb2._STATUS
_REGISTERINSTANCERESPONSE.fields_by_name['pplan'].message_type = physical_plan_pb2._PHYSICALPLAN
_NEWINSTANCEASSIGNMENTMESSAGE.fields_by_name['pplan'].message_type = physical_plan_pb2._PHYSICALPLAN
_TUPLEMESSAGE.fields_by_name['set'].message_type = tuple_pb2._HERONTUPLESET
_STRMGRHELLORESPONSE.fields_by_name['status'].message_type = common_pb2._STATUS
_TUPLESTREAMMESSAGE.fields_by_name['set'].message_type = tuple_pb2._HERONTUPLESET
DESCRIPTOR.message_types_by_name['NewPhysicalPlanMessage'] = _NEWPHYSICALPLANMESSAGE
DESCRIPTOR.message_types_by_name['RegisterInstanceRequest'] = _REGISTERINSTANCEREQUEST
DESCRIPTOR.message_types_by_name['RegisterInstanceResponse'] = _REGISTERINSTANCERESPONSE
DESCRIPTOR.message_types_by_name['NewInstanceAssignmentMessage'] = _NEWINSTANCEASSIGNMENTMESSAGE
DESCRIPTOR.message_types_by_name['TupleMessage'] = _TUPLEMESSAGE
DESCRIPTOR.message_types_by_name['StrMgrHelloRequest'] = _STRMGRHELLOREQUEST
DESCRIPTOR.message_types_by_name['StrMgrHelloResponse'] = _STRMGRHELLORESPONSE
DESCRIPTOR.message_types_by_name['TupleStreamMessage'] = _TUPLESTREAMMESSAGE
DESCRIPTOR.message_types_by_name['StartBackPressureMessage'] = _STARTBACKPRESSUREMESSAGE
DESCRIPTOR.message_types_by_name['StopBackPressureMessage'] = _STOPBACKPRESSUREMESSAGE

class NewPhysicalPlanMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWPHYSICALPLANMESSAGE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.NewPhysicalPlanMessage)

class RegisterInstanceRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERINSTANCEREQUEST

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.RegisterInstanceRequest)

class RegisterInstanceResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERINSTANCERESPONSE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.RegisterInstanceResponse)

class NewInstanceAssignmentMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NEWINSTANCEASSIGNMENTMESSAGE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.NewInstanceAssignmentMessage)

class TupleMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TUPLEMESSAGE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.TupleMessage)

class StrMgrHelloRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STRMGRHELLOREQUEST

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.StrMgrHelloRequest)

class StrMgrHelloResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STRMGRHELLORESPONSE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.StrMgrHelloResponse)

class TupleStreamMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TUPLESTREAMMESSAGE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.TupleStreamMessage)

class StartBackPressureMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STARTBACKPRESSUREMESSAGE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.StartBackPressureMessage)

class StopBackPressureMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOPBACKPRESSUREMESSAGE

  # @@protoc_insertion_point(class_scope:heron.proto.stmgr.StopBackPressureMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\035com.twitter.heron.proto.stmgrB\rStreamManager')
# @@protoc_insertion_point(module_scope)
