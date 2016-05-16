#coding: utf-8
from sua import *

data = {
  'conjugate': {
    'koya': {
      'tdy': {JE:'naye', TU:'oye', ELLE:'aye', IL:'aye', NOUS:'toye', VOUS:'boye', ILS:'baye', ELLES:'baye'},
    },
    'prefix': {
      'default': {
    'inf': 'ko',
    'tdy': {JE:'na', TU:'o', ELLE:'a', IL:'a', IT: 'e', NOUS:'to', VOUS:'bo', ILS:'ba'},
    'ydy': {JE:'na', TU:'o', ELLE:'a', IL:'a', IT: 'e', NOUS:'to', VOUS:'bo', ILS:'ba'},
    'tmw': {JE:'nako', TU:'oko', ELLE:'ako', IL:'ako', IT:'ako',  NOUS:'toko', VOUS:'boko', ILS:'bako'},
  },
    },
    'suffix': {
      'default': {
    'inf': u'a',
    'tdy': 'i',
    'tmw': u'a',
    'ydy': 'aki',
  },
    },
  },
  'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'alliterate': {
      'prefix': {
        '': ' ya ',
        'a': ' ya ',
        'e': ' na ',
        'm': ' ya ',
        'y': ' na ',
      },
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
  ('ani azali ', 'ani aza '),
  ('lii', 'lei'),
  ], 
}
