# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: seating.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rseating.proto\"L\n#AddChairToSeatingArrangementRequest\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\x05\x12\x13\n\x0b\x61rrangement\x18\x02 \x01(\t\"x\n!AddChairToSeatingArrangementReply\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x42\n\n\x08_messageB\x08\n\x06_error\"=\n(RemoveChairFromSeatingArrangementRequest\x12\x11\n\tchair_ids\x18\x01 \x01(\t\"}\n&RemoveChairFromSeatingArrangementReply\x12\x14\n\x07message\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x0bstatus_code\x18\x03 \x01(\x05\x42\n\n\x08_messageB\x08\n\x06_error2\xf4\x01\n\x0bSeatingCall\x12j\n\x1c\x41\x64\x64\x43hairToSeatingArrangement\x12$.AddChairToSeatingArrangementRequest\x1a\".AddChairToSeatingArrangementReply\"\x00\x12y\n!RemoveChairFromSeatingArrangement\x12).RemoveChairFromSeatingArrangementRequest\x1a\'.RemoveChairFromSeatingArrangementReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'seating_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDCHAIRTOSEATINGARRANGEMENTREQUEST._serialized_start=17
  _ADDCHAIRTOSEATINGARRANGEMENTREQUEST._serialized_end=93
  _ADDCHAIRTOSEATINGARRANGEMENTREPLY._serialized_start=95
  _ADDCHAIRTOSEATINGARRANGEMENTREPLY._serialized_end=215
  _REMOVECHAIRFROMSEATINGARRANGEMENTREQUEST._serialized_start=217
  _REMOVECHAIRFROMSEATINGARRANGEMENTREQUEST._serialized_end=278
  _REMOVECHAIRFROMSEATINGARRANGEMENTREPLY._serialized_start=280
  _REMOVECHAIRFROMSEATINGARRANGEMENTREPLY._serialized_end=405
  _SEATINGCALL._serialized_start=408
  _SEATINGCALL._serialized_end=652
# @@protoc_insertion_point(module_scope)