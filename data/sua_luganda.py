#coding: utf-8
from sua import *

data = {
  'conjugate': {
    'ba': {
      'tdy': '',
    },
    'prefix': {
      'default': {
        'inf': 'oku',
        'done_tdy': {JE:'n', TU:'o', ELLE:'a', IL:'a', IT:'a',  NOUS:'tu', VOUS:'mu', ILS:'ba', ELLES:'ba'},
        'not_tdy': {JE:'si', TU:'to', ELLE:'ta', IL:'ta', IT:'ta',  NOUS:'tetu', VOUS:'temu', ILS:'teba', ELLES:'teba'},
        'tdy': {JE:'n', TU:'o', ELLE:'a', IL:'a', IT:'a',  NOUS:'tu', VOUS:'mu', ILS:'ba', ELLES:'ba'},
    'ydy': {JE:'na', TU:'wa', ELLE:'ya', IL:'ya', IT:'ya', NOUS:'twa', VOUS:'mwa', ILS:'ba', ELLES:'ba'},
    'tmw': {JE:'ndi', TU:'oli', ELLE:'ali', IL:'ali', IT:'ali', NOUS:'tuli', VOUS:'muli', ILS:'bali', ELLES:'bali'},
  },
    },
    'suffix': {
      'default': {
    'inf': 'a',
    'done_tdy': 'e',
    'not_tdy': 'a',
    'tdy': 'a',
    'ydy': 'a',
    'tmw': u'a',
  },
    },
  },
  'order': bantu['order'],
  'order_triple': bantu['order_triple'],
  'subs': [
    ('[a]', ''),
    ('_', ''),
    ('akole', 'akoze'),
  ], 
  'voices': {
    'kintu': [
      ('ffe', ''),
      ('ye abeera', ''),
    ],
  }
}
