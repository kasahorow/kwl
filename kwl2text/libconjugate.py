# -*- coding: utf-8 -*- 

"""Conjugate verbs"""

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

  
def spelling_change_pre(language, pre, stem, ending):
  return pre

def spelling_change_stem(language, pre, stem, ending):
  return stem

def spelling_change_end(language, pre, stem, ending):
  if 'french' == language:
    if stem[-1] == 'g' and ending[0] in ('a', 'o'):
      ending = 'e' + ending
  return ending


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
  def __init__(self, grammar):
    self.grammar = grammar
    self.language = grammar.language

  def getLanguageTenses(self):
    if self.language in self.TENSES:
      return self.TENSES[self.language]
    else:
      return {}

  def conjugate(self, verb, stem, pronoun, tense):
    try:  # For irregular verbs, return immediately
      data = {self.language: {verb: self.grammar.data['conjugate'][verb]}}
      return get_affix(self.language, tense, pronoun, verb, data)
    except KeyError, e:
      pass # Use prefix/suffix data next

    pattern = verb[-2:]
    ending = self.get_suffix(tense, pronoun, pattern)
    pre = self.get_prefix(tense, pronoun, pattern)

    corrected_pre = spelling_change_pre(self.language, pre, stem, ending)
    corrected_stem = spelling_change_stem(self.language, pre, stem, ending)
    corrected_end = spelling_change_end(self.language, pre, stem, ending)

    return corrected_pre + corrected_stem + corrected_end

  def get_prefix(self, tense, pronoun, pattern):
    starts = {}
    try:
      starts[self.language] = self.grammar.data['conjugate']['prefix']
    except KeyError:
      pass

    return get_affix(self.language, tense, pronoun, pattern, starts)

  def get_suffix(self, tense, pronoun, pattern):
    endings = {}
    try:
      endings[self.language] = self.grammar.data['conjugate']['suffix']
    except KeyError:
      pass

    return get_affix(self.language, tense, pronoun, pattern, endings)

  def getConjugation(self, verb, person=1, tense='tdy'):
    tense = tense.lower()
    tokens = verb.split(' ')
    if len(tokens) > 1 and self.language == 'akan':
      verb = tokens[0]
      rest = tokens[1:]
    else:
      rest = []

    cjn = self.conjugate(verb, self.stem(verb), person, tense)
    return ' '.join([cjn] + rest)

  def stem(self, word):
    stemmed = word
    AFFIX = {
      'amarinya': {'prefix': u'መ', 'suffix': ''},
      'chewa': {'prefix':'ku', 'suffix': 'a'},
      'english': {'prefix':'to ', 'suffix': ''},
      'deutsch': {'prefix':'', 'suffix': 'en'},
      'gikuyu': {'prefix': u'gũ', 'suffix': 'a'},
      'kongo': {'prefix':'ku ', 'suffix': 'a'},
      'luganda': {'prefix':'oku', 'suffix': 'a'},
      'malagasy': {'prefix':'m', 'suffix': ''},
      'espanyol': {'prefix': '', 'suffix': 'ar'},
      'zulu': {'prefix':'uku', 'suffix': 'a'},
    }
    try:
      AFFIX[self.language] = self.grammar.data['stem']
    except KeyError:
      pass

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
    elif self.language in ('oromoo'):
      if word.endswith('uu'):
        stemmed = word[:-2]
    elif self.language in ('french'):
      stemmed = word[:-2]
    elif self.language in AFFIX:
      prefix = AFFIX[self.language]['prefix'] if 'prefix' in AFFIX[self.language] else ''
      suffix = AFFIX[self.language]['suffix'] if 'suffix' in AFFIX[self.language] else ''
      if len(stemmed) > 4 and stemmed.startswith(prefix):
        stemmed = word[len(prefix):]
      if len(suffix) and stemmed.endswith(suffix):
        stemmed = stemmed[:-len(suffix)]

    return stemmed
