# coding: utf-8

import logging
import os

def load_td(lang_f, lang_t, show_errors=True):
  """Load the translation dictionary for this language pair.
     Values are in utf-8.
  """
  TD = {}
  cwd = os.path.dirname(os.path.abspath(__file__))
  lang_tsv = '%s/%s_%s_woaka.tsv' % (cwd, lang_f, lang_t)
  count = 0
  try:
    dictionary = open(lang_tsv, 'r').readlines()
  except IOError:
    dictionary = []
    logging.warn('%s not found!' % lang_tsv)

  for line in dictionary:
    count = count + 1
    data = line.strip().split('\t')
    try:  # key by entry, pos
      if lang_f == 'english' and lang_t != 'englishs':
        TD[get_td_key(data)] = data[0].decode('utf-8')
        TD[get_key([get_td_key(data), 'defn'])] = data[3].decode('utf-8')
        TD[get_key([get_td_key(data), 'sample'])] = data[5].decode('utf-8')
      else:
        pass
        #TD[get_td_key(data, True)] = data[1].decode('utf-8')
        #TD[get_key([get_td_key(data, True), 'defn'])] = data[4].decode('utf-8')
        #TD[get_key([get_td_key(data, True), 'sample'])] = data[5].decode('utf-8')
    except Exception, e:
      if False and show_errors:
        sys.stderr.write('No data for %s on line %s of %s: %s\n' % (data[0], count, lang_tsv, e))

  return TD


def get_td_key(tsv, use_kw_key=False):
  """Get key for looking up entries in the translation dictionary."""
  if use_kw_key:
    return get_key([tsv[0], tsv[2]])
  else:
    return get_key([tsv[1], tsv[2]])

def get_key(fragments):
  key = '-'.join([x for x  in fragments])
  return key.replace('#', ' ')
