# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"\x80\x01\n\x0e\x41\x64\x64UserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x15\n\ruser_password\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x0f\n\x07role_id\x18\x06 \x01(\x05\"c\n\x0c\x41\x64\x64UserReply\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x42\n\n\x08_messageB\x08\n\x06_error\"$\n\x11RemoveUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"f\n\x0fRemoveUserReply\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x42\n\n\x08_messageB\x08\n\x06_error2m\n\x08UserCall\x12+\n\x07\x41\x64\x64User\x12\x0f.AddUserRequest\x1a\r.AddUserReply\"\x00\x12\x34\n\nRemoveUser\x12\x12.RemoveUserRequest\x1a\x10.RemoveUserReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDUSERREQUEST._serialized_start=15
  _ADDUSERREQUEST._serialized_end=143
  _ADDUSERREPLY._serialized_start=145
  _ADDUSERREPLY._serialized_end=244
  _REMOVEUSERREQUEST._serialized_start=246
  _REMOVEUSERREQUEST._serialized_end=282
  _REMOVEUSERREPLY._serialized_start=284
  _REMOVEUSERREPLY._serialized_end=386
  _USERCALL._serialized_start=388
  _USERCALL._serialized_end=497
# @@protoc_insertion_point(module_scope)
