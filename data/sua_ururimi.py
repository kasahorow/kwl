#coding: utf-8
from sua import *

data = {
  'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'plural': {
      'prefix': {'ij':'amaj'},  # Noun classes, key-length = 1
    },
    'conjugate': {
      'prefix': {
        'default': {
          'inf': 'ku',
          'tdy': {JE:'nra', TU:'ura', ELLE:'ara', IL:'ara', IT:'ara', NOUS:'tura', VOUS:'mura', ILS:'bara'},
          'ydy': {JE:'na', TU:'wa', ELLE:'ya', IT:'ya', IL:'ya', NOUS:'twa', VOUS:'mwa', ILS:'ba'},
          'tmw': {JE:'nza', TU:'uza', ELLE:'aza', IT:'aza', IL:'aza', NOUS:'tuza', VOUS:'muza', ILS:'baza'},
        },
      },
      'suffix': {
        'default': {
          'inf': 'a',
          'tdy': 'a',
          'ydy': 'e',
          'tmw': 'a',
        },
      },
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
  ('amai', 'ama'),
  ('nra', 'nda'),
  ('agende', 'agiye'),  # Past tense of verb kugenda
  ('akore', 'akoze'), # Past tense of verb gukora
  #('ua', 'wa'),
  ('turaba', 'ni'),
  ('uraba', 'ni'),
  ('ndaba', 'ni'),
  ('baraba', 'ni'),
  ('muraba', 'ni'),
  ('araba', 'ni'),
  ], 
}
