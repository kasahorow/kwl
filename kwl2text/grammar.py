# coding: utf-8
# Grammar configuration for all languages

JE = 'je'
TU = 'tu'
ELLE = 'el'
IL = 'il'
IT = 'it'
NOUS = 'nu'
VOUS = 'vu'
ILS = 'is'
ELLES = 'es'

afa = {
  # https://en.wikipedia.org/wiki/Afroasiatic_languages
  'order': {'default': (1, 0), 'adj_nom': (0, 1)},
  'order_triple': {'default': (0, 1, 2), },
}
bantu = {
  'order': {'default': (0, 1), 'det_nom': (1, 0), 'adj_nom': (1, 0), 'n_p': (1, 0), 'pos_nom': (1, 0)},
  'order_triple': {'default': (0, 1, 2)},
}
kwa = {
#  'order': {'default': (1, 0), 'act_adv': (0, 1), 'n_p': (0, 1), 'pos_nom': (0, 1), 'nom_in': (0, 1), 'pre_nom': (0, 1), 'tu_adv': (0, 1), 'vous_adv': (0, 1)},
  'order': {'default': (0, 1), 'adj_nom': (1, 0), 'det_nom': (1, 0), 'nom_nom': (1, 0), 'of_p': (1, 0), 'question': {'act_adv': (0, 1)},},
  'order_triple': {'default': (0, 1, 2), 'question': (2, 1, 0), },
}

latin = {
  'order': {'default': (0, 1), 'question': {'act_adv': (1, 0)}, },
  'order_triple': {'default': (0, 1, 2), 'question': (2, 1, 0)},
}

