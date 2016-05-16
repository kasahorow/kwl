# coding: utf-8

import logging
import sys
import os
import text2kwl as t2k

import semantics as s

DEBUG = True

def get_kwl_map():
  kwl_map = {
    'adjective': 'adj:...',
    'conjunction': '...',
    'determiner': 'det:...',
    'noun': 'nom:...',
    'noun plural': 'plural(nom:...)',
    'possessive': 'pos:...',
    'preposition': 'pre:...', 
    'pronoun': 'pro:...',
    'verb': 'act:...',
    'verb je tdy': 'tdy(je(act:...))',
    'verb je ydy': 'ydy(je(act:...))',
    'verb je tmw': 'tmw(je(act:...))',
    'verb tu tdy': 'tdy(tu(act:...))',
    'verb f tdy': 'tdy(f(act:...))',
    'verb m tdy': 'tdy(m(act:...))',
  }
  return kwl_map

def convert_to_kwl_tag(pos):
  kwl_map = get_kwl_map()
  return kwl_map[pos]

def tag_pos(word, source, separator):
  poss = get_kwl_map().keys()
  tags = []
  try:
    number = int(word)
  except ValueError:
    number = None
  
  for pos in poss:
    if '%s%s%s' % (word, separator, pos) in source:
      if ' ' in pos:  # A complex part of speech
        word = source['%s-%s' % (word, pos)]
      tags.append(convert_to_kwl_tag(pos))
    elif '%s%s%s' % (word.lower(), separator, pos) in source:
      tags.append(convert_to_kwl_tag(pos))
    elif number:
      tags.append('adj:...')

  if len(tags):
    if len(word) == 1 or word == word.lower():
      return tags[0].replace('...', word)  # pick the first match
    else:
      return 'title(%s)' % tags[0].replace('...', word)  # pick the first match
  
  return 'raw(%s)' % word if word else ''

def text_to_kwl(text, translation_dictionary={}, separator='-'):
  tagged = []
  tokens = text.strip().split(' ')
  for token in tokens:
    tagged.append(tag_pos(token, translation_dictionary, separator))

  logging.info(tagged)
  psr = t2k.text2kwlParser()
  sem = s.Semantics()
  w = psr.parse(' '.join(tagged), rule_name='sentence', semantics=sem,
                parseinfo=True)
  return w

