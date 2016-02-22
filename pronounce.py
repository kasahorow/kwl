#!/usr/bin/env python
# encoding: utf-8

import logging
import re

# Tuples of Akan word and common spoken rendition
AKAN_TWI = [  # Order matters
  (u'fo$', u'foɔ', 'e.g. sɔfo -> sɔfoɔ'),
  ('gua', 'dwa'),
  ('mb', 'mm'),
  ('nd', 'nn'),
  ('nye', 'ne'),
  ('nyi', 'ni'),
  ('te$', u'teɛ', u'e.g. aberante -> aberanteɛ'),
  ('tu$', u'tuo', 'e.g. afotu -> afotuo'),
]

AKAN_FANTI = [  # Order matters
  (r'a(?P<consonant>[^aeɛioɔu])i', r'e\g<consonant>i', 'e.g. adiban -> ediban'),
  (r'a(?P<consonant>[^aeɛioɔu])u', r'e\g<consonant>u', 'e.g. aduonu -> eduonu'),
  ('de', 'dze'),
  ('di', 'dzi'),
  ('te', 'tse'),  # e.g. ketew -> ketsew (must come before the next rule else ketew becomes ketw)
  (r'e(?P<consonant>[^aeɛioɔu])e', r'e\g<consonant>', 'e.g. bere -> ber'),
  ('iri', 'ir'),
  ('iri', 'ir'),
  ('oro', 'or'),
  ('ti', 'tsi'),
]

