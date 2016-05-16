# coding: utf-8
"""A standalone KWL interpretor."""

from kwl2text import kwl2text
from kwl2text.generator import Generator
import kwl2text.semantics as semantics
import kasahorow as k
import data
import logging
import re
import sys
import text2kwl.parse_text as t2k
import voice as v

def get_lc(language):
  return k.get_kasa_from_language(language)

def extract_kwl(text, tag='kwl'):
  stories = re.findall(r"(<%(tag)s.*?%(tag)s>)" % {'tag': tag}, text, re.S|re.M|re.DOTALL)
  return stories

def parse_kwl(kwl):
  kwl = kwl.strip()
  if not kwl:
    return ''
  psr = kwl2text.kwl2textParser()
  sem = semantics.Semantics()

  if '<kwl' != kwl[0:4]:
    kwl = u'<kwl %s ;' % kwl  # Convert into a proper KWL story
  ast = psr.parse(kwl, 'kwl2text', semantics=sem, parseinfo=True)
  if not ast['v']:
    raise ValueError('FAILED to parse %s as KWL' % kwl)

  return ast


def localize(kwl, language, lexicon={}, voice=None):
  """Convert <kwl> code into language."""
  lexicon = lexicon if len(lexicon) else data.load_td('english', language)
  grammar_model = data.load_grammar(language)

  if voice and 'subs' in grammar_model.data:
    grammar_model.data['subs'] += data.get_voice_substitutions(language, voice)

  tg = Generator(get_lc(language), language, grammar_model,
                 ast=parse_kwl(kwl), lexicon=lexicon)
  kwl_l10n = tg.generate()
  return kwl_l10n


def text_to_kwl(text, lexicon={}):
  lexicon = lexicon if len(lexicon) else data.load_td('english', 'english')
  return t2k.text_to_kwl(text, lexicon) 


def kwl_to_text(kwl_text, language):
  return localize(kwl_text, language)

__all__ = ['text_to_kwl', 'kwl_to_text']

if __name__ == '__main__':
  import sys

  args_len = len(sys.argv)
  if args_len == 3:
    print kwl_to_text(sys.argv[1], sys.argv[2])
  elif args_len == 2:
    print text_to_kwl(sys.argv[1])
  else:
    print """Usage:
      python kwl.py <kwl2text> <language>
      python kwl.py <text2kwl>
      """
