#coding: utf-8
from sua import *

data = {
  'conjugate': {
      'prefix': {
        'default': {
          'inf': 'ku',
          'tdy': {JE:'ndima', TU:'uma', ELLE:'ama', IL:'ama', IT:'ama',  NOUS:'tima', VOUS:'muma', ILS:'ama'},
          'now_tdy': {JE:'ndiku', TU:'uku', ELLE:'aku', IL:'aku', IT:'aku',  NOUS:'tiku', VOUS:'muku', ILS:'aku'},
          'ydy': {JE:'ndina', TU:'una', ELLE:'ana', IL:'ana', IT:'ana', NOUS:'tina', VOUS:'muna', ILS:'ana'},
          'tmw': {JE:'ndidza', TU:'udza', ELLE:'adza', IL:'adza', IT:'adza',  NOUS:'tidza', VOUS:'mudza', ILS:'adza'},
        },
      },
      'suffix': {
        'default': {
          'inf': 'a',
          'tdy': 'a',
          'tmw': u'a',
          'ydy': 'a',
        },
      },
    },
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'alliterate': {
      'prefix': {
        'k': ' ya',
      },
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
    ('ya la', 'ya'),
  ], 
}
