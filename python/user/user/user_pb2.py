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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"\x9e\x01\n\x0e\x41\x64\x64UserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x15\n\ruser_password\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x0f\n\x07role_id\x18\x06 \x01(\x05\x12\x12\n\x05grade\x18\x07 \x01(\x05H\x00\x88\x01\x01\x42\x08\n\x06_grade\"$\n\x11RemoveUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"-\n\x1aGetAllClassesOfUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\x17\n\x15GetAllTeachersRequest\"`\n\tUserReply\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x42\n\n\x08_messageB\x08\n\x06_error2\xde\x01\n\x08UserCall\x12(\n\x07\x41\x64\x64User\x12\x0f.AddUserRequest\x1a\n.UserReply\"\x00\x12.\n\nRemoveUser\x12\x12.RemoveUserRequest\x1a\n.UserReply\"\x00\x12@\n\x13GetAllClassesOfUser\x12\x1b.GetAllClassesOfUserRequest\x1a\n.UserReply\"\x00\x12\x36\n\x0eGetAllTeachers\x12\x16.GetAllTeachersRequest\x1a\n.UserReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDUSERREQUEST._serialized_start=15
  _ADDUSERREQUEST._serialized_end=173
  _REMOVEUSERREQUEST._serialized_start=175
  _REMOVEUSERREQUEST._serialized_end=211
  _GETALLCLASSESOFUSERREQUEST._serialized_start=213
  _GETALLCLASSESOFUSERREQUEST._serialized_end=258
  _GETALLTEACHERSREQUEST._serialized_start=260
  _GETALLTEACHERSREQUEST._serialized_end=283
  _USERREPLY._serialized_start=285
  _USERREPLY._serialized_end=381
  _USERCALL._serialized_start=384
  _USERCALL._serialized_end=606
# @@protoc_insertion_point(module_scope)