data = {
  'akan': {
    'order': kwa['order'],
    'order_triple': {'default': (0, 1, 2)},
  },
  'amarinya': {
    'order': {'default': (0,1),},
    'order_triple': afa['order_triple'],
    'plural': {
      'suffix': {'': u'ታት'},
    },
  },
  'chewa': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'alliterate': {
      'prefix': {
        'k': ' ya',
      },
    },
  },
  'english': {
    'order': latin['order'],
    'order_triple': latin['order_triple'],
  },
  'french': {
    'order': latin['order'], 
    'order_triple': latin['order_triple'],
    'plural': {
      'suffix': {'':'s'},
    },
  },
  'gadangme': {
    'order': kwa['order'],
    'order_triple': kwa['order_triple'],
    'plural': {
      'suffix': {'':'i'},
    },
  },
  'gbe': {
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
  },
  'german': {
    'order': latin['order'], #{'n_p': (0, 1), 'a_p': (0, 1), 'd_p': (0, 1), 'det_nom': (0, 1), 'adj_nom': (0,1), 'pro_nom': (0, 1)},
    'order_triple': latin['order_triple'],
    'plural': {
      'suffix': {'':'en'},
    },
    'conjugate': {
      'prefix': {
        'default': {
          'tmw': {JE: 'werde ', TU: 'wirst ', IL: 'wird ', ELLE: 'wird ', NOUS: 'werden ', VOUS: 'werdet ', ILS: 'werden ', ELLES: 'werden ' },
         },
      },
      'suffix': {
        'default': {
          'inf': 'en',
          'tmw': 'en',
          'tdy': {JE: 'e', TU: 'st', IL: 't', ELLE: 't', NOUS: 'en', VOUS: 't', ILS: 'en', ELLES: 'en' },
          'ydy': {JE: 'te', TU: 'test', IL: 'te', ELLE: 'te', NOUS: 'ten', VOUS: 'tet', ILS: 'ten', ELLES: 'ten' },
         },
      },
    },
  },
  'gikuyu': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
  },
  'hausa': {
    'order': afa['order'],
    'order_triple': afa['order_triple'],
    'plural': {
      'suffix': {'':'n'},
    },
    'conjugate': {
      'prefix': {
        'ne': {
          'inf': '',
          'tdy': '',
        },
        'default': {
          'inf': 'yi ',
          'tdy': '',
          'tmw': 'za ',
        },
      },
      'suffix': {
        'ne': {
          'inf': '',
          'tdy': '',
        },
        'default': {
          'tdy': 'n',
        },
      },
    },
  },
  'igbo': {
    'order': {'default': (1, 0), 'n_p': (0, 1),},
    'order_triple': kwa['order_triple'],
  },
  'kongo': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
  },
  'lingala': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'alliterate': {
      'prefix': {
        '': ' ya ',
        'a': ' ya ',
        'e': ' na ',
        'm': ' ya ',
        'y': ' na ',
      },
    },
  },
  'luganda': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
  },
  'luwo': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
  },
  'malagasy': {
    'order': {'default': (0, 1), 'a_p': (1, 0), 'adj_nom': (1, 0), 'pos_nom': (1, 0)},
    'order_triple': {'default': (1, 2, 0), 'question': (2, 1, 0)},
    'conjugate': {
      'prefix': {
        'default': {
          'tdy': 'm',
          'ydy': 'n',
          'tmw': 'h',
        },
      },
    },
  },
  'oromo': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
  },
  'shona': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'plural': {
      'prefix': {'ch':'zv'},  # Noun classes, key-length = 1
    },
    'conjugate': {
      'prefix': {
        've': {  # uve [to be]
          'tdy': {JE: 'ndiri', TU: 'uri', ELLE: 'ari', IL: 'ari', NOUS: 'tiri', VOUS: 'muri', ILS: 'vari'},
        },
        'default': {
          'inf': 'ku',
          'tdy': {JE:'ndino', TU:'uno', ELLE:'ano', IL:'ano', NOUS:'tino', VOUS:'muno', ILS:'vano'},
          'ydy': {JE:'ndaka', TU:'waka', ELLE:'aka', IL:'aka', NOUS:'taka', VOUS:'maka', ILS:'vaka'},
          'tmw': {JE:'ndicha', TU:'ucha', ELLE:'acha', IL:'acha', NOUS:'ticha', VOUS:'mucha', ILS:'vacha'},
        },
      },
      'suffix': {
        've': { 'inf': '', 'tdy': '', }, # uve [to be]
        'default': {
          'inf': 'a',
          'tdy': 'a',
          'ydy': 'a',
          'tmw': 'a',
        },
      },
    },
  },
  'sinhala': {
    'order': dict(afa['order'].items() + {'pos_nom': (0, 1)}.items()),
    'order_triple': afa['order_triple'],
  },
  'spanish': {
    'order': latin['order'], 
    'order_triple': latin['order_triple'],
    'plural': {
      'suffix': {'':'s'},  # Noun classes, key-length = 1
    },
    'conjugate': {
      'suffix': {
        'ar': {
          'inf': 'ar',
          'tdy': {JE:'o', TU:'as', ELLE:'a', IL:'a', NOUS:'amos', VOUS:'avos', ILS:'an'},
          'tmw': {JE:u'aré', TU:'arás', ELLE:u'ará', IL:u'ará', NOUS:'aremos', VOUS:'aréis', ILS:'arán'},
          'ydy': {JE:u'é', TU:'aste', ELLE:u'ó', IL:u'ó', NOUS:'amos', VOUS:'asteis', ILS:'aron'},
        },
      },
    },
  },
  'swahili': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'plural': {
      'prefix': {'ji': 'maji', 'ki': 'vi'}, # key-length = 2
    },
  },
  'tigrinya': {
    'order': {'default': (0, 1), },
    'order_triple': afa['order_triple'],
    'plural': {
      'suffix': {'': u'ታት'},
    },
  },
  'ururimi': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'plural': {
      'prefix': {'ij':'amaj'},  # Noun classes, key-length = 1
    },
    'conjugate': {
      'prefix': {
        'default': {
          'inf': 'ku',
          'tdy': {JE:'nra', TU:'ura', ELLE:'ara', IL:'ara', NOUS:'tura', VOUS:'mura', ILS:'bara'},
          'ydy': {JE:'na', TU:'wa', ELLE:'ya', IL:'ya', NOUS:'twa', VOUS:'mwa', ILS:'ba'},
          'tmw': {JE:'nza', TU:'uza', ELLE:'aza', IL:'aza', NOUS:'tuza', VOUS:'muza', ILS:'baza'},
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
  },
  'wolof': {
    'alliterate': {
      'prefix': {
        'm': ' bu',
      },
    },
    'plural': {
      'suffix': {
        'j':' yi'
      },
    },
    'conjugate': {
      'prefix': {
        'default': {
          'inf': '',
          'tdy': {JE:'maa ngi ', TU:'yaa ngi ', ELLE:'mu ngi ', IL:'mu ngi ', NOUS:'nu ngi ', VOUS:'yeena ngi ', ILS:u'ñu ngi '},
          #'ydy': {JE:'', TU:'', ELLE:'', IL:'', NOUS:'', VOUS:'', ILS:''},
          'tmw': {JE:'dinaa ', TU:'dinga ', ELLE:'dina ', IL:'dina ', NOUS:'dinanu ', VOUS:'dingeen ', ILS:u'dinañu '},
        },
      },
      'suffix': {
        'default': {
          'inf': '',
          'ydy': {JE:' naa', TU:' nga', ELLE:' na', IL:' na', NOUS:' nanu', VOUS:' ngeen', ILS:u' nañu'},
        },
      },
    },
    'order': {'n_p': (0, 1), 'a_p': (1, 0), 'det_nom': (1, 0), 'pos_nom': (0, 1), 'adj_nom': (1, 0), 'default': (1, 0)},
    'order_triple': {'default': (0, 1, 2)},
  },
  'yoruba': {
    'order': {'n_p': (0, 1), 'a_p': (1, 0), 'pos_nom': (0, 1), 'adj_nom': (1, 0), 'default': (1, 0)},
    'order_triple': {'default': (0, 1, 2)},
  },
  'zulu': {
    'order': bantu['order'],
    'order_triple': bantu['order_triple'],
    'plural': {
      'prefix': {'in':'izin'},  # Noun classes, key-length = 1
    },
  },
}

