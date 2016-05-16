#coding: utf-8
from sua import *

data = {
  'conjugate': {
    'in': {
      'tdy': 'en',
      'ydy': 'en',
      'tmw': 'en',
    },
    'prefix': {
      'default': {
    'inf': '',
    'tdy': {JE:'a', TU:'i', ELLE:'o', IL:'o', IT:'o',  NOUS:'wa', VOUS:'wu', ILS:'gi'},
    'ydy': {JE:'ne a', TU:'ne i', ELLE:'ne o', IL:'ne o', IT:'ne o',  NOUS:'ne wa', VOUS:'ne u', ILS:'ne gi'},
    'tmw': {JE:'abiro ', TU:'ibiro ', ELLE:'obiro ', IL:'obiro ', IT:'obiro ',  NOUS:'wabiro ', VOUS:'ubiro ', ILS:'gibiro '},
  },
    },
  },
  'order': bantu['order'],
  'order_triple': bantu['order_triple'],
  'subs': [
    ('[a]', ''),
    ('_', ''),
  ], 
}
