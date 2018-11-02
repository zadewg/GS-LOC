# source: location.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='location.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0elocation.proto\"\xc5\x02\n\x08Response\x12%\n\x05wifis\x18\x02 \x03(\x0b\x32\x16.Response.ResponseWifi\x1a\x91\x02\n\x0cResponseWifi\x12\x0b\n\x03mac\x18\x01 \x01(\t\x12\x35\n\x08location\x18\x02 \x01(\x0b\x32#.Response.ResponseWifi.WifiLocation\x12\x0f\n\x07\x63hannel\x18\x15 \x01(\x05\x1a\xab\x01\n\x0cWifiLocation\x12\x10\n\x08latitude\x18\x01 \x01(\x03\x12\x11\n\tlongitude\x18\x02 \x01(\x03\x12\x10\n\x08\x61\x63\x63uracy\x18\x03 \x01(\x05\x12\x12\n\nzeroField4\x18\x04 \x01(\x05\x12\x10\n\x08\x61ltitude\x18\x05 \x01(\x05\x12\x18\n\x10\x61ltitudeAccuracy\x18\x06 \x01(\x05\x12\x11\n\tunknown11\x18\x0b \x01(\x05\x12\x11\n\tunknown12\x18\x0c \x01(\x05\"\x81\x01\n\x07Request\x12#\n\x05wifis\x18\x02 \x03(\x0b\x32\x14.Request.RequestWifi\x12\x10\n\x05\x66ound\x18\x03 \x01(\x05:\x01\x30\x12\x13\n\x08notfound\x18\x04 \x01(\x05:\x01\x30\x12\x0e\n\x06source\x18\x05 \x01(\t\x1a\x1a\n\x0bRequestWifi\x12\x0b\n\x03mac\x18\x01 \x01(\t')
)




_RESPONSE_RESPONSEWIFI_WIFILOCATION = _descriptor.Descriptor(
  name='WifiLocation',
  full_name='Response.ResponseWifi.WifiLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Response.ResponseWifi.WifiLocation.latitude', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Response.ResponseWifi.WifiLocation.longitude', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='Response.ResponseWifi.WifiLocation.accuracy', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zeroField4', full_name='Response.ResponseWifi.WifiLocation.zeroField4', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='Response.ResponseWifi.WifiLocation.altitude', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitudeAccuracy', full_name='Response.ResponseWifi.WifiLocation.altitudeAccuracy', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown11', full_name='Response.ResponseWifi.WifiLocation.unknown11', index=6,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='Response.ResponseWifi.WifiLocation.unknown12', index=7,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=344,
)

_RESPONSE_RESPONSEWIFI = _descriptor.Descriptor(
  name='ResponseWifi',
  full_name='Response.ResponseWifi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='Response.ResponseWifi.mac', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='Response.ResponseWifi.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel', full_name='Response.ResponseWifi.channel', index=2,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_RESPONSEWIFI_WIFILOCATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=344,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wifis', full_name='Response.wifis', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_RESPONSEWIFI, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=344,
)


_REQUEST_REQUESTWIFI = _descriptor.Descriptor(
  name='RequestWifi',
  full_name='Request.RequestWifi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='Request.RequestWifi.mac', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=476,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wifis', full_name='Request.wifis', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='found', full_name='Request.found', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notfound', full_name='Request.notfound', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='Request.source', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_REQUESTWIFI, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=476,
)

_RESPONSE_RESPONSEWIFI_WIFILOCATION.containing_type = _RESPONSE_RESPONSEWIFI
_RESPONSE_RESPONSEWIFI.fields_by_name['location'].message_type = _RESPONSE_RESPONSEWIFI_WIFILOCATION
_RESPONSE_RESPONSEWIFI.containing_type = _RESPONSE
_RESPONSE.fields_by_name['wifis'].message_type = _RESPONSE_RESPONSEWIFI
_REQUEST_REQUESTWIFI.containing_type = _REQUEST
_REQUEST.fields_by_name['wifis'].message_type = _REQUEST_REQUESTWIFI
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  ResponseWifi = _reflection.GeneratedProtocolMessageType('ResponseWifi', (_message.Message,), dict(

    WifiLocation = _reflection.GeneratedProtocolMessageType('WifiLocation', (_message.Message,), dict(
      DESCRIPTOR = _RESPONSE_RESPONSEWIFI_WIFILOCATION,
      __module__ = 'location_pb2'
      # @@protoc_insertion_point(class_scope:Response.ResponseWifi.WifiLocation)
      ))
    ,
    DESCRIPTOR = _RESPONSE_RESPONSEWIFI,
    __module__ = 'location_pb2'
    # @@protoc_insertion_point(class_scope:Response.ResponseWifi)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'location_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.ResponseWifi)
_sym_db.RegisterMessage(Response.ResponseWifi.WifiLocation)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(

  RequestWifi = _reflection.GeneratedProtocolMessageType('RequestWifi', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST_REQUESTWIFI,
    __module__ = 'location_pb2'
    # @@protoc_insertion_point(class_scope:Request.RequestWifi)
    ))
  ,
  DESCRIPTOR = _REQUEST,
  __module__ = 'location_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  ))
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.RequestWifi)


# @@protoc_insertion_point(module_scope)