GEEZ = [  # Order matters. Generally, longest sequence is replaced first
  (u'0', u'0'), (u'1', u'1'), (u'2', u'2'), (u'3', u'3'), (u'4', u'4'), (u'5', u'5'), (u'6', u'6'), (u'7', u'7'), (u'8', u'8'), (u'9', u'9'),
  (u'ha', u'ሀ'),  (u'hu', u'ሁ'), (u'hi', u'ሂ'), (u'haa', u'ሃ'), (u'he', u'ሄ'), (u'hii', u'ህ'), (u'ho', u'ሆ'),
  (u'la', u'ለ'), (u'lu', u'ሉ'), (u'li', u'ሊ'), (u'laa', u'ላ'), (u'le', u'ሌ'), (u'lii', u'ል'), (u'lo', u'ሎ'),
  (u'hwa', u'ሐ'), (u'hwu', u'ሑ'), (u'hwii', u'ሒ'), (u'hwaa', u'ሓ'), (u'hwe', u'ሔ'), (u'hwi', u'ሕ'), (u'hwo', u'ሖ'),
  (u'ma', u'መ'), (u'mu', u'ሙ'), (u'mii', u'ሚ'), (u'maa', u'ማ'), (u'me', u'ሜ'), (u'mi', u'ም'), (u'mo', u'ሞ'),
  (u'sa', u'ሠ'), (u'su', u'ሡ'), (u'sii', u'ሢ'), (u'saa', u'ሣ'), (u'se', u'ሤ'), (u'si', u'ሥ'), (u'so', u'ሦ'),
  (u'ra', u'ረ'), (u'ru', u'ሩ'), (u'rii', u'ሪ'), (u'raa', u'ራ'), (u're', u'ሬ'), (u'ri', u'ር'), (u'ro', u'ሮ'),
  (u'ssa', u'ሰ'), (u'ssu', u'ሱ'), (u'ssii', u'ሲ'), (u'ssaa', u'ሳ'), (u'sse', u'ሴ'), (u'ssi', u'ስ'), (u'sso', u'ሶ'),
  (u'sha', u'ሸ'), (u'shu', u'ሹ'), (u'shii', u'ሺ'), (u'shaa', u'ሻ'), (u'she', u'ሼ'), (u'shi', u'ሽ'), (u'sho', u'ሾ'),
  (u'ka', u'ቀ'), (u'ku', u'ቁ'), (u'kii', u'ቂ'), (u'kaa', u'ቃ'), (u'ke', u'ቄ'), (u'ki', u'ቅ'), (u'ko', u'ቆ'), #(u'', u''), (u'', u''), (u'', u''), (u'', u''), (u'', u''),
  (u'qa', u'ቐ'), (u'qu', u'ቑ'), (u'qii', u'ቒ'), (u'qaa', u'ቓ'), (u'qe', u'ቔ'), (u'qi', u'ቕ'), (u'qo', u'ቖ'),# (u'', u''), (u'', u''), (u'', u''), (u'', u''), (u'', u''),
  (u'ba', u'በ'), (u'bu', u'ቡ'), (u'bii', u'ቢ'), (u'baa', u'ባ'), (u'be', u'ቤ'), (u'bi', u'ብ'), (u'bo', u'ቦ'),
  (u'bwa', u'ቧ'),
  (u'va', u'ቨ'), (u'vu', u'ቩ'), (u'vii', u'ቪ'), (u'vaa', u'ቫ'), (u've', u'ቬ'), (u'vi', u'ቭ'), (u'vo', u'ቮ'),
  (u'ta', u'ተ'), (u'tu', u'ቱ'), (u'tii', u'ቲ'), (u'taa', u'ታ'), (u'te', u'ቴ'), (u'ti', u'ት'), (u'to', u'ቶ'),
  (u'cha', u'ቸ'), (u'chu', u'ቹ'), (u'chii', u'ቺ'), (u'chaa', u'ቻ'), (u'che', u'ቼ'), (u'chi', u'ች'), (u'cho', u'ቾ'),

  (u'hya', u'ኀ'), (u'hyu', u'ኁ'), (u'hyii', u'ኂ'), (u'hyaa', u'ኃ'), (u'hye', u'ኄ'), (u'hyi', u'ኅ'), (u'hyo', u'ኆ'), (u'hywa', u'ኈ'), (u'hywii', u'ኊ'), (u'hywaa', u'ኋ'), (u'hywe', u'ኌ'), (u'hywi', u'ኍ'),
  (u'naa', u'ነ'), (u'nu', u'ኑ'), (u'nii', u'ኒ'), (u'na', u'ና'), (u'ne', u'ኔ'), (u'ni', u'ን'), (u'no', u'ኖ'),
  (u'nwa', u'ኗ'),
  (u'gna', u'ኘ'), (u'gnu', u'ኙ'), (u'gni', u'ኚ'), (u'gnaa', u'ኛ'), (u'gne', u'ኜ'), (u'gnii', u'ኝ'), (u'gno', u'ኞ'),
  (u'a', u'አ'), (u'u', u'ኡ'), (u'ii', u'ኢ'), (u'aa', u'ኣ'), (u'e', u'ኤ'), (u'i', u'እ'), (u'o', u'ኦ'),

 # (u'kha', u''), (u'u', u''), (u'ii', u''), (u'a', u''), (u'e', u''), (u'i', u''), (u'o', u'')
#, (u'', u''), (u'', u''), (u'', u''), (u'', u''), (u'', u''),

  (u'kha', u'ከ'), (u'khu', u'ኩ'), (u'khii', u'ኪ'), (u'khaa', u'ካ'), (u'khe', u'ኬ'), (u'khi', u'ክ'), (u'kho', u'ኮ'), (u'khwa', u'ኰ'), (u'khwii', u'ኲ'), (u'khwaa', u'ኳ'), (u'khwe', u'ኴ'), (u'khwi', u'ኵ'),
  (u'ksa', u'ኸ'), (u'ksu', u'ኹ'), (u'ksii', u'ኺ'), (u'ksaa', u'ኻ'), (u'kse', u'ኼ'), (u'ksi', u'ኽ'), (u'kso', u'ኾ'), (u'kswa', u'ዀ'), (u'kswii', u'ዂ'), (u'kswaa', u'ዃ'), (u'kswe', u'ዄ'), (u'kswi', u'ዅ'),
  (u'wa', u'ወ'), (u'wu', u'ዉ'), (u'wii', u'ዊ'), (u'waa', u'ዋ'), (u'we', u'ዌ'), (u'wi', u'ው'), (u'wo', u'ዎ'),
  (u'ja', u'ዐ'), (u'ju', u'ዑ'), (u'jii', u'ዒ'), (u'jaa', u'ዓ'), (u'je', u'ዔ'), (u'ji', u'ዕ'), (u'jo', u'ዖ'),
  (u'za', u'ዘ'), (u'zu', u'ዙ'), (u'zii', u'ዚ'), (u'zaa', u'ዛ'), (u'ze', u'ዜ'), (u'zi', u'ዝ'), (u'zo', u'ዞ'), (u'zwaa', u'ዟ'),
  (u'dza', u'ዠ'), (u'dzu', u'ዡ'), (u'dzii', u'ዢ'), (u'dzaa', u'ዣ'), (u'dze', u'ዤ'), (u'dzi', u'ዥ'), (u'dzo', u'ዦ'),
  (u'ya', u'የ'), (u'yu', u'ዩ'), (u'yii', u'ዪ'), (u'yaa', u'ያ'), (u'ye', u'ዬ'), (u'yi', u'ይ'), (u'yo', u'ዮ'),
  (u'da', u'ደ'), (u'du', u'ዱ'), (u'dii', u'ዲ'), (u'daa', u'ዳ'), (u'de', u'ዴ'), (u'di', u'ድ'), (u'do', u'ዶ'),
  (u'gha', u'ጀ'), (u'ghu', u'ጁ'), (u'ghii', u'ጂ'), (u'ghaa', u'ጃ'), (u'ghe', u'ጄ'), (u'ghi', u'ጅ'), (u'gho', u'ጆ'),
  (u'ga', u'ገ'), (u'gu', u'ጉ'), (u'gii', u'ጊ'), (u'gaa', u'ጋ'), (u'ge', u'ጌ'), (u'gi', u'ግ'), (u'go', u'ጎ'),# (u'', u'ጐ'), (u'', u'ጒ'), (u'', u'ጓ'), (u'', u'ጔ'), (u'', u'ጕ'),
  (u'tha', u'ጠ'), (u'thu', u'ጡ'), (u'thii', u'ጢ'), (u'thaa', u'ጣ'), (u'the', u'ጤ'), (u'thi', u'ጥ'), (u'tho', u'ጦ'),
  (u'cza', u'ጨ'), (u'czu', u'ጩ'), (u'czii', u'ጪ'), (u'czaa', u'ጫ'), (u'cze', u'ጬ'), (u'czi', u'ጭ'), (u'czo', u'ጮ'),
  (u'pha', u'ጰ'), (u'phu', u'ጱ'), (u'phii', u'ጲ'), (u'phaa', u'ጳ'), (u'phe', u'ጴ'), (u'phi', u'ጵ'), (u'pho', u'ጶ'),
  (u'sza', u'ጸ'), (u'szu', u'ጹ'), (u'szii', u'ጺ'), (u'szaa', u'ጻ'), (u'sze', u'ጼ'), (u'szi', u'ጽ'), (u'szo', u'ጾ'),
  (u'zsa', u'ፀ'), (u'zsu', u'ፁ'), (u'zsii', u'ፂ'), (u'zsaa', u'ፃ'), (u'zse', u'ፄ'), (u'tze', u'ፅ'), (u'zso', u'ፆ'),
  (u'fa', u'ፈ'), (u'fu', u'ፉ'), (u'fii', u'ፊ'), (u'faa', u'ፋ'), (u'fe', u'ፌ'), (u'fi', u'ፍ'), (u'fo', u'ፎ'),
  (u'pa', u'ፐ'), (u'pu', u'ፑ'), (u'pii', u'ፒ'), (u'paa', u'ፓ'), (u'pe', u'ፔ'), (u'pi', u'ፕ'), (u'po', u'ፖ'),
  (u'gwa', u'ጐ'), (u'gwaa', u'ጓ'),
  (u'lwa', u'ሏ'),
  (u'qwaa', u'ቋ'),
  (u'swa', u'ሷ'),
  (u'zhwa', u'ዧ'),
]

