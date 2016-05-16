# coding: utf-8

"""Language models for all kasahorow languages.
   Relies on composition instead of inheritance.
   Ref: http://learnpythonthehardway.org/book/ex44.html
"""

def get_kasahorow():
  return sorted(['ak', 'am', 'de', 'ee', 'en', 'es', 'ff', 'fr', 'ge', 'ha', 'ig', 'ki', 'lg', 'ln', 'lw', 'mg', 'ny', 'om', 'pt', 'rw', 'sn', 'so', 'sw', 'ss', 'ti', 'tz', 'wo', 'xh', 'yo', 'zu'])

def get_kasa_from_language(language):
  kasa = language
  langs = {
    'akan': 'ak',
    'amarinya': 'am',
    'fanti': 'ak-fat',
    'chewa': 'ny',
    'english': 'en',
    'french': 'fr',
    'fula': 'ff',
    'gadangme': 'ge',
    'gbe': 'ee',
    'deutsch': 'de',
    'hausa': 'ha',
    'igbo': 'ig',
    'gikuyu': 'ki',
    'kongo': 'kg',
    'lingala': 'ln',
    'luganda': 'lg',
    'luwo': 'lw',
    'malagasy': 'mg',
    'oromoo': 'om',
    'portuguesa': 'pt',
    'shona': 'sn',
    'sinhala': 'si',
    'soomaali': 'so',
    'swati': 'ss',
    'espanyol': 'es',
    'swahili': 'sw',
    'tamazight': 'tz',
    'tigrinya': 'ti',
    'twi': 'ak-twi',
    'ururimi': 'rw',
    'wolof': 'wo',
    'xhosa': 'xh',
    'yoruba': 'yo',
    'zulu': 'zu',
  }
  inv_langs = {v: k for k, v in langs.items()}

  if len(language)>2 and language in langs:
    kasa = langs[language]
  elif language in inv_langs:
    kasa = inv_langs[language]

  return kasa


