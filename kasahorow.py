# coding: utf-8

"""Language models for all kasahorow languages.
   Relies on composition instead of inheritance.
   Ref: http://learnpythonthehardway.org/book/ex44.html
"""

def get_kasahorow():
  return sorted(['ak', 'am', 'de', 'ee', 'en', 'es', 'ff', 'fr', 'ge', 'ha', 'ig', 'ki', 'lg', 'ln', 'lw', 'mg', 'ny', 'om', 'rw', 'sn', 'so', 'sw', 'ti', 'tz', 'wo', 'yo', 'zu'])

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
    'german': 'de',
    'hausa': 'ha',
    'igbo': 'ig',
    'gikuyu': 'ki',
    'kongo': 'kg',
    'lingala': 'ln',
    'luganda': 'lg',
    'luwo': 'lw',
    'malagasy': 'mg',
    'oromo': 'om',
    'shona': 'sn',
    'sinhala': 'si',
    'somali': 'so',
    'spanish': 'es',
    'swahili': 'sw',
    'tamazight': 'tz',
    'tigrinya': 'ti',
    'twi': 'ak-twi',
    'ururimi': 'rw',
    'wolof': 'wo',
    'yoruba': 'yo',
    'zulu': 'zu',
  }
  inv_langs = {v: k for k, v in langs.items()}

  if len(language)>2 and language in langs:
    kasa = langs[language]
  elif language in inv_langs:
    kasa = inv_langs[language]

  return kasa


