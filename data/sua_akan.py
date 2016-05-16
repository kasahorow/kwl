# coding: utf-8
from sua import *

data = {
  'conjugate': {
    'prefix': {
      'default': {
    'may': u'bɛtumi a',
    'tdy': '',
    'now_tdy': 're',
    'tmw': u'bɛ',
    'notinf': 'nn',
    'not_tdy': 'nn',
    'done_tdy': 'a',
    'done_ydy': 'a',
  },
  'ba': {
    'cmd': 'bra',
  },
  u'wɔ': {
    'may': u'bɛtumi anya',
    'tdy': u'wɔ',
    'ydy': 'nyaee',
    'tmw': u'bɛnya',
  },
    },
    'suffix': {
      'default': {
      'ydy': 'ee'
      }
    }
  },
  'order': kwa['order'],
  'order_triple': {'default': (0, 1, 2)},
  'subs': [
    (u'nyaeew\u0254ee', u'nyaee'),
    (u'nyaw\u0254', u'nya'),
    (u'w\u0254w\u0254', u'w\u0254'),
    (u'oana yɛ', u'oana nye'),
    (u'ba ha', 'bra ha'),
    ('_', ''),
    ('nbien', 'abien'),
  ],
}

