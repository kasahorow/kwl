#coding: utf-8
from sua import *

data = {
  'conjugate': {
      'prefix': {
      },
        'aller' : {
    'tdy' : {JE:'vais', TU:'vas', IL:'va', ELLE:'va', NOUS:'allons', VOUS:'allez', ILS:'vont', ELLES:'vont'},
    'tmw' : {JE:'irai', TU:'iras', IL:'ira', ELLE:'ira', IT:'ira', NOUS:'irons', VOUS:'irez', ILS:'iront', ELLES:'iront'},
    'ydy' : {JE:'allais', TU:'allais', ELLE:'allait', IL:'allait', IT:'allait', NOUS:'allions', VOUS:'alliez', \
      ELLES:'allaient', ILS:'allaient'},
    'conditional' : ['irais', 'irais', 'irait', 'irions', 'iriez', \
      'iraient'],
    'past participle' : 'allé'
    },

  'avoir' : {
    'tdy' : ['ai', 'as', 'a', 'avons', 'avez', 'ont'],
    'tmw' : ['aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront'],
    'ydy' : ['avais', 'avais', 'avait', 'avions', 'aviez', 'avaient'],
    'conditional' : ['aurais', 'aurais', 'aurait', 'aurions', 'auriez', \
      'auraient'],
    'past participle' : 'eu'
    },

  'dormir' : {
    'tdy' : {JE:'dors', TU:'dors', IL:'dort', ELLE:'dort', NOUS:'dormons', VOUS:'dormez', ILS:'dormont', ELLES:'dormont'},
    'ydy' : {JE:'dormais', TU:'dormais', IL:'dormait', ELLE:'dormait', NOUS:'dormions', VOUS:'dormiez', ILS:'dormaient', ELLES:'dormaient'},
   },
        u'être' : {
    'tdy' : {JE:'suis', TU:'es', ELLE:'est', IL:'est', IT:'est', NOUS:'sommes', VOUS:u'êtes', ILS:'sont', ELLES:'sont'},
    'tmw' : {JE:'serai', TU:'seras', ELLE:'sera', IL:'sera', IT:'sera', NOUS:'serons', VOUS:'serez', ILS:'seront', ELLES:'seront'},
    'ydy' : {JE:u'étais', TU:u'étais', ELLE:u'était', IT:u'était', IL:u'était', NOUS:u'étions', VOUS:u'étiez', ELLES:u'étaient', ILS:u'étaient'},
    'conditional' : ['serais', 'serais', 'serait', 'serions', 'seriez', \
      'seraient'],
    'past participle' : 'été'
    },
        'devoir' : {
    'tdy' : ['dois', 'dois', 'doit', 'devons', 'devez', 'doivent'],
    'tmw' : ['devrai', 'devras', 'devra', 'devrons', 'devrez', \
      'devront'],
    'ydy' : ['devais', 'devais', 'devait', 'devions', 'deviez', \
      'devaient'],
    'conditional' : ['devrais', 'devrais', 'devrait', 'devrions', \
      'devriez', 'devraient'],
    'past participle' : 'dû'
    },

  'faire' : {
    'tdy' : ['fais', 'fais', 'fait', 'faisons', 'faites', 'font'],
    'tmw' : ['ferai', 'feras', 'fera', 'ferons', 'ferez', 'feront'],
    'ydy' : ['faisais', 'faisais', 'faisait', 'faisions', 'faisez', \
      'faisaient'],
    'conditional' : ['ferais', 'ferais', 'ferait', 'ferions', 'feriez', \
      'feraient'],
    'past participle' : 'fait'
    },

  'mettre' : {
    'tdy' : ['mets', 'mets', 'met', 'mettons', 'mettez', 'mettent'],
    'tmw' : ['mettrai', 'mettras', 'mettra', 'mettrons', 'mettrez', \
      'mettront'],
    'ydy' : ['mettais', 'mettais', 'mettait', 'mettions', 'mettiez', \
      'mettaient'],
    'conditional' : ['mettrais', 'mettrais', 'mettrait', 'mettrions', \
      'mettriez', 'mettraient'],
    'past participle' : 'mis'
    },

  'pouvoir' : {
    'tdy' : ['peux', 'peux', 'peut', 'pouvons', 'pouvez', 'peuvent'],
    'tmw' : ['pourrai', 'pourras', 'pourra', 'pourrons', 'pourrez', \
      'pourront'],
    'ydy' : ['pouvais', 'pouvais', 'pouvait', 'pouvions', 'pouviez', \
      'pouvaient'],
    'conditional' : ['pourrais', 'pourrais', 'pourrait', 'pourrions', \
      'pourriez', 'pourraient'],
    'past participle' : 'pu'
    },
        'savoir' : {
    'tdy' : ['sais', 'sais', 'sait', 'savons', 'savez', 'savent'],
    'tmw' : ['saurai', 'sauras', 'saura', 'saurons', 'saurez', \
      'sauront'],
    'ydy' : ['savais', 'savais', 'savait', 'savions', 'saviez', \
      'savaient'],
    'conditional' : ['saurais', 'saurais', 'saurait', 'saurions', \
      'sauriez', 'sauraient'],
    'past participle' : 'su'
    },

  'voir' : {
    'tdy' : ['vois', 'vois', 'voit', 'voyons', 'voyez', 'voient'],
    'tmw' : ['verrai', 'verras', 'verra', 'verrons', 'verrez', \
      'verront'],
    'ydy' : ['voyais', 'voyais', 'voyait', 'voyions', 'voyiez', \
      'voyaient'],
    'conditional' : ['verrais', 'verrais', 'verrait', 'verrions', \
      'verriez', 'verraient'],
    'past participle' : 'vu'
    },
      'suffix': {
        'er' : {
          'inf': 'er',
          'tdy' : {JE:'e', TU:'es', IL:'e', IT:'e', ELLE:'e', NOUS:'ons', VOUS:'ez', ILS:'ent', ELLES:'ent'},
          'tmw' : {JE:'erai', TU:'eras', IL:'era', IT:'era', ELLE:'era', NOUS:'erons', VOUS:'erez', ELLES:'eront', ILS:'eront'},
          'ydy' : {JE:'ais', TU:'ais', ELLE:'ait', IL:'ait', IT:'ait', NOUS:'ions', VOUS:'iez', ELLES:'aient', ILS:'aient'},
    'conditional' : ['erais', 'erais', 'erait', 'erions', 'eriez', \
      'eraient'],
          'past participle' : u'é'
    },
  'ir' : {
    'inf': 'ir',
    'tdy' : {JE:'is', TU:'is', IL:'it', IT:'it', ELLE:'it', NOUS:'issons', VOUS:'issez', ILS:'issent', ELLES:'issent'},
    'tmw' : {JE:'irai', TU:'iras', ELLE:'ira', IL:'ira', IT:'ira', NOUS:'irons', VOUS:'irez', ELLES:'iront', ILS:'iront'},
    'ydy' : {JE:'issais', TU:'issais', ELLE:'issait', IL:'issait', IT:'issait', NOUS:'issions', VOUS:'issiez', \
      ELLES:'issaient', ILS:'issaient'},
    'conditional' : ['irais', 'irais', 'irait', 'irions', 'iriez', \
      'iraient'],
    'past participle' : 'i'
    },
  're' : {
    'inf': 're',
    'tdy' : {JE:'s', TU:'s', IL:'', IT:'', ELLE:'', NOUS:'ons', VOUS:'ez', ILS:'ent', ELLES:'ent'},
    'tmw' : {JE:'rai', TU:'ras', ELLE:'ra', IT:'ra', IL:'ra',  NOUS:'rons', VOUS:'rez', ILS:'ront'},
    'ydy' : {JE:'ais', TU:'ais', ELLE:'ait', IT:'ait', IL:'ait', NOUS:'ions', VOUS:'iez', ILS:'aient'},
    'condtional' : ['rais', 'rais', 'rait', 'rions', 'riez', 'raient'],
    'past participle' : 'u'
    },
      },
    },
    'order': latin['order'],
    'order_triple': latin['order_triple'],
    'plural': {
      'suffix': {'':'s'},
    },
  'subs': [
    ('[a]', ''),
    ('oiez', 'oyez'),
  ('oions', 'oyons'),
  ('iiez', 'yiez'),
  ('iions', 'yions'),
  ('oia', 'oya'),
  ('je ai', "j'ai"),
  ('la livre', 'le livre'),
  ('ma livre', 'mon livre'),
  ], 
}