SINHALA = [
 (u'a', u'අ'), (u'aa', u'\u0dcf'), (u'ee', u'ේ'),(u'ɛ', u'ඇ'),  (u'ɛ', u'\u0dd0'), (u'ɛɛ', u'\u0dd1'), (u'i', u'\u0dd2'), (u'ii', u'\u0dd3'), (u'o', u'ඔ'), (u'o', u'\u0ddc'), (u'oo', u'\u0ddd'),  (u'u', u'ු'), (u'uu', u'\u0dd6'), (u'h', u'\u0dca'), (u'_', u'ණ'), (u'_', u'ළ'), (u'_', u'\u0da7'), 
 (u'ba', u'බ'), 
 (u'da', u'ද'), 
 (u'ga', u'ග'), 
 (u'ha', u'හ'),
 (u'ka', u'ක'), 
 (u'ja', u'ජ'),
 (u'la', u'ල'),
 (u'na', u'න'), (u'nha', u'\u0db3'),
 (u'ma', u'ම'), 
 (u'pa', u'ප'),
 (u'ra', u'ර'),
 (u'sa', u'ස'),
 (u'ta', u'ත'),
 (u'tha', u'ථ'),
 (u'va', u'ව'),
 (u'ya', u'ය'),
]

def get_twi(word, pos):
  """Return Asante Twi pronunciation of Akan spelling."""
  twi = word
  for sub in AKAN_TWI:
    if len(sub) == 3:  # A regex
      twi = re.sub(sub[0], sub[1], twi)
    else:
      twi = twi.replace(sub[0], sub[1])
  return twi.lower()

def get_fanti(word, pos):
  """Return Fante pronunciation of Akan spelling."""
  fanti = word
  if word in ('dede'):  # Fanti non-conversion exceptions
    return word
  for sub in AKAN_FANTI:
    if len(sub) == 3:
      fanti = re.sub(sub[0], sub[1], fanti)
    else:
      fanti = fanti.replace(sub[0], sub[1])
  return fanti.lower()


