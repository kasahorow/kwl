JE = 'je'
TU = 'tu'
ELLE = 'el'
IL = 'il'
IT = 'it'
NOUS = 'nu'
VOUS = 'vu'
ILS = 'is'
ELLES = 'es'

afa = {
  # https://en.wikipedia.org/wiki/Afroasiatic_languages
  'order': {'default': (1, 0), 'adj_nom': (0, 1)},
  'order_triple': {'default': (0, 1, 2), },
}
bantu = {
  'order': {'default': (0, 1), 'det_nom': (1, 0), 'adj_nom': (1, 0), 'n_p': (1, 0), 'pos_nom': (1, 0)},
  'order_triple': {'default': (0, 1, 2)},
}
geez = {
  'order': {'default': (1, 0), 'adj_nom': (0, 1)},
  'order_triple': {'default': (0, 2, 1), },
}
kwa = {
#  'order': {'default': (1, 0), 'act_adv': (0, 1), 'n_p': (0, 1), 'pos_nom': (0, 1), 'nom_in': (0, 1), 'pre_nom': (0, 1), 'tu_adv': (0, 1), 'vous_adv': (0, 1)},
  'order': {'default': (0, 1), 'adj_nom': (1, 0), 'det_nom': (1, 0), 'nom_nom': (1, 0), 'of_p': (1, 0), 'pre_det_nom': (1, 0), 'pre_pos_nom': (1, 0), 'question': {'act_adv': (0, 1)},},
  'order_triple': {'default': (0, 1, 2), 'question': (2, 1, 0), },
}

latin = {
  'order': {'default': (0, 1), 'question': {'act_adv': (1, 0)}, },
  'order_triple': {'default': (0, 1, 2), 'question': (2, 1, 0)},
}
