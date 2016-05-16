# coding: utf-8
"""Allow customization of standard output into idiosyncratic forms."""

import data
import pronounce as p

def get_voices(language):
  "Print out list of available voices in this language."


def apply_voice(language, voice, surface):
  "Apply the substitutions of this particular voice."
  subs = data.get_voice_substitutions(language, voice)
  return p.find_and_replace(surface, subs) 
