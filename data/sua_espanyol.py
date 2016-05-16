#coding: utf-8
from sua import *

data = {
  'order': latin['order'],
    'order_triple': latin['order_triple'],
    'plural': {
      'suffix': {'':'s'},  # Noun classes, key-length = 1
    },
    'conjugate': {
      'suffix': {
        'ar': {
          'inf': 'ar',
          'tdy': {JE:'o', TU:'as', ELLE:'a', IT:'a', IL:'a', NOUS:'amos', VOUS:'avos', ILS:'an'},
          'tmw': {JE:u'aré', TU:'arás', ELLE:u'ará', IT:u'ará', IL:u'ará', NOUS:'aremos', VOUS:'aréis', ILS:'arán'},
          'ydy': {JE:u'é', TU:'aste', ELLE:u'ó', IT:u'ó', IL:u'ó', NOUS:'amos', VOUS:'asteis', ILS:'aron'},
        },
      },
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
    ('la libro', 'el libro'),
  ], 
}
