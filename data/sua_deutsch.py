#coding: utf-8
from sua import *

data = {
  'order': latin['order'], #{'n_p': (0, 1), 'a_p': (0, 1), 'd_p': (0, 1), 'det_nom': (0, 1), 'adj_nom': (0,1), 'pro_nom': (0, 1)},
    'order_triple': latin['order_triple'],
    'plural': {
      'suffix': {'':'en'},
    },
    'conjugate': {
      'prefix': {
        'default': {
          'tmw': {JE: 'werde ', TU: 'wirst ', IT: 'wird', IL: 'wird ', ELLE: 'wird ', NOUS: 'werden ', VOUS: 'werdet ', ILS: 'werden ', ELLES: 'werden ' },
         },
      },
      'suffix': {
        'default': {
          'inf': 'en',
          'tmw': 'en',
          'tdy': {JE: 'e', TU: 'st', IT: 't', IL: 't', ELLE: 't', NOUS: 'en', VOUS: 't', ILS: 'en', ELLES: 'en' },
          'ydy': {JE: 'te', TU: 'test', IT: 'te', IL: 'te', ELLE: 'te', NOUS: 'ten', VOUS: 'tet', ILS: 'ten', ELLES: 'ten' },
         },
      },
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
  ('gehte', 'ging'),
  ('gn', 'gen'),
  ('meine buch', 'mein buch'),
  ], 
}
