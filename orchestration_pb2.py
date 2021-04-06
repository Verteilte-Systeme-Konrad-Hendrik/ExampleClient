# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orchestration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='orchestration.proto',
  package='Orchestration',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13orchestration.proto\x12\rOrchestration\"\x1a\n\nClientInfo\x12\x0c\n\x04port\x18\x01 \x01(\r\"\x1c\n\x0bRoundNumber\x12\r\n\x05round\x18\x01 \x01(\x04\"\x86\x01\n\x10QueueMessageBulk\x12*\n\x0bsendingNode\x18\x01 \x01(\x0b\x32\x15.Orchestration.NodeId\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x04\x12-\n\x08messages\x18\x03 \x03(\x0b\x32\x1b.Orchestration.QueueMessage\"g\n\x0cQueueMessage\x12%\n\x06sender\x18\x01 \x01(\x0b\x32\x15.Orchestration.NodeId\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x04\x12\x17\n\x0fmessage_content\x18\x03 \x01(\x0c\"\x07\n\x05\x45mpty\"*\n\x0f\x41\x62stractMessage\x12\x17\n\x0fmessage_content\x18\x01 \x01(\x0c\"\x18\n\x06NodeId\x12\x0e\n\x06nodeId\x18\x01 \x01(\t2\x8c\x03\n\x13\x43lientCommunication\x12L\n\x0eproduceMessage\x12\x1e.Orchestration.AbstractMessage\x1a\x1a.Orchestration.RoundNumber\x12L\n\x0epublishMessage\x12\x1e.Orchestration.AbstractMessage\x1a\x1a.Orchestration.RoundNumber\x12@\n\x0ctriggerRound\x12\x1a.Orchestration.RoundNumber\x1a\x14.Orchestration.Empty\x12R\n\x13pullMessageForRound\x12\x1a.Orchestration.RoundNumber\x1a\x1f.Orchestration.QueueMessageBulk\x12\x43\n\x10registerListener\x12\x14.Orchestration.Empty\x1a\x19.Orchestration.ClientInfo2]\n\x12ServerFacingClient\x12G\n\x13NotifyRoundFinished\x12\x1a.Orchestration.RoundNumber\x1a\x14.Orchestration.Emptyb\x06proto3'
)




_CLIENTINFO = _descriptor.Descriptor(
  name='ClientInfo',
  full_name='Orchestration.ClientInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='Orchestration.ClientInfo.port', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=64,
)


_ROUNDNUMBER = _descriptor.Descriptor(
  name='RoundNumber',
  full_name='Orchestration.RoundNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='round', full_name='Orchestration.RoundNumber.round', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=94,
)


_QUEUEMESSAGEBULK = _descriptor.Descriptor(
  name='QueueMessageBulk',
  full_name='Orchestration.QueueMessageBulk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sendingNode', full_name='Orchestration.QueueMessageBulk.sendingNode', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='Orchestration.QueueMessageBulk.sequence_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messages', full_name='Orchestration.QueueMessageBulk.messages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=231,
)


_QUEUEMESSAGE = _descriptor.Descriptor(
  name='QueueMessage',
  full_name='Orchestration.QueueMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='Orchestration.QueueMessage.sender', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='Orchestration.QueueMessage.sequence_number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_content', full_name='Orchestration.QueueMessage.message_content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=336,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Orchestration.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=345,
)


_ABSTRACTMESSAGE = _descriptor.Descriptor(
  name='AbstractMessage',
  full_name='Orchestration.AbstractMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_content', full_name='Orchestration.AbstractMessage.message_content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=389,
)


_NODEID = _descriptor.Descriptor(
  name='NodeId',
  full_name='Orchestration.NodeId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='Orchestration.NodeId.nodeId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=415,
)

_QUEUEMESSAGEBULK.fields_by_name['sendingNode'].message_type = _NODEID
_QUEUEMESSAGEBULK.fields_by_name['messages'].message_type = _QUEUEMESSAGE
_QUEUEMESSAGE.fields_by_name['sender'].message_type = _NODEID
DESCRIPTOR.message_types_by_name['ClientInfo'] = _CLIENTINFO
DESCRIPTOR.message_types_by_name['RoundNumber'] = _ROUNDNUMBER
DESCRIPTOR.message_types_by_name['QueueMessageBulk'] = _QUEUEMESSAGEBULK
DESCRIPTOR.message_types_by_name['QueueMessage'] = _QUEUEMESSAGE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['AbstractMessage'] = _ABSTRACTMESSAGE
DESCRIPTOR.message_types_by_name['NodeId'] = _NODEID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientInfo = _reflection.GeneratedProtocolMessageType('ClientInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTINFO,
  '__module__' : 'orchestration_pb2'
  # @@protoc_insertion_point(class_scope:Orchestration.ClientInfo)
  })
