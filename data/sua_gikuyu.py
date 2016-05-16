#coding: utf-8
from sua import *

data = {
  'conjugate': {
    'prefix': {
      'default': {
    'inf': u'gũ',
    'tdy': {JE:u'nĩ', TU:u'nĩũ', ELLE:u'nĩa', IL:u'nĩa', IT:u'nĩa', NOUS:u'nĩtũ', VOUS:u'nĩmũ', ILS:u'nĩma'},
    'tmw': {JE:u'ndĩga', TU:u'nĩũga', ELLE:u'nĩaga', IL:u'nĩaga', IT:u'nĩaga', NOUS:u'nĩtũga', VOUS:u'nĩmũga', ILS:u'nĩmaga'},
    'ydy': {JE:u'nĩ', TU:u'nĩũ', ELLE:u'nĩa', IL:u'nĩa', IT:u'nĩaga', NOUS:u'nĩtũ', VOUS:u'nĩmũ', ILS:u'nĩma'},
  },
    },
    'suffix': {
      'default': {
    'inf': u'a',
    'tdy': 'a',
    'tmw': u'a',
    'ydy': 're',
  },
    },
  },
  'order': bantu['order'],
  'order_triple': bantu['order_triple'],
  'subs': [
    ('[a]', ''),
    ('_', ''),
  ], 
}
