# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61\x64min.proto\"e\n\nAddRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x0f\n\x07role_id\x18\x05 \x01(\x05\"\x1b\n\x08\x41\x64\x64Reply\x12\x0f\n\x07message\x18\x01 \x01(\t20\n\tAdminCall\x12#\n\x07\x41\x64\x64User\x12\x0b.AddRequest\x1a\t.AddReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'admin_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDREQUEST._serialized_start=15
  _ADDREQUEST._serialized_end=116
  _ADDREPLY._serialized_start=118
  _ADDREPLY._serialized_end=145
  _ADMINCALL._serialized_start=147
  _ADMINCALL._serialized_end=195
# @@protoc_insertion_point(module_scope)