_sym_db.RegisterMessage(ClientInfo)

RoundNumber = _reflection.GeneratedProtocolMessageType('RoundNumber', (_message.Message,), {
  'DESCRIPTOR' : _ROUNDNUMBER,
  '__module__' : 'orchestration_pb2'
  # @@protoc_insertion_point(class_scope:Orchestration.RoundNumber)
  })
_sym_db.RegisterMessage(RoundNumber)

QueueMessageBulk = _reflection.GeneratedProtocolMessageType('QueueMessageBulk', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEMESSAGEBULK,
  '__module__' : 'orchestration_pb2'
  # @@protoc_insertion_point(class_scope:Orchestration.QueueMessageBulk)
  })
_sym_db.RegisterMessage(QueueMessageBulk)

QueueMessage = _reflection.GeneratedProtocolMessageType('QueueMessage', (_message.Message,), {
  'DESCRIPTOR' : _QUEUEMESSAGE,
  '__module__' : 'orchestration_pb2'
  # @@protoc_insertion_point(class_scope:Orchestration.QueueMessage)
  })
_sym_db.RegisterMessage(QueueMessage)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'orchestration_pb2'
  # @@protoc_insertion_point(class_scope:Orchestration.Empty)
  })
_sym_db.RegisterMessage(Empty)

AbstractMessage = _reflection.GeneratedProtocolMessageType('AbstractMessage', (_message.Message,), {
  'DESCRIPTOR' : _ABSTRACTMESSAGE,
  '__module__' : 'orchestration_pb2'
  # @@protoc_insertion_point(class_scope:Orchestration.AbstractMessage)
  })
_sym_db.RegisterMessage(AbstractMessage)

NodeId = _reflection.GeneratedProtocolMessageType('NodeId', (_message.Message,), {
  'DESCRIPTOR' : _NODEID,
  '__module__' : 'orchestration_pb2'
  # @@protoc_insertion_point(class_scope:Orchestration.NodeId)
  })
_sym_db.RegisterMessage(NodeId)



_CLIENTCOMMUNICATION = _descriptor.ServiceDescriptor(
  name='ClientCommunication',
  full_name='Orchestration.ClientCommunication',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=418,
  serialized_end=814,
  methods=[
  _descriptor.MethodDescriptor(
    name='produceMessage',
    full_name='Orchestration.ClientCommunication.produceMessage',
    index=0,
    containing_service=None,
    input_type=_ABSTRACTMESSAGE,
    output_type=_ROUNDNUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='publishMessage',
    full_name='Orchestration.ClientCommunication.publishMessage',
    index=1,
    containing_service=None,
    input_type=_ABSTRACTMESSAGE,
    output_type=_ROUNDNUMBER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='triggerRound',
    full_name='Orchestration.ClientCommunication.triggerRound',
    index=2,
    containing_service=None,
    input_type=_ROUNDNUMBER,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='pullMessageForRound',
    full_name='Orchestration.ClientCommunication.pullMessageForRound',
    index=3,
    containing_service=None,
    input_type=_ROUNDNUMBER,
    output_type=_QUEUEMESSAGEBULK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='registerListener',
    full_name='Orchestration.ClientCommunication.registerListener',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CLIENTINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLIENTCOMMUNICATION)

DESCRIPTOR.services_by_name['ClientCommunication'] = _CLIENTCOMMUNICATION


_SERVERFACINGCLIENT = _descriptor.ServiceDescriptor(
  name='ServerFacingClient',
  full_name='Orchestration.ServerFacingClient',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=816,
  serialized_end=909,
  methods=[
  _descriptor.MethodDescriptor(
    name='NotifyRoundFinished',
    full_name='Orchestration.ServerFacingClient.NotifyRoundFinished',
    index=0,
    containing_service=None,
    input_type=_ROUNDNUMBER,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERFACINGCLIENT)

DESCRIPTOR.services_by_name['ServerFacingClient'] = _SERVERFACINGCLIENT

# @@protoc_insertion_point(module_scope)