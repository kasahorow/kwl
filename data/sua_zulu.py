#coding: utf-8
from sua import *

data = {
  'conjugate': {
    'prefix': {
      'ni': {
    'inf': '',
    'tdy': '',
  },
  'default': {
    'inf': 'uku',
    'tdy': {JE:'ngiya', TU:'uya', ELLE:'uya', IL:'uya', IT:'uya', NOUS:'siya', VOUS:'niya', ILS:'baya'},
    'ydy': {JE:'ngi', TU:'ni', ELLE:'u', IL:'u', IT:'u', NOUS:'si', VOUS:'ni', ILS:'ba'},
    'tmw': {JE:'ngizo', TU:'uzo', ELLE:'uzo', IL:'uzo', IT:'uzo',  NOUS:'sizo', VOUS:'nizo', ILS:'bazo'},
  },
    },
    'suffix': {
      'ni': {
    'inf': '',
    'tdy': '',
  },
  'default': {
    'inf': 'a',
    'tdy': 'a',
    'ydy': 'ile',
    'tmw': u'a',
  },
    },
  },
  'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'plural': {
      'prefix': {'in':'izin'},  # Noun classes, key-length = 1
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
  ], 
}
