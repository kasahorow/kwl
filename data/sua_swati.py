# coding: utf-8
# Ref: http://learn101.org/xhosa_plural.php
from sua import *

data = {
  'order': bantu['order'],
  'order_triple': bantu['order_triple'],
  'plural': {
      'prefix': {'in': 'izin', 'um':'aba'},
  },
  'conjugate': {
    'prefix': {
      'default': {
        'inf': 'uku',
        'now_tdy': {JE:'nda', TU:'u', ELLE:'uh', IL:'uh', IT:'uh', NOUS:'siya', VOUS:'wa', ELLES:'ba', ILS:'ba'},
        'tdy': {JE:'ndi', TU:'u', ELLE:'u', IL:'u', IT:'u', NOUS:'si', VOUS:'we', ELLES:'be', ILS:'be'},
        'tmw': {JE:'ndizo', TU:'uzo', ELLE:'uzo', IL:'uzo', IT:'uzo', NOUS:'sizo', VOUS:'wazo', ELLES:'bazo', ILS:'bazo'},
        'ydy': {JE:'nda', TU:'u', ELLE:'uh', IL:'uh', IT:'uh', NOUS:'siya', VOUS:'wa', ELLES:'ba', ILS:'ba'},
      },
    },
    'suffix': {
      'default': {
        'inf': 'a',
        'tdy': 'a',
        'tmw': 'a',
        'ydy': 'a',
        'now_tdy': 'ile',
      },
    },
  },
  'stem': {'prefix': 'uku', 'suffix': 'a'},
  'subs': [
    ('[a]', ''),
    ('[the]', ''),
  ]
}
