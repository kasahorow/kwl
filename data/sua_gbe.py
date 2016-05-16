#coding: utf-8
from sua import *

data = {
  'conjugate': {
      'prefix': {
        'default': {
            'now_tdy': 'le ... ',
            'tmw': u'a',
            'ydy': '',
        },
        u'yɛ': {
          'tdy': 'nye',
        }
      },
      'suffix': {
        'default': {
          'now_tdy': 'm',
          'tdy': '',
          'ydy': '',
        }
      }
},
    'order': kwa['order'],
    'order_triple': kwa['order_triple'],
    'plural': {
      'suffix': {'':'wo'},
    },
  'subs': [
    ('[a]', ''),
    ('_', ''),
    (u'nyenyɛ', 'nye'),
  ], 
}
