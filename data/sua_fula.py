#coding: utf-8
# References: 
#    http://www.smcm.edu/gambia/wp-content/uploads/sites/31/2015/03/gamble-14.pdf
#    http://www.ibamba.net/pular/manual.pdf
#    http://files.eric.ed.gov/fulltext/ED403752.pdf

from sua import *

data = {
  'order': {'default': (1, 0), 'adj_nom': (1, 0)},
      'order_triple': kwa['order_triple'],
      'plural': {
        'suffix': {'owo':u'ooɓe', 'a':'i'},
      },
      'conjugate': {
        'prefix': {
          'ne': {
            'inf': '',
            'tdy': '',
          },
          'default': {
            'tdy': {JE:u'ɗo ', TU:u'ɗo ', IT:u'ɗi ', IL:u'ɗi ', ELLE:u'ɗi ',
                    NOUS:u'ɗɛn ng', VOUS:u'ɗo ng', ILS:u'ɗi ng', ELLES:u'ɗi ng'},
            'ydy': '',
            'tmw': '',
          },
        },
        'suffix': {
          'ne': {
            'inf': '',
            'tdy': '',
          },
          'default': {
            'inf': 'de',
            'tdy': 'a',
            'tmw': 'at',
            'ydy': 'i',
            'not_ydy': 'aani',
          },
        },
      },
  'subs': [
    ('[a]', ''),
  ],
}
