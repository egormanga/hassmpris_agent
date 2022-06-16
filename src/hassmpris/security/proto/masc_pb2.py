# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: masc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='masc.proto',
  package='MASCPackage',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmasc.proto\x12\x0bMASCPackage\"J\n\x17IssueCertificateRequest\x12\x14\n\x0c\x45ncryptedCSR\x18\x02 \x01(\x0c\x12\x19\n\x11\x45ncryptedCSRNonce\x18\x01 \x01(\x0c\"\xb1\x01\n\x15IssueCertificateReply\x12\"\n\x1a\x45ncryptedClientCertificate\x18\x01 \x01(\x0c\x12\'\n\x1f\x45ncryptedClientCertificateNonce\x18\x02 \x01(\x0c\x12\"\n\x1a\x45ncryptedServerCertificate\x18\x03 \x01(\x0c\x12\'\n\x1f\x45ncryptedServerCertificateNonce\x18\x04 \x01(\x0c\x32m\n\x0bMASCService\x12^\n\x10IssueCertificate\x12$.MASCPackage.IssueCertificateRequest\x1a\".MASCPackage.IssueCertificateReply\"\x00\x62\x06proto3'
)




_ISSUECERTIFICATEREQUEST = _descriptor.Descriptor(
  name='IssueCertificateRequest',
  full_name='MASCPackage.IssueCertificateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='EncryptedCSR', full_name='MASCPackage.IssueCertificateRequest.EncryptedCSR', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EncryptedCSRNonce', full_name='MASCPackage.IssueCertificateRequest.EncryptedCSRNonce', index=1,
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
  serialized_start=27,
  serialized_end=101,
)


_ISSUECERTIFICATEREPLY = _descriptor.Descriptor(
  name='IssueCertificateReply',
  full_name='MASCPackage.IssueCertificateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='EncryptedClientCertificate', full_name='MASCPackage.IssueCertificateReply.EncryptedClientCertificate', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EncryptedClientCertificateNonce', full_name='MASCPackage.IssueCertificateReply.EncryptedClientCertificateNonce', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EncryptedServerCertificate', full_name='MASCPackage.IssueCertificateReply.EncryptedServerCertificate', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EncryptedServerCertificateNonce', full_name='MASCPackage.IssueCertificateReply.EncryptedServerCertificateNonce', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=104,
  serialized_end=281,
)

DESCRIPTOR.message_types_by_name['IssueCertificateRequest'] = _ISSUECERTIFICATEREQUEST
DESCRIPTOR.message_types_by_name['IssueCertificateReply'] = _ISSUECERTIFICATEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IssueCertificateRequest = _reflection.GeneratedProtocolMessageType('IssueCertificateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISSUECERTIFICATEREQUEST,
  '__module__' : 'masc_pb2'
  # @@protoc_insertion_point(class_scope:MASCPackage.IssueCertificateRequest)
  })
_sym_db.RegisterMessage(IssueCertificateRequest)

IssueCertificateReply = _reflection.GeneratedProtocolMessageType('IssueCertificateReply', (_message.Message,), {
  'DESCRIPTOR' : _ISSUECERTIFICATEREPLY,
  '__module__' : 'masc_pb2'
  # @@protoc_insertion_point(class_scope:MASCPackage.IssueCertificateReply)
  })
_sym_db.RegisterMessage(IssueCertificateReply)



_MASCSERVICE = _descriptor.ServiceDescriptor(
  name='MASCService',
  full_name='MASCPackage.MASCService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=283,
  serialized_end=392,
  methods=[
  _descriptor.MethodDescriptor(
    name='IssueCertificate',
    full_name='MASCPackage.MASCService.IssueCertificate',
    index=0,
    containing_service=None,
    input_type=_ISSUECERTIFICATEREQUEST,
    output_type=_ISSUECERTIFICATEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MASCSERVICE)

DESCRIPTOR.services_by_name['MASCService'] = _MASCSERVICE

# @@protoc_insertion_point(module_scope)
