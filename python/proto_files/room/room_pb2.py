# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: room.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nroom.proto\"L\n\x0e\x41\x64\x64RoomRequest\x12\x11\n\troom_name\x18\x01 \x01(\t\x12\x13\n\x0broom_length\x18\x02 \x01(\x05\x12\x12\n\nroom_width\x18\x03 \x01(\x05\"c\n\x0c\x41\x64\x64RoomReply\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x42\n\n\x08_messageB\x08\n\x06_error\"$\n\x11RemoveRoomRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\x05\"f\n\x0fRemoveRoomReply\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x42\n\n\x08_messageB\x08\n\x06_error2m\n\x08RoomCall\x12+\n\x07\x41\x64\x64Room\x12\x0f.AddRoomRequest\x1a\r.AddRoomReply\"\x00\x12\x34\n\nRemoveRoom\x12\x12.RemoveRoomRequest\x1a\x10.RemoveRoomReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'room_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDROOMREQUEST._serialized_start=14
  _ADDROOMREQUEST._serialized_end=90
  _ADDROOMREPLY._serialized_start=92
  _ADDROOMREPLY._serialized_end=191
  _REMOVEROOMREQUEST._serialized_start=193
  _REMOVEROOMREQUEST._serialized_end=229
  _REMOVEROOMREPLY._serialized_start=231
  _REMOVEROOMREPLY._serialized_end=333
  _ROOMCALL._serialized_start=335
  _ROOMCALL._serialized_end=444
# @@protoc_insertion_point(module_scope)