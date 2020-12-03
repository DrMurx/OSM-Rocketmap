# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/deep_linking_enum_wrapper.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/deep_linking_enum_wrapper.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0pogoprotos/enums/deep_linking_enum_wrapper.proto\x12\x10pogoprotos.enums\"\x9f\x04\n\x16\x44\x65\x65pLinkingEnumWrapper\"E\n\tTodayStep\x12\x0e\n\nTODAY_VIEW\x10\x00\x12\x12\n\x0e\x46IELD_RESEARCH\x10\x01\x12\x14\n\x10SPECIAL_RESEARCH\x10\x02\"\xc1\x02\n\x04Open\x12\t\n\x05UNSET\x10\x00\x12\r\n\tOPEN_SHOP\x10\x01\x12\r\n\tOPEN_NEWS\x10\x02\x12\x16\n\x12OPEN_BATTLE_LEAGUE\x10\x03\x12\x11\n\rOPEN_SETTINGS\x10\x04\x12\x17\n\x13OPEN_PLAYER_PROFILE\x10\x05\x12\x0e\n\nOPEN_BUDDY\x10\x06\x12\x15\n\x11OPEN_AVATAR_ITEMS\x10\x07\x12\x13\n\x0fOPEN_QUEST_LIST\x10\x08\x12\x1a\n\x16OPEN_POKEMON_INVENTORY\x10\t\x12\x17\n\x13OPEN_NEARBY_POKEMON\x10\n\x12\x10\n\x0cOPEN_POKEDEX\x10\x0b\x12\x0f\n\x0bOPEN_EVENTS\x10\x0c\x12\x10\n\x0cOPEN_JOURNAL\x10\r\x12\r\n\tOPEN_TIPS\x10\x0e\x12\x17\n\x13OPEN_ITEM_INVENTORY\x10\x0f\"%\n\x04Mode\x12\x12\n\x0eNEARBY_POKEMON\x10\x00\x12\t\n\x05RAIDS\x10\x01\"/\n\x04Type\x12\x10\n\x0c\x43OMBAT_PARTY\x10\x00\x12\x0b\n\x07POKEMON\x10\x01\x12\x08\n\x04\x45GGS\x10\x02\"\"\n\x06Screen\x12\x0b\n\x07PROFILE\x10\x00\x12\x0b\n\x07\x46RIENDS\x10\x01\x62\x06proto3')
)



_DEEPLINKINGENUMWRAPPER_TODAYSTEP = _descriptor.EnumDescriptor(
  name='TodayStep',
  full_name='pogoprotos.enums.DeepLinkingEnumWrapper.TodayStep',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TODAY_VIEW', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIELD_RESEARCH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECIAL_RESEARCH', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=97,
  serialized_end=166,
)
_sym_db.RegisterEnumDescriptor(_DEEPLINKINGENUMWRAPPER_TODAYSTEP)

_DEEPLINKINGENUMWRAPPER_OPEN = _descriptor.EnumDescriptor(
  name='Open',
  full_name='pogoprotos.enums.DeepLinkingEnumWrapper.Open',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_SHOP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_NEWS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_BATTLE_LEAGUE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_SETTINGS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_PLAYER_PROFILE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_BUDDY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_AVATAR_ITEMS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_QUEST_LIST', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_POKEMON_INVENTORY', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_NEARBY_POKEMON', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_POKEDEX', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_EVENTS', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_JOURNAL', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_TIPS', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPEN_ITEM_INVENTORY', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=169,
  serialized_end=490,
)
_sym_db.RegisterEnumDescriptor(_DEEPLINKINGENUMWRAPPER_OPEN)

_DEEPLINKINGENUMWRAPPER_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='pogoprotos.enums.DeepLinkingEnumWrapper.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NEARBY_POKEMON', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAIDS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=492,
  serialized_end=529,
)
_sym_db.RegisterEnumDescriptor(_DEEPLINKINGENUMWRAPPER_MODE)

_DEEPLINKINGENUMWRAPPER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='pogoprotos.enums.DeepLinkingEnumWrapper.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COMBAT_PARTY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGGS', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=531,
  serialized_end=578,
)
_sym_db.RegisterEnumDescriptor(_DEEPLINKINGENUMWRAPPER_TYPE)

_DEEPLINKINGENUMWRAPPER_SCREEN = _descriptor.EnumDescriptor(
  name='Screen',
  full_name='pogoprotos.enums.DeepLinkingEnumWrapper.Screen',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROFILE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIENDS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=580,
  serialized_end=614,
)
_sym_db.RegisterEnumDescriptor(_DEEPLINKINGENUMWRAPPER_SCREEN)


_DEEPLINKINGENUMWRAPPER = _descriptor.Descriptor(
  name='DeepLinkingEnumWrapper',
  full_name='pogoprotos.enums.DeepLinkingEnumWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEEPLINKINGENUMWRAPPER_TODAYSTEP,
    _DEEPLINKINGENUMWRAPPER_OPEN,
    _DEEPLINKINGENUMWRAPPER_MODE,
    _DEEPLINKINGENUMWRAPPER_TYPE,
    _DEEPLINKINGENUMWRAPPER_SCREEN,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=614,
)

_DEEPLINKINGENUMWRAPPER_TODAYSTEP.containing_type = _DEEPLINKINGENUMWRAPPER
_DEEPLINKINGENUMWRAPPER_OPEN.containing_type = _DEEPLINKINGENUMWRAPPER
_DEEPLINKINGENUMWRAPPER_MODE.containing_type = _DEEPLINKINGENUMWRAPPER
_DEEPLINKINGENUMWRAPPER_TYPE.containing_type = _DEEPLINKINGENUMWRAPPER
_DEEPLINKINGENUMWRAPPER_SCREEN.containing_type = _DEEPLINKINGENUMWRAPPER
DESCRIPTOR.message_types_by_name['DeepLinkingEnumWrapper'] = _DEEPLINKINGENUMWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeepLinkingEnumWrapper = _reflection.GeneratedProtocolMessageType('DeepLinkingEnumWrapper', (_message.Message,), dict(
  DESCRIPTOR = _DEEPLINKINGENUMWRAPPER,
  __module__ = 'pogoprotos.enums.deep_linking_enum_wrapper_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.enums.DeepLinkingEnumWrapper)
  ))
_sym_db.RegisterMessage(DeepLinkingEnumWrapper)


# @@protoc_insertion_point(module_scope)