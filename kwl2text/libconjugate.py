# -*- coding: utf-8 -*- 

"""Conjugate verbs"""

import grammar as models
import logging

JE = models.JE
TU = models.TU
ELLE = models.ELLE
IL = models.IL
IT = models.IT
NOUS = models.NOUS
VOUS = models.VOUS
ILS = models.ILS
ELLES = models.ELLES

irregular = {}
starts = {}  # Prefixes
endings = {}  # Suffixes

# Akan
starts['akan'] = {
  'default': {
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
    'tdy': u'wɔ',
    'ydy': 'nyaee',
    'tmw': u'bɛnya',
  },
}
endings['akan'] = {
  'default': {
    'ydy': 'ee'
  }
}

# Chewa
starts['chewa'] = {
  'default': {
    'inf': 'ku',
    'tdy': {JE:'ndima', TU:'uma', ELLE:'ama', IL:'ama', NOUS:'tima', VOUS:'muma', ILS:'ama'},
    'now_tdy': {JE:'ndiku', TU:'uku', ELLE:'aku', IL:'aku', NOUS:'tiku', VOUS:'muku', ILS:'aku'},
    'ydy': {JE:'ndina', TU:'una', ELLE:'ana', IL:'ana', NOUS:'tina', VOUS:'muna', ILS:'ana'},
    'tmw': {JE:'ndidza', TU:'udza', ELLE:'adza', IL:'adza', NOUS:'tidza', VOUS:'mudza', ILS:'adza'},
  }
}
endings['chewa'] = {
  'default': {
    'inf': 'a',
    'tdy': 'a',
    'tmw': u'a',
    'ydy': 'a',
  }
}

# English
starts['english'] = {
  'default': {
    'inf': 'to ',
    'tmw': 'will ',
    'done_tdy': {JE:'have ', TU:'have ', IL:'has ', ELLE:'has ', NOUS:'have ', VOUS:'have ', ILS:'have ', ELLES:'have '},
    'done_ydy': 'had ',
    'not_tmw': ' will not ',
    'not_ydy': ' did not ',
  },
  'be': {
    'tdy': {JE:'am', TU:'are', IL:'is', ELLE:'is', NOUS:'are', VOUS:'are', ILS:'are', ELLES:'are'},
    'ydy': {JE:'was', TU:'were', IL:'was', ELLE:'was', NOUS:'were', VOUS:'were', ILS:'were', ELLES:'were'},
  }
}
endings['english'] = { 
  'default': {
    'done_tdy': 'ed',
    'done_ydy': 'ed',
    'tdy' : {JE:'', TU:'', IL:'s', ELLE:'s', NOUS:'', VOUS:'', ILS:'', ELLES:''},
    'not_tdy': ' not',
    'ydy': 'ed',
  },
  'be': {
    'tdy': '',
    'ydy': '',
   }
}
irregular['english'] = {
  'be': {
    'tdy': {JE:'am', TU:'are', IL:'is', ELLE:'is', NOUS:'are', VOUS:'are', ILS:'are', ELLES:'are'},
    'ydy': {JE:'was', TU:'were', IL:'was', ELLE:'was', NOUS:'were', VOUS:'were', ILS:'were', ELLES:'were'},
  }
}

# French
starts['french'] = {
  'se ': {
    'tdy': {JE:'me '},
  }
}

# Gadangme
starts['gadangme'] = {
  'default': {
    'tdy': 'm',
    'tmw': u'baa',
    'ydy': '',
  }
}

endings['gadangme'] = {
  'default': {
    'tdy': '',
    'ydy': ' omo',
  }
}


# Igbo
starts['igbo'] = {
  'default': {
    'inf': 'ruo ',
    'tdy': 'na-',
    'tmw': u'ga-',
  }
}

# Gikuyu
starts['gikuyu'] = {
  'default': {
    'inf': u'gũ',
    'tdy': {JE:u'nĩ', TU:u'nĩũ', ELLE:u'nĩa', IL:u'nĩa', NOUS:u'nĩtũ', VOUS:u'nĩmũ', ILS:u'nĩma'},
    'tmw': {JE:u'ndĩga', TU:u'nĩũga', ELLE:u'nĩaga', IL:u'nĩaga', NOUS:u'nĩtũga', VOUS:u'nĩmũga', ILS:u'nĩmaga'},
    'ydy': {JE:u'nĩ', TU:u'nĩũ', ELLE:u'nĩa', IL:u'nĩa', NOUS:u'nĩtũ', VOUS:u'nĩmũ', ILS:u'nĩma'},
  }
}
endings['gikuyu'] = {
  'default': {
    'inf': u'a',
    'tdy': 'a',
    'tmw': u'a',
    'ydy': 're',
  }
}


#Kongo
starts['kongo'] = {
  'default': {
    'inf': 'ku',
    'tdy': 'ke', #{JE:'ke', TU:'ke', ELLE:'a', IL:'a', NOUS:'to', VOUS:'bo', ILS:'ba'},
    'ydy': '', #{JE:'na', TU:'o', ELLE:'a', IL:'a', NOUS:'to', VOUS:'bo', ILS:'ba'},
    'tmw': 'ta', #{JE:'n', TU:'oko', ELLE:'ako', IL:'ako', NOUS:'toko', VOUS:'boko', ILS:'bako'},
  }
}
endings['kongo'] = {
  'default': {
    'inf': u'a',
    'tdy': 'a',
    'tmw': u'a',
    'ydy': 'aka',
  }
}

# Oromo
starts['oromo'] = {
  'default': {
    'tdy': '',
    'ydy': '',
    'tmw': 'ni ',
  }
}
endings['oromo'] = {
  'default': {
    'tdy': {JE:'aan jiraa', TU:'aa jirtaa', ELLE:'aa jirtii', IL:'aa jiraa', NOUS:'aa jirraa', VOUS:'aa jirtuu', ILS:'aa jiranii', ELLES:'aa jiranii'},
    'ydy': 'ee',
    'tmw': {JE:'dhaa', TU:'ttaa', IL:'aa', ELLE:'tii', NOUS:'nnaa', VOUS:'tuu', ILS:'anii', ELLES:'anii'},
  }
}

# Lingala
starts['lingala'] = {
  'default': {
    'inf': 'ko',
    'tdy': {JE:'na', TU:'o', ELLE:'a', IL:'a', IT: 'e', NOUS:'to', VOUS:'bo', ILS:'ba'},
    'ydy': {JE:'na', TU:'o', ELLE:'a', IL:'a', NOUS:'to', VOUS:'bo', ILS:'ba'},
    'tmw': {JE:'nako', TU:'oko', ELLE:'ako', IL:'ako', NOUS:'toko', VOUS:'boko', ILS:'bako'},
  }
}
endings['lingala'] = {
  'default': {
    'inf': u'a',
    'tdy': 'i',
    'tmw': u'a',
    'ydy': 'aki',
  }
}

# Luganda
starts['luganda'] = {
  'default': {
    'inf': 'oku',
    'tdy': {JE:'n', TU:'o', ELLE:'a', IL:'a', NOUS:'tu', VOUS:'mu', ILS:'ba', ELLES:'ba'},
    'ydy': 'a',
    'tmw': {JE:'ndi', TU:'oli', ELLE:'ali', IL:'ali', NOUS:'tuli', VOUS:'muli', ILS:'bali', ELLES:'bali'},
  }
}
endings['luganda'] = {
  'default': {
    'inf': 'a',
    'tdy': 'a',
    'ydy': 'a',
    'tmw': u'a',
  }
}

# Luwo
starts['luwo'] = {
  'default': {
    'inf': '',
    'tdy': {JE:'a', TU:'i', ELLE:'o', IL:'o', NOUS:'wa', VOUS:'wu', ILS:'gi'},
    'ydy': {JE:'ne a', TU:'ne i', ELLE:'ne o', IL:'ne o', NOUS:'ne wa', VOUS:'ne u', ILS:'ne gi'},
    'tmw': {JE:'abiro ', TU:'ibiro ', ELLE:'obiro ', IL:'obiro ', NOUS:'wabiro ', VOUS:'ubiro ', ILS:'gibiro '},
  }
}

# Swahili
starts['swahili'] = {
  'ni': {
    'inf': '',
    'tdy': '',
  },
  'default': {
    'inf': 'ku',
    'tdy': {JE:'nina', TU:'una', ELLE:'ana', IL:'ana', NOUS:'tuna', VOUS:'mna', ILS:'wana'},
    'ydy': {JE:'nili', TU:'uli', ELLE:'ali', IL:'ali', NOUS:'tuli', VOUS:'mli', ILS:'wali'},
    'tmw': {JE:'nita', TU:'uta', ELLE:'ata', IL:'ata', NOUS:'tuta', VOUS:'mta', ILS:'wata'},
  }
}
endings['swahili'] = {
  'ni': {
    'inf': '',
    'tdy': '',
  },
  'default': {
    'inf': 'a',
    'tdy': 'a',
    'ydy': 'a',
    'tmw': 'a',
  }
}


# Yoruba
starts['yoruba'] = {
  'default': {
    'inf': 'lati ',
    'tdy': 'n',
    'tmw': u'maa',
  }
}
endings['yoruba'] = {
  'default': {
    'ydy': ' lana',
    'not': u'kọ',
  }
}

# Zulu
starts['zulu'] = {
  'ni': {
    'inf': '',
    'tdy': '',
  },
  'default': {
    'inf': 'uku',
    'tdy': {JE:'ngiya', TU:'uya', ELLE:'uya', IL:'uya', NOUS:'siya', VOUS:'niya', ILS:'baya'},
    'ydy': {JE:'ngi', TU:'ni', ELLE:'u', IL:'u', NOUS:'si', VOUS:'ni', ILS:'ba'},
    'tmw': {JE:'ngizo', TU:'uzo', ELLE:'uzo', IL:'uzo', NOUS:'sizo', VOUS:'nizo', ILS:'bazo'},
  }
}
endings['zulu'] = {
  'ni': {
    'inf': '',
    'tdy': '',
  },
  'default': {
    'inf': 'a',
    'tdy': 'a',
    'ydy': 'ile',
    'tmw': u'a',
  }
}

endings['french'] = {
  'er' : {
    'inf': 'er',
    'tdy' : {JE:'e', TU:'es', IL:'e', ELLE:'e', NOUS:'ons', VOUS:'ez', ILS:'ent', ELLES:'ent'},
    'tmw' : {JE:'erai', TU:'eras', IL:'era', ELLE:'era', NOUS:'erons', VOUS:'erez', ELLES:'eront', ILS:'eront'},
    'ydy' : {JE:'ais', TU:'ais', ELLE:'ait', IL:'ait', NOUS:'ions', VOUS:'iez', ELLES:'aient', ILS:'aient'},
    'conditional' : ['erais', 'erais', 'erait', 'erions', 'eriez', \
      'eraient'],
    'past participle' : u'é'
    },
  'ir' : {
    'inf': 'ir',
    'tdy' : {JE:'is', TU:'is', IL:'it', ELLE:'it', NOUS:'issons', VOUS:'issez', ILS:'issent', ELLES:'issent'},
    'tmw' : ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
    'ydy' : ['issais', 'issais', 'issait', 'issions', 'issiez', \
      'issaient'],
    'conditional' : ['irais', 'irais', 'irait', 'irions', 'iriez', \
      'iraient'],
    'past participle' : 'i'
    },
  're' : {
    'inf': 're',
    'tdy' : {JE:'s', TU:'s', IL:'', ELLE:'', NOUS:'ons', VOUS:'ez', ILS:'ent', ELLES:'ent'},
    'tmw' : {JE:'rai', TU:'ras', ELLE:'ra', NOUS:'rons', VOUS:'rez', ILS:'ront'},
    'ydy' : {JE:'ais', TU:'ais', ELLE:'ait', NOUS:'ions', VOUS:'iez', ILS:'aient'},
    'conditional' : ['rais', 'rais', 'rait', 'rions', 'riez', 'raient'],
    'past participle' : 'u'
    },
  }
  

