#coding: utf-8
from sua import *

data = {
  'alliterate': {
      'prefix': {
        'm': ' bu',
      },
    },
    'plural': {
      'suffix': {
        'j':'j yi'
      },
    },
    'conjugate': {
      'prefix': {
        'default': {
          'inf': '',
          'tdy': {JE:'maa ngi ', TU:'yaa ngi ', ELLE:'mu ngi ', IT:'mu ngi', IL:'mu ngi ', NOUS:'nu ngi ', VOUS:'yeena ngi ', ILS:u'ñu ngi '},
          #'ydy': {JE:'', TU:'', ELLE:'', IL:'', NOUS:'', VOUS:'', ILS:''},
          'tmw': {JE:'dinaa ', TU:'dinga ', ELLE:'dina ', IT:'dina ', IL:'dina ', NOUS:'dinanu ', VOUS:'dingeen ', ILS:u'dinañu '},
        },
      },
      'suffix': {
        'default': {
          'inf': '',
          'ydy': {JE:' naa', TU:' nga', ELLE:' na', IT:' na', IL:' na', NOUS:' nanu', VOUS:' ngeen', ILS:u' nañu'},
        },
      },
    },
    'order': {'n_p': (0, 1), 'a_p': (1, 0), 'det_nom': (1, 0), 'pos_nom': (0, 1), 'adj_nom': (1, 0), 'default': (1, 0)},
    'order_triple': {'default': (0, 1, 2)},
  'subs': [
    ('[a]', ''),
  ], 
}
