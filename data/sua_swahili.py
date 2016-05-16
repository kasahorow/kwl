#coding: utf-8
from sua import *
data = {
  'conjugate': {
    'ni': {
      'inf': 'ni',
      'tdy': 'ni',
    },
    'prefix': {
  'default': {
    'inf': 'ku',
    'tdy': {JE:'nina', TU:'una', ELLE:'ana', IL:'ana', IT:'ana', NOUS:'tuna', VOUS:'mna', ILS:'wana'},
    'ydy': {JE:'nili', TU:'uli', ELLE:'ali', IL:'ali', IT:'ali', NOUS:'tuli', VOUS:'mli', ILS:'wali'},
    'tmw': {JE:'nita', TU:'uta', ELLE:'ata', IL:'ata', IT:'ata', NOUS:'tuta', VOUS:'mta', ILS:'wata'},
  },
    },
    'suffix': {
      'default': {
        'inf': 'a',
        'tdy': 'a',
        'ydy': 'a',
        'tmw': 'a',
      },
    },
  },
  'order': bantu['order'],
  'order_triple': bantu['order_triple'],
  'plural': {
    'prefix': {'ji': 'maji', 'ki': 'vi'}, # key-length = 2
  },
  'subs': [
    ('[a]', ''),
    ('_', ''),
  ('Nani anania', 'Ambao ni'),
  ('ya angu', 'yangu'),
  ('ya ake', 'yake'),
  ('siku kila', 'kila siku'),
  ], 
}
