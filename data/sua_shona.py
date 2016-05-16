#coding: utf-8
from sua import *

data = {
  'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'plural': {
      'prefix': {'ch':'zv'},  # Noun classes, key-length = 1
    },
    'conjugate': {
      'prefix': {
        've': {  # uve [to be]
          'tdy': {JE: 'ndiri', TU: 'uri', ELLE: 'ari', IT: 'ari', IL: 'ari', NOUS: 'tiri', VOUS: 'muri', ILS: 'vari'},
        },
        'default': {
          'inf': 'ku',
          'tdy': {JE:'ndino', TU:'uno', ELLE:'ano', IT: 'ano', IL:'ano', NOUS:'tino', VOUS:'muno', ILS:'vano'},
          'ydy': {JE:'ndaka', TU:'waka', ELLE:'aka', IT: 'aka', IL:'aka', NOUS:'taka', VOUS:'maka', ILS:'vaka'},
          'tmw': {JE:'ndicha', TU:'ucha', ELLE:'acha', IT: 'acha', IL:'acha', NOUS:'ticha', VOUS:'mucha', ILS:'vacha'},
        },
      },
      'suffix': {
        've': { 'inf': '', 'tdy': '', }, # uve [to be]
        'default': {
          'inf': 'a',
          'tdy': 'a',
          'ydy': 'a',
          'tmw': 'a',
        },
      },
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
    ('noria', 'ri'),
    ('ari ani', 'ndiani'),
  ], 
}
