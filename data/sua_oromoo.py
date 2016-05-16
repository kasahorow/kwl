#coding: utf-8
from sua import *

data = {
  'conjugate': {
    'prefix': {
      'default': {
    'tdy': '',
    'ydy': '',
    'tmw': 'ni ',
  },
    },
    'suffix': {
      'default': {
    'tdy': {JE:'aan jiraa', TU:'aa jirtaa', ELLE:'aa jirtii', IL:'aa jiraa', IT:'aa jiraa', NOUS:'aa jirraa', VOUS:'aa jirtuu', ILS:'aa jiranii', ELLES:'aa jiranii'},
    'ydy': 'ee',
    'tmw': {JE:'dhaa', TU:'ttaa', IT:'aa', IL:'aa', ELLE:'tii', NOUS:'nnaa', VOUS:'tuu', ILS:'anii', ELLES:'anii'},
  },
    },
  },
  'order': bantu['order'],
  'order_triple': bantu['order_triple'],
  'subs': [
    ('[a]', ''),
    ('chdh', 'dh'),
  ('chtt', 'tt'),
  ('cht', 't'),
  ('chnn', 'nn'),
  ('chn', 'n'),
  ('_', ''),
  ], 
}