irregular['french'] = {
  
  'aller' : {
    'tdy' : {JE:'vais', TU:'vas', IL:'va', ELLE:'va', NOUS:'allons', VOUS:'allez', ILS:'vont', ELLES:'vont'},
    'tmw' : ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
    'ydy' : ['allais', 'allais', 'allait', 'allions', 'alliez', \
      'allaient'],
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

  'être' : {
    'tdy' : ['suis', 'es', 'est', 'sommes', 'êtes', 'sont'],
    'tmw' : ['serai', 'seras', 'sera', 'serons', 'serez', 'seront'],
    'ydy' : ['étais', 'étais', 'était', 'étions', 'étiez', 'étaient'],
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
  
  }
  
irregular['lingala'] = {
  'koya': {
    'tdy': {JE:'naye', TU:'oye', ELLE:'aye', IL:'aye', NOUS:'toye', VOUS:'boye', ILS:'baye', ELLES:'baye'},
  }
}


def get_affix(language, tense, pronoun, pattern, affixes):
  affix = ''
  try:
    return affixes[language][pattern][tense][pronoun] 
  except (KeyError, IndexError, TypeError):
    pass

  try:
    return affixes[language][pattern][tense] 
  except (KeyError, IndexError, TypeError):
    pass

  try:
    return affixes[language]['default'][tense][pronoun] 
  except (KeyError, IndexError, TypeError):
    pass

  try:
    return affixes[language]['default'][tense] 
  except (KeyError, IndexError, TypeError):
    pass

  return affix

  
def get_prefix(language, tense, pronoun, pattern):
  try:
    starts[language] = models.data[language]['conjugate']['prefix']
  except KeyError:
    pass

  if language not in starts:
    starts[language] = {}
  return get_affix(language, tense, pronoun, pattern, starts)

def get_suffix(language, tense, pronoun, pattern):
  try:
    endings[language] = models.data[language]['conjugate']['suffix']
  except KeyError:
    pass
  return get_affix(language, tense, pronoun, pattern, endings)

def spelling_change_pre(language, pre, stem, ending):
  return pre

def spelling_change_stem(language, pre, stem, ending):
  return stem

def spelling_change_end(language, pre, stem, ending):
  if 'french' == language:
    if stem[-1] == 'g' and ending[0] in ('a', 'o'):
      ending = 'e' + ending
  return ending

def conjugate(language, verb, stem, pronoun, tense):
  pattern = verb[-2:]
  ending = get_suffix(language, tense, pronoun, pattern)
  pre = get_prefix(language, tense, pronoun, pattern)

  corrected_pre = spelling_change_pre(language, pre, stem, ending)
  corrected_stem = spelling_change_stem(language, pre, stem, ending)
  corrected_end = spelling_change_end(language, pre, stem, ending)

  return corrected_pre + corrected_stem + corrected_end


class VerbGenerator:
  """Generators for Verbs."""
  TENSES = {
  'oromo': {
    'VERB1PS_TDY': 'ani VERBaa jiraa',
    'VERB2PS_TDY': 'ati VERBaa jirtaa',
    'VERB3PS_TDY_F': 'isheen VERBaa jirtii',
    'VERB3PS_TDY_M': 'inni VERBaa jiraa',
    'VERB1PP_TDY': 'nuti VERBaa jiraa',
    'VERB2PP_TDY': 'isini VERBaa jirtuu',
    'VERB3PP_TDY': 'isaani VERBaa jiranii',

    'VERB1PS_YDY': 'ani VERBdhee',
    'VERB2PS_YDY': 'ati VERBttee',
    'VERB3PS_YDY_F': 'isheen VERBttee',
    'VERB3PS_YDY_M': 'inni VERBtee',
    'VERB1PP_YDY': 'nuti VERBnee',
    'VERB2PP_YDY': 'isini VERBttanii',
    'VERB3PP_YDY': 'isaani VERBtanii',

    'VERB1PS_TMW': 'ani ni VERBdhaa',
    'VERB2PS_TMW': 'ati ni VERBttaa',
    'VERB3PS_TMW_F': 'isheen ni VERBttii',
    'VERB3PS_TMW_M': 'inni ni VERBtaa',
    'VERB1PP_TMW': 'nuti ni VERBnnaa',
    'VERB2PP_TMW': 'isini ni VERBttuu',
    'VERB3PP_TMW': 'isaani ni VERBtanii',
  },
}
  def __init__(self, language):
    self.language = language

  def getLanguageTenses(self):
    if self.language in self.TENSES:
      return self.TENSES[self.language]
    else:
      return {}

  def getConjugation(self, verb, person=1, tense='tdy'):
    tense = tense.lower()
    tokens = verb.split(' ')
    if len(tokens) > 1 and self.language == 'akan':
      verb = tokens[0]
      rest = tokens[1:]
    else:
      rest = []

    cjn = conjugate(self.language, verb, self.stem(verb), person, tense)
    return ' '.join([cjn] + rest)

  def stem(self, word):
    stemmed = word
    AFFIX = {
      'chewa': {'pre':'ku', 'end': 'a'},
      'english': {'pre':'to ', 'end': ''},
      'german': {'pre':'', 'end': 'en'},
      'gikuyu': {'pre': u'gũ', 'end': 'a'},
      'kongo': {'pre':'ku ', 'end': 'a'},
      'luganda': {'pre':'oku', 'end': 'a'},
      'malagasy': {'pre':'m', 'end': ''},
      'spanish': {'pre': '', 'end': 'ar'},
      'zulu': {'pre':'uku', 'end': 'a'},
    }
    if self.language in ('shona', 'swahili', 'ururimi'):
      if len(stemmed) > 4 and stemmed.startswith('ku'):
        stemmed = word[2:]
      if stemmed.endswith('a'):
        stemmed = stemmed[:-1]
    elif self.language in ('lingala'):
      if len(stemmed) > 4 and stemmed.startswith('ko'):
        stemmed = word[2:]
      if stemmed.endswith('a'):
        stemmed = stemmed[:-1]
    elif self.language in ('oromo'):
      if word.endswith('uu'):
        stemmed = word[:-2]
    elif self.language in ('french'):
      stemmed = word[:-2]
    elif self.language in AFFIX:
      prefix = AFFIX[self.language]['pre'] if 'pre' in AFFIX[self.language] else ''
      suffix = AFFIX[self.language]['end'] if 'end' in AFFIX[self.language] else ''
      if len(stemmed) > 4 and stemmed.startswith(prefix):
        stemmed = word[len(prefix):]
      if len(suffix) and stemmed.endswith(suffix):
        stemmed = stemmed[:-len(suffix)]

    return stemmed
