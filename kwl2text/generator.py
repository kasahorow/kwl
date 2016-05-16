# coding: utf-8

import libconjugate as lib
import l10n
import logging

class Token:
  def __init__(self, fragment, l10n, pos):
    self.l10n = l10n
    self.fragment = fragment
    self.pos = pos

  def __str__(self):
    return u'TOKEN(%s:%s)' % (self.pos, self.fragment)

class Generator:
  """Generate a sentence in a target language from a KWL AST parse tree."""
  
  def __init__(self, kasa, language, grammar, ast={}, lexicon={}):
    self.ast = ast
    self.kasa = kasa
    self.language = language
    self.grammar = grammar
    self.object = ''  # Default.
    self.operators = []  # Empty stack
    self.person = self.grammar.ELLE  # Default pronoun person
    self.stype = ast['v'][0]['t']  # Default.
    self.subject = '' # Default.
    self.lexicon = lexicon
    self.tense = 'inf'  # Infinitive tense by default
    self.token = 1
    self.tokens = {}
    self.verb = ''  # Default.
    self.story = []
   
  def getOps(self):
    return {
      ':': self.colon_fn,
      ',': self.comma_fn,
      'a_p': self.adj_nom_fn,
      'act': self.verb_fn,
      'act_adv': self.act_p_adv_p_fn,
      'adj': self.adjective_fn,
      'adj_adj_nom': self.adj_nom_fn,
      'adj_nom': self.adj_nom_fn,
      'adj_nom_nom': self.adj_nom_fn,
      'adj_nom_plural': self.adj_nom_fn,
      'adj_sci': self.adj_nom_fn,
      'adv': self.adverb_fn, # adverb
      'and': self.and_fn,
      'at': self.at_fn,
      'd_p': self.det_nom_fn,
      'det_nom': self.det_nom_fn,
      'det_adj_nom': self.adj_nom_fn,
      'default': self.default_fn,  # default operator
      'defn': self.defn_fn,
      'det': self.determiner_fn,
      'done_tdy': self.perfect_present_fn,
      'done_tmw': self.perfect_future_fn,
      'done_ydy': self.perfect_past_fn,
      'elle': self.conjugate_elle_fn,
      'elles': self.conjugate_elles_fn,
      'exc': self.exclamation_fn,
      'f': self.conjugate_elle_fn,
      'headline': self.title_fn,
      'i': self.conjugate_it_fn,
      'il': self.conjugate_il_fn,
      'ils': self.conjugate_ils_fn,
      'in': self.in_p_fn,
      'inf': self.infinitive_fn,
      'je': self.conjugate_je_fn,
      'kg': self.environment_fn,
      'like': self.like_fn,
      'third': self.object_fn,
      'm': self.conjugate_il_fn,
      'may': self.tense_may_fn,
      'n_p': self.n_p_fn,
      'nom': self.nom_fn,
      'nom_nom': self.n_p_fn,
      'not_tdy': self.not_tdy_fn,
      'now_tdy': self.continuous_present_fn,
      'now_tmw': self.continuous_future_fn,
      'now_ydy': self.continuous_past_fn,
      'nous': self.conjugate_nous_fn,
      'of': self.of_fn,
      'or': self.or_fn,
      'p_p': self.p_p_fn,
      'plural': self.plural_fn,
      'pos': self.possessive_fn,  # Possessive pronouns
      'pos_nom': self.pos_nom_fn,
      'pre': self.preposition_fn,
      'pro': self.pronoun_fn,
      'pro_nom': self.pro_nom_fn,
      'quote': self.quote_fn,
      'subject': self.subject_fn,
      's_v': self.subject_verb_fn,
      's_v_o': self.subject_verb_object_fn,
      'sample': self.sample_fn,
      'sci': self.sci_fn,
      'so': self.so_fn,
      'story': self.story_fn,
      'tdy': self.today_fn,
      'then': self.ifthen_fn,
      'title': self.title_fn,
      'tmw': self.tomorrow_fn,
      'to': self.to_fn,
      'tu': self.conjugate_tu_fn,
      'verb': self.action_fn,
      'vous': self.conjugate_vous_fn,
      'when': self.when_fn,
      'ydy': self.yesterday_fn,
    }

  def capfirst_fn(self, surface):
   return surface[0].upper() + surface[1:]

  def generate(self):
    """Generate the sentence for human consumption."""
    surface = self.getHumanFromAST(self.ast)  # Process the AST
    surface = self.single_spacing(surface)
    surface = self.make_substitutions(' ' + surface)  #  make interior text, e,g, " a animal" => " an animal"
    surface = self.format_sentence(surface, self.stype)
    surface = self.make_substitutions(surface, 'punctuation')  # e.g. replace in Amarinya
    surface = self.single_spacing(surface)
    return surface.strip()

  def make_substitutions(self, surface, key='subs'):
    if self.grammar.data.has_key(key):
      for k,v in list(self.grammar.data[key]) + [(' , ', ', '), (' : ', ': ')]:
        surface = find_and_replace(k, v, surface)
    return surface.strip()

  def generate_sentence(self):
    if '...' in self.verb:
      self.verb = self.verb.replace('...', self.object)
      self.object = ''
    elif '~' in self.verb:
      self.verb = self.verb.replace('~', self.object)
      self.object = ''

    human = self.reorder_triple((self.subject, self.verb, self.object), self.stype)
    surface = ' '.join([x if x else '' for x in human])

    # Reset subject, verb, and object
    self.setSubject('')
    self.setObject('')
    self.setVerb('')
    
    return surface
  
  def format_sentence(self, surface, stype):
    new_surface = surface
    if stype == 'question':
      new_surface = self.question_fn(surface)
    elif stype == 'statement':
      new_surface = self.statement_fn(surface)
    elif stype == 'command':
      new_surface = self.command_fn(surface)
    return new_surface

  def single_spacing(self, surface):
    "Replace more than one space between words with a single space."
    if '  ' in surface:
      return self.single_spacing(surface.replace('  ', ' '))
    else:
      return self.punctuation_spacing(surface)

  def punctuation_spacing(self, surface):
    for punc in [',', ]:
      surface = surface.replace(' %s' % punc, punc)
    return surface

  def action_fn(self, surface):
    self.setVerb(surface)
    return surface

  def addToken(self, token_obj):
    self.tokens['arg%s' % self.token] = token_obj
    self.token = self.token + 1

  def expand(self, args_dict):
    if 'nom' in args_dict:
      return self.noun_fn(*args_dict['nom'])
    elif 'defn' in args_dict:
      return self.defn_fn(args_dict['defn']['word'], args_dict['defn']['pos'])

  def tuple_fn(self, surface, ttype):
    parts = surface.split('<kwb>')
    if len(parts) == 2:  # Reorder by language
      new_parts = self.reorder_tuple(parts, ttype)
      new_parts.insert(1, self.alliterate(parts[1]))
    else:
      new_parts = parts
    new_surface = ' '.join(new_parts)
    return new_surface

  def adj_nom_fn(self, surface):
    return self.tuple_fn(surface, 'adj_nom')

  def det_nom_fn(self, surface):
    return self.tuple_fn(surface, 'det_nom')

  def alliterate(self, surface):
    try:
      prefix = self.grammar.data['alliterate']['prefix'][surface[0:1]]
    except Exception, e:
      prefix = ' '
    return prefix

  def colon_fn(self, surface):
    human = ': '.join(surface.split('<kwb>'))
    return human

  def comma_fn(self, surface):
    human = ', '.join(surface.split('<kwb>'))
    return human

  def command_fn(self, surface):
    return u'%s!' % self.capfirst_fn(surface)

  def conjugate(self, surface, person, tense):
    self.person = person
    #v = lib.VerbGenerator(self.language)
    v = lib.VerbGenerator(self.grammar)
    try:
      cjn = v.getConjugation(surface, person, tense).replace('VERB', surface)
    except ValueError, e:
      cjn = u'CONJUGATION FAIL: %s with error: %s' % (surface, e)
    return cjn

  def not_tdy_fn(self, surface):
    self.tense = 'not_tdy'
    return self.conjugate(surface, self.person, self.tense)

  def conjugate_je_fn(self, surface):
    self.person = self.grammar.JE
    return surface

  def conjugate_tu_fn(self, surface):
    self.person = self.grammar.TU
    return surface

  def conjugate_il_fn(self, surface):
    self.person = self.grammar.IL
    return surface

  def conjugate_it_fn(self, surface):
    self.person = self.grammar.IT
    return surface

  def conjugate_elle_fn(self, surface):
    self.person = self.grammar.ELLE
    return surface

  def conjugate_nous_fn(self, surface):
    self.person = self.grammar.NOUS
    return surface

  def conjugate_vous_fn(self, surface):
    self.person = self.grammar.VOUS
    return surface
  
  def conjugate_ils_fn(self, surface):
    self.person = self.grammar.ILS
    return surface

  def conjugate_elles_fn(self, surface):
    self.person = self.grammar.ELLES
    return surface

  def default_fn(self, surface, pos=None):
    parts = surface.split('<kwb>')
    parts_len = len(parts)
    if parts_len == 3:
      human = self.subject_verb_object_fn(surface)
    elif parts_len == 2:
      new_parts = self.reorder_tuple(parts, pos)
      human = ' '.join(new_parts)
    else:
      human = ' '.join(surface.split('<kwb>'))
    return human

  def defn_fn(self, word):
    if self.tokens:
      token = self.tokens['arg1']
      key = self.get_key([token.fragment, token.pos, 'defn'])  
      return self.translate(key)
    else:
      logging.warn('No defn found for %s' % word)
      return ''

  def exclamation_fn(self, surface):
    key = self.get_key([surface, 'exclamation'])
    out = self.translate(key)
    return u'%s' % out

  def environment_fn(self, surface):
    """Read the environment value and substitute it."""
    try:
      kg = getattr(self, surface)
    except KeyError, e:
      logging.warn('Cannot get environment variable with value: %s (%s)' % (surface, e)) 
      kg = 'kg:%s' % surface
    return kg

  def infinitive_fn(self, surface):
    self.tense = 'inf'
    return self.conjugate(surface, self.person, self.tense)

  
  def pro_nom_fn(self, surface):
    return self.n_p_fn(surface, 'pro_nom')

  def pos_nom_fn(self, surface):
    return self.n_p_fn(surface, 'pos_nom')

  def continuous_present_fn(self, surface):
    self.tense = 'now_tdy'
    return self.conjugate(surface, self.person, self.tense)

  def continuous_future_fn(self, surface):
    self.tense = 'now_tmw'
    return self.conjugate(surface, self.person, self.tense)

  def continuous_past_fn(self, surface):
    self.tense = 'now_ydy'
    return self.conjugate(surface, self.person, self.tense)

  def object_fn(self, surface):
    self.setObject(surface)
    return surface

  def n_p_fn(self, surface, ptype='n_p'):
    JSTR = {
      'akan': ' ',
      'english': ' ',
      'lingala': self.alliterate(surface),
      'swahili': ' ya ',
      'default': ' ',
    }
    sep = JSTR[self.language if self.language in JSTR else 'default']
    parts = surface.split('<kwb>')
    
    if len(parts) == 2:  # Reorder by language
      new_parts = self.reorder_tuple(parts, ptype)
    else:
      new_parts = parts
   
    human = sep.join(new_parts)
    return human
    
  def p_p_fn(self, surface):
    "Prepositional phrase."
    ORDER = {
      'default': (0, 1), 
    }
    words = surface.split('<kwb>')
    if len(words) == 1:
      return surface
    elif len(words) == 2:
      human = []
      order = ORDER[self.language if self.language in ORDER else 'default']
      for pos in order:
        human.append(words[pos])
      return ' '.join(human)

  def perfect_future_fn(self, surface):
    self.tense = 'done_tmw'
    return self.conjugate(surface, self.person, self.tense)

  def perfect_past_fn(self, surface):
    self.tense = 'done_ydy'
    return self.conjugate(surface, self.person, self.tense)

  def perfect_present_fn(self, surface):
    self.tense = 'done_tdy'
    return self.conjugate(surface, self.person, self.tense)

  def plural_fn(self, surface):
    #return l10n.plural(self.language, surface)
    return l10n.plural(self.grammar, surface)

  def question_fn(self, surface):
    return u'%s? ' % self.capfirst_fn(surface)

  def quote_fn(self, surface):
    return u'"%s"' % surface

  def sample_fn(self, word):
    if self.tokens:
      token = self.tokens['arg1']
      key = self.get_key([token.fragment, token.pos, 'sample'])  
      return self.translate(key)
    else:
      logging.warn('No example found for %s' % word)
      return ''

  def statement_fn(self, surface):
    return u'%s.' % self.capfirst_fn(surface)

  def story_fn(self, surface):
    phrases = surface.split('<kwb>')
    sentence = ' '.join(phrases)
    self.story.append(sentence)
    return sentence

  def subject_fn(self, surface):
    self.setSubject(surface)
    return surface

  def two_part_fn(self, ast, parts):
    sentence = ast.split('<kwb>')
    if parts[0][-5:] in ('v_p', 'tdy_p', 'ydy_p', 'tmw_p'):  # verb, object
      self.setSubject('')
      self.setObject(sentence[1])
      self.setVerb(sentence[0])
    else: # subject, verb
      self.setSubject(sentence[0])
      self.setObject('')
      self.setVerb(sentence[1])
    return self.generate_sentence()
  
  def subject_verb_fn(self, surface):
    sentence = surface.split('<kwb>')
    return self.generate_sentence()

  def subject_verb_object_fn(self, surface):
    sentence = surface.split('<kwb>')
    # NB: Object must be set before the verb so '...' substitution can happen
    self.setSubject(sentence[0])
    self.setObject(sentence[2])
    self.setVerb(sentence[1])
    return self.generate_sentence()

  def tense_may_fn(self, surface):
    self.tense = 'may'
    return self.conjugate(surface, self.person, self.tense)
 
  def title_fn(self, surface):
    if len(surface) > 1:
      return surface.title()
    else:
      return surface

  def today_fn(self, surface):
    self.tense = 'tdy'
    return self.conjugate(surface, self.person, self.tense)

  def tomorrow_fn(self, surface):
    self.tense = 'tmw'
    return self.conjugate(surface, self.person, self.tense)

  def act_p_adv_p_fn(self, surface):
    words = surface.split('<kwb>')
    reordered = self.reorder_tuple(words, 'act_adv')
    return ' '.join(reordered)

  def act_p_nom_p_fn(self, surface):
    sentence = surface.split('<kwb>')
    #self.person = self.grammar.TU
    #pronoun = pronouns_to_inglish(self.person)
    #self.subject = self.pronoun_fn(pronoun)     
    self.object = sentence[1]
    self.setVerb(sentence[0])
    return self.generate_sentence()

  def yesterday_fn(self, surface):
    self.tense = 'ydy'
    return self.conjugate(surface, self.person, self.tense)

  def nom_fn(self, noun):
    return self.noun_fn(noun, pos='noun')

  def sci_fn(self, noun):
    return self.noun_fn(noun, pos='science')

  def noun_fn(self, noun, number=1, pos='noun', nclass=None):
    if self.language in ('english', 'inglish'):
      if number == 1:
        human = noun
      else:
        human = l10n.plural('english', noun)
    else:
      singular = self.translate(self.get_key([noun, pos]))
      if number == 1:
        human = singular if '-noun' not in singular else u'[%s]' % noun
      else:
        human = l10n.plural(self.language, noun, number)

    self.addToken(Token(noun, human, pos))
    return human

  def possessive_fn(self, pronoun, nclass=None, view='subject'):
    """Possessive pronouns."""
    return self.lookup(pronoun, 'possessive')

  def pronoun_fn(self, pronoun, nclass=None, view='subject'):
    return self.lookup(pronoun, 'pronoun')

  def lookup(self, word, pos, number=1, nclass=None):
    if self.language in ('english', 'inglish'):
      singular = word # English is the default incoming language
    else:
      singular = self.translate(self.get_key([word, pos]))
    if number == 1:  
      try:
        human = '%s' % int(word)
      except ValueError, e:
        human = singular if '-%s' % pos not in singular else  u'[%s]' % word
      else:
        human = l10n.plural(self.language, singular, number)

    self.addToken(Token(word, human, pos))
    return human

  def adjective_fn(self, adjective, number=1, nclass=None):
    if self.language in ('english', 'inglish'):
      human = adjective # English adjectives don't have plurals
    else:
      singular = self.translate(self.get_key([adjective, 'adjective']))
      if number == 1:
        try:
          human = '%s' % int(adjective)

        except ValueError, e:
          human = singular if '-adjective' not in singular else  u'[%s]' % adjective
  
      else:
        human = l10n.plural(self.language, singular, number)

    self.addToken(Token(adjective, human, 'adjective'))
    return human

  def adverb_fn(self, adverb):
    return self.lookup(adverb, 'adverb')

  def determiner_fn(self, determiner, number=1, nclass=None):
    human = determiner
    if self.language != 'english':
      human = self.translate(self.get_key([determiner, 'determiner']))
    self.addToken(Token(determiner, human, 'determiner'))
    return human

  def in_p_fn(self, surface):
    new_surface = u'%s<kwb>%s' % (self.preposition_fn('in'), surface)
    return self.tuple_fn(new_surface, "in_p")

  def preposition_fn(self, prep):
    human = prep
    if self.language != 'english':
      human = self.translate(self.get_key([prep, 'preposition']))
    return human

  def verb_fn(self, verb, person=1, number=1, nclass='positive', tense='present'):
    if self.language in ('englis', 'inglis'):
      human = verb # English adjectives don't have plurals
    else:
      human = self.translate(self.get_key([verb, 'verb']))
    self.addToken(Token(verb, human, 'verb'))
    return human

  def sentence_fn(self, noun_phrase, verb_phrase):
    return self.model.sentence_fn(noun_phrase, verb_phrase)


  def and_fn(self, surface):
    sep = self.translate(self.get_key(['and', 'conjunction']))
    combine = u' %s ' % sep
    subject = self.single_spacing(combine.join(surface.split('<kwb>')))
    self.setSubject(subject)
    return subject

  def ifthen_fn(self, surface):
    parts = surface.split('<kwb>')
    sep = 'if ... then'
    if self.language!='english':
      sep = self.translate(self.get_key([sep, 'conjunction']))
    
    if len(parts) < 2:
      subject = surface
    else:
      human = sep.replace('...', parts[0])
      human = human + u' ' + ' '.join(parts[1:])
      subject = self.single_spacing(human)
    self.setSubject(subject)
    return subject
    
  def like_fn(self, surface):
    """Represent like(X). """
    new_surface = u'%s<kwb>%s' % (self.preposition_fn('like'), surface)
    return self.tuple_fn(new_surface, "in_p")

  def of_fn(self, surface):
    """Join two noun phrases with the preposition 'of'. """
    words = surface.split('<kwb>')
    order = self.reorder_tuple(words, 'of_p')  # 'of' reverses noun phrases in Inglish
    sep = self.translate(self.get_key(['of', 'preposition']))
    combine = u' %s ' % sep
    if len(words) == 1:
      subject = surface
    elif len(words) == 2:
      human = []
      for word in order:
        human.append(word)
      subject = self.single_spacing(combine.join(human))
    self.setSubject(subject)
    return subject


  def or_fn(self, surface):
    sep = 'or'
    if self.language!='english':
      sep = self.translate(self.get_key([sep, 'conjunction']))
    combine = u' %s ' % sep
    subject = self.single_spacing(combine.join(surface.split('<kwb>')))
    self.setSubject(subject)
    return subject

  def at_fn(self, surface):
    """Represent at(X). """
    new_surface = u'%s<kwb>%s' % (self.preposition_fn('at'), surface)
    return self.tuple_fn(new_surface, "in_p")

  def to_fn(self, surface):
    """Represent to(X). """
    new_surface = u'%s<kwb>%s' % (self.preposition_fn('to'), surface)
    return self.tuple_fn(new_surface, "in_p")

  def reorder_tuple(self, pair, ptype='n_p'):
    "Reorder this word pair into a human readable format for this language."
    human = []
    try:
      order = self.grammar.data['order'][self.stype][ptype]
    except (KeyError, TypeError), e:
      #logging.warn('%s order not set for %s: using default value' % (self.language, ptype))
      try:
        order = self.grammar.data['order'][ptype]
      except KeyError, e:
        order = self.grammar.data['order']['default']

    if '...' in pair[0]:
      human = [pair[0].replace('...', pair[1]), '']
    elif '...' in pair[1]:
      human = ['', pair[1].replace('...', pair[0])]
    else:
      for pos in order:
        human.append(pair[pos])

    return human

  def reorder_triple(self, triple, ptype='statement'):
    "Reorder this word triple into a human readable format for this language."
    human = []
    if 'english' == self.language:
      if triple[0] == 'who' and ptype == 'question':
        ptype = 'who_subject_question'  # use a different triple order
      elif triple[2] == 'who' and ptype == 'question':
        ptype = 'who_object_question'  # use a different triple order

    try:
      order = self.grammar.data['order_triple'][ptype]
    except KeyError, e:
      #logging.warn('%s "order_triple" not set for %s: using default value' % (self.language, ptype))
      order = self.grammar.data['order_triple']['default']

    for pos in order:
      human.append(triple[pos])

    return human

  def so_fn(self, surface):
    sep = self.translate(self.get_key(['so', 'conjunction']))
    combine = u' %s ' % sep
    subject = self.single_spacing(combine.join(surface.split('<kwb>')))
    self.setSubject(subject)
    return subject

  def when_fn(self, surface):
    parts = surface.split('<kwb>')
    sep = 'when'
    if self.language!='english':
      sep = self.translate(self.get_key([sep, 'conjunction']))

    if len(parts) < 2:
      subject = surface
    else:
      human = parts[0] + u' ' + sep + u' ' + ' '.join(parts[1:])
      subject = self.single_spacing(human)
    self.setSubject(subject)
    return subject

  def getSentenceTypes(self):
    return ['command', 'question', 'statement']

  def getSentenceType(self):
    return self.stype

  def setAst(self, ast):
    self.ast = ast

  def setSentenceType(self, stype):
    if stype in self.getSentenceTypes():
      self.stype = stype
      if stype == 'command':
        self.tense = 'cmd'  # Change the default part of speech for command
    else:
      self.stype = 'statement'  # default sentence type

  def getObject(self):
    return self.object

  def setObject(self, surface):
    self.object = surface

  def getPartOfSpeech(self, pos):
    POS = {
      'object': self.object,
      'subject': self.subject,
      'verb': self.verb,
    }
    return POS[pos] if pos in POS else ('<%s not implemented>' % pos)

  def getSubject(self):
    return self.subject

  def setSubject(self, ast):
    self.subject = ast

  def getVerb(self):
    return self.verb

  def setVerb(self, surface):
    self.verb = surface

  def get_date_format(self):
    if self.kasa == 'ak':
      return 'MM da DD, afe YYYY'
    elif self.kasa == 'ge':
      return 'MM gbii DD, YYYY'
    elif self.kasa == 'ha':
      return 'DD ga MM, YYYY'
    elif self.kasa == 'sw':
      return 'Tarehe DD MM mwaka wa YYYY'
    else:
      return 'MM DD, YYYY'

  def get_en_date(self, number_str, cat):
    month_map = {
      '01': 'January',
      '02': 'February',
      '03': 'March',
      '04': 'April',
      '05': 'May',
      '06': 'June',
      '07': 'July',
      '08': 'August',
      '09': 'September',
      '10': 'October',
      '11': 'November',
      '12': 'December',
    }
    day_map = {
      '1': 'Sunday',
      '2': 'Monday',
      '3': 'Tuesday',
      '4': 'Wednesday',
      '5': 'Thursday',
      '6': 'Friday',
      '7': 'Saturday'
    }
    if cat == 'month':
      return month_map[number_str] if number_str in month_map else number_str
    if cat == 'day':
      return day_map[number_str] if number_str in day_map else number_str

  def date_t(self, date_str):
    from datetime import datetime
    fdate = ''
    fmt = self.get_date_format()
    year, month, day = date_str.split('-')
    month_name = self.get_en_date(month.zfill(2), 'month')
    date = fmt.replace('YYYY', str(year))
    date = date.replace('MM', self.translate(self.get_key([month_name, 'noun']))) if month else ''
    date = date.replace('DD', str(day) if day else '')
    try:
      weekday = 1 + ((1 + datetime(int(year), int(month), int(day)).weekday()) % 7)
      day_name = self.get_en_date('%s' % weekday, 'day')
      date_l10n = self.translate(self.get_key([day_name, 'noun']))
      weekday = '' if date_l10n == weekday else '%s.' % date_l10n
    except Exception, e:  # TODO: handle the exceptions properly
      logging.info('Date l10n error (weekday): %s' % e)
      weekday = ''

    try:
      fdate = weekday + ' ' + date
    except Exception, e:
      logging.info('Date l10n error (full date): %s' % e)
      fdate = '%s-%s-%s' % (year, month, day)
    return fdate

  def getHumanFromAST(self, ast):
    "Convert AST into string for human consumption."
    _l10n = '' 
    operators = self.getOps()

    if not ast:
      _l10n = ''
    elif 't' in ast and 'v' in ast:  # AST is a dictionary
      self.operators.append(ast['t'])
      if ast['t'] in ('alpha', 'number', 'raw'):  # tokens
        _l10n = ast['v']
      elif ast['t'] == 'date':
        _l10n = self.date_t(ast['v'])
      else:
        try:
          _l10n = operators[ast['t']](self.getHumanFromAST(ast['v']))
        except KeyError:
          _l10n = operators['default'](self.getHumanFromAST(ast['v']), ast['t'])
    elif type([]) == type(ast):  # AST is a list of values
      human = []
      for x in ast:
        self.operators.append(x['t'])
        if x['t'] == 'raw':
          human.append(x['v'])
        elif x['t'] == 'date':
          human.append(self.date_t(x['v']))
        else:
          try:
            human.append(operators[x['t']](self.getHumanFromAST(x['v'])))
          except KeyError:
            human.append(operators['default'](self.getHumanFromAST(x['v']), x['t']))
          parts = x['t']
 
      _l10n = '<kwb>'.join(human)  # Use a special delimiter so can split into components again
    else:
      raise ValueError('AST should be either a list or a dictionary with "t" and "v" keys: %s' % ast)
    return _l10n.strip() if _l10n else ''

  def translate(self, lexicon_key):
    TM = self.lexicon
    human_text = ' '.join(lexicon_key.split('-')[0:-1])
    translated_text = human_text
    if lexicon_key and str(lexicon_key) in TM.keys():  # keys are always English ASCII
      translated_text = TM[lexicon_key]
    else:
      translated_text = u'[%s]' % human_text
    return translated_text

  def get_key(self, fragments):
    key = '-'.join([x for x  in fragments])
    return key.replace('#', ' ')

def find_and_replace(find, replace, data):
 return data.replace(find, replace)

def getConjugation(self, verb, person=1, tense='tdy'):
    tense = tense.lower()
    tokens = verb.split(' ')
    if len(tokens) > 1 and self.language == 'akan':
      verb = tokens[0]
      rest = tokens[1:]
    else:
      rest = []

    cjn = lib.conjugate(self.language, verb, self.stem(verb), person, tense)
    return ' '.join([cjn] + rest)