def from_twi(word, pos):
  """Convert Twi pronunciation to Akan spelling."""
  akan = word.lower()
  for sub in AKAN_TWI:
    if len(sub) == 3:
      akan = re.sub(sub[1], sub[0], akan)
    else:
      akan = akan.replace(sub[1], sub[0])
  return akan


def from_fanti(word, pos):
  """Convert Fante pronunciation to Akan spelling."""
  akan = word
  for sub in AKAN_FANTI:
    if len(sub) == 3:
      akan = re.sub(sub[1], sub[0], akan)
    else:
      akan = akan.replace(sub[1], sub[0])
  return akan

def sinhala_to_latin():
  "Return a dictionary of Geez characters and their latin tokens."
  ltg = {}
  for pair in SINHALA:
    ltg[pair[1]] = pair[0]
  return ltg

def geez_to_latin():
  "Return a dictionary of Geez characters and their latin tokens."
  ltg = {}
  for pair in GEEZ:
    ltg[pair[1]] = pair[0]
  return ltg

def geez_to_latin():
  "Return a dictionary of Geez characters and their latin tokens."
  ltg = {}
  for pair in GEEZ:
    ltg[pair[1]] = pair[0]
  return ltg

def latin_to_geez():
  "Return a dictionary of latin tokens and their Geez characters."
  ltg = {}
  for pair in GEEZ:
    ltg[pair[0]] = pair[1]
  return ltg

def tokenize_geez(word):
  latin_tokens = geez_to_latin().values()
  vowels = 'aeiou'
  tokens = []
  sofar = ''
  count = 0
  word_length = len(word)
  for c in word:
    count+= 1
    sofar+= c
    if count < word_length and word[count] in vowels:
      continue  # All Geez alphabets start with consonants

    if sofar in latin_tokens:
      tokens.append(sofar)
      sofar = ''
    else:
      continue 
  return tokens

def get_geez(word):
  """Given a Unicode string of kasahorow Tigrinya, return the phonetic Tigrinya Abugida."""
  pron = u''
  latin = word.lower()
  ti_pron = latin
  to_geez = latin_to_geez()
  tokens = tokenize_geez(latin)
  if len(tokens) > 1:
    tokens.sort(key=len)  # Sort by longest token first before replacing
    tokens.reverse()
  for token in tokens:
    ti_pron = ti_pron.replace(token, to_geez[token])

  pron = ti_pron
  return pron

def get_latin(geez):
  latin = ''
  tokens = geez
  gtl = geez_to_latin()
  for token in tokens:
    if token.strip():
      latin+= gtl[token]
    else:
      latin+= token
  return latin

def abugida_to_latin(abugida, language):
  latin = ''
  tokens = abugida
  gtl = abugida_to_latin_map(language)
  for token in tokens:
    if token.strip():
      latin+= gtl[token]
    else:
      latin+= token
  return latin

def abugida_to_latin_map(language):
  if language in ('amarinya', 'geez', 'tigrinya'):
    alphabet_map = GEEZ
  elif 'sinhala' == language:
    alphabet_map = SINHALA
  ltg = {}
  for pair in alphabet_map:
    ltg[pair[1]] = pair[0]
  return ltg

def find_and_replace(word, subs):
  """Return Kirundi pronunciation of Ururimi spelling."""
  ru = word
  for sub in subs:
    if len(sub) == 3:
      ru = re.sub(sub[0], sub[1], ru)
    else:
      ru = ru.replace(sub[0], sub[1])
  return ru.lower()

def get_ururimi(word, style):
  if 'kirundi' == style:
    subs = [('cy', 'c'), ('jy', 'j'), ('shy', 'sh'), ('by', 'vy')]
    word = find_and_replace(word, subs) 
  return word

def get_yoruba(word, style):
  if 'oyo' == style:
    subs = [('ah', u'á'), ('ha', u'à'), ('eh', u'é'), ('he', u'è'),
            (u'ẹh', u'ẹ́'), (u'hẹ', u'ẹ̀'), ('ih', u'í'), ('hi', u'ì'),
            ('oh', u'ó'), ('ho', u'ò'), (u'ọh', u'ọ́'), (u'họ', u'ọ̀'),
            ('uh', u'ú'), ('hu', u'ù')]
    word = find_and_replace(word, subs) 
  return word


def get_phonetic(word, lang):
  phonetic = ''
  if lang == 'akan':
    phonetic = get_twi(word, 'noun')
  elif lang in ('amaarignaa', 'geez', 'tigirignaa'):
    phonetic = get_latin(word) 
  elif lang in ('kirundi', 'kinyarwanda'):
    phonetic = get_ururimi(word, lang)
  elif lang == 'sinhala':
    phonetic = abugida_to_latin(word, 'sinhala')
  elif lang == 'yoruba':
    phonetic = get_yoruba(word, 'oyo')
  return phonetic

