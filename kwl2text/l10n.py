#!/usr/bin/env python
# coding: utf-8

import os
import sys

def longest_prefix_match(search, urllist):
    # http://stackoverflow.com/questions/5434813/longest-prefix-matches-for-urls
    matches = [url for url in urllist if url.startswith(search)]
    if matches:
        return max(matches, key=len)
    else:
        return ''
        #raise Exception("Not found")


def longest_suffix_match(search, urllist):
    # http://stackoverflow.com/questions/5434813/longest-prefix-matches-for-urls
    matches = [url for url in urllist if url.endswith(search)]
    if matches:
        return max(matches, key=len)
    else:
        return ''

def get_word_prefix(word, prefixes=[]):
  key = longest_prefix_match(word[0:2], prefixes.keys())
  try:
    prefix = prefixes[key]
  except KeyError:
    prefix = ''
  return (key, prefix)

def get_word_suffix(word, suffixes=[]):
  key = longest_suffix_match(word[-2:0], suffixes.keys())
  try:
    suffix = suffixes[key]
  except KeyError:
    suffix = ''
  return (key, suffix)


#def plural(language, noun, number=2, nclass=None):
def plural(grammar, noun, number=2, nclass=None):
  """Return the plural form of this language. noun is a Unicode string."""
  prefix = ''
  suffix = ''
  stem = noun.strip()

  if number == 1:
    return noun

  if grammar.language == 'english':
    pl = u'%ss' % stem
    if pl[-4:] == 'tchs':  # so that 'loch' will still be lochs
      suffix = 'es'
    else:
      suffix = 's'

  elif grammar.language == 'akan':
    if ' ' in stem:  # compound
       data = stem.split(' ')
       return plural(grammar, data[0], number) + ' ' + plural(grammar, ' '.join(data[1:]), number) 
    elif stem[0] in ('[', 'l', 'r', 'v',  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'): # likely to be a foreign word import: redio, Venezuwela, lɔre
      pass  # Noun does not change form
    elif stem[-1:] in ('l'):  # like bɔɔl
      pass
    elif stem[-2:] in (u'bɔ', 'da', u'kɔ', u'yɛ'):  # Activities      
      pass
    elif stem[-3:] == 'nyi':
      prefix = 'a'
      stem = stem[:-3]
      suffix = 'fo'
    elif stem[0] in (u'b', u'f', u'p'):
      prefix = 'm'
    elif stem[0] not in ('n', 'm'):
      prefix = 'n'
 
    stem = stem.lstrip(u'aeioɔu')
    pl = u'%(prefix)s%(noun)s%(suffix)s' % { 'noun': noun.lstrip(u'aeioɔu'),
      'prefix': prefix, 'suffix': suffix}
  elif 'plural' in grammar.data:
    try:
      replace, prefix = get_word_prefix(noun, grammar.data['plural']['prefix'])
      stem = noun[len(replace):]
    except (IndexError, KeyError),  e:
      pass
    try:
      replace, suffix = get_word_suffix(noun, grammar.data['plural']['suffix'])
      stem = noun[:len(noun) - len(replace)]
    except (IndexError, KeyError),  e:
      pass

  pl = u'%(prefix)s%(stem)s%(suffix)s' % { 'prefix': prefix, 'stem': stem, 'suffix': suffix }
  return pl

