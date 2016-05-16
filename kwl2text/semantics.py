# coding: utf-8
class Semantics:
  def _default(self, ast):
    return ast
  
  def clean_label(self, label):
    return label.replace(':', '')

  def conjugated_verb(self, ast):
    return {'t': ast[0], 
            'v': {'t': ast[1], 'v': ast[2]}}

  def formatted(self, ast):
    return {'t': ast[0], 'v': ast[1]}

  def is_action(self, ptype):
    "Return True if this ptype is verb tense."
    parts = ptype.split('_')
    return ('v' in parts) or ('tdy' in parts) or ('tmw' in parts) or ('ydy' in parts)

  def token(self, ast):
    try:
      float(ast)
      return {'t':'number', 'v': ast }
    except ValueError:
      return {'t':'alpha', 'v': ast }

  def raw(self, ast):
    "A special primitive type like token()."
    fun, arg = ast.split('(')
    return {'t':fun, 'v': arg[:-1]}

  def triple_phrase(self, ast):
    return self.tuple(ast)

  def tuple(self, ast):
    return self.tuple_kwl(ast)

  def tuple_verb(self, ast):
    return self.tuple_kwl(ast)

  def tuple_entry_preposition_p_kwl(self, ast):
    return self.tuple_kwl(ast)

  def tuple_kwl(self, ast):
    return {'t': '%s_%s' % (ast[0]['t'], ast[1]['t']), 
            'v': ast}

  def get_tuple_type(self, label):
    label = label.replace(':', '')  # Remove trailing ':'
    ptypes = {
      'act': 'v_p',  # Verb phrase
      'adj': 'a_p',  # Adjective-headed phrase
      'det': 'd_p',  # Determiner-headed phrase
      'nom': 'n_p',  # Noun phrase
      'pro': 'n_p',  # Noun phrase
      'pre': 'p_p',  # Prepositional phrase
      'raw': 'n_p',  # Noun phrase
      'sci': 'n_p',  # Noun phrase
    }
    if label in ptypes:
      return ptypes[label]
    else:
     return '%s_p' % label
    
  def fun_word(self, ast):
    new_ast = []
    if len(ast) == 2:  
      new_ast.append(ast[0])
      new_ast.append(self.phrase(ast[1]))
    else:
      new_ast = ast
    return new_ast
  
  def phrase(self, words):
    ptypes = {
      'act': 'v_p',  # Verb phrase
      'adj': 'a_p',  # Adjective-headed phrase
      'det': 'd_p',  # Determiner-headed phrase
      'nom': 'n_p',  # Noun phrase
      'pro': 'n_p',  # Noun phrase
      'pre': 'p_p',  # Prepositional phrase
      'raw': 'n_p',  # Noun phrase
      'sci': 'n_p',  # Noun phrase
    }
    if len(words) == 0:
      return None
    elif len(words) == 1:
      return self._phrase(words, ptypes)
    elif len(words) == 2:
      return {'t': '%s_%s' % (words[0]['t'], words[1]['t']), 'v': words }
    elif len(words) > 2:
      return self._phrase(words, ptypes)
  
  def _phrase(self, words, ptypes):
      if words[0]['t'] in ptypes:
        return {'t': ptypes[words[0]['t']], 'v': words }      
      else:
       return {'t': '%s_p' % words[0]['t'], 'v': words }

  def sub_expression(self, ast):
    new_ast = ast[1] # Remove left_paren (ast[0]), and right_paren (ast[2])
    return new_ast

  def subject_verb(self, ast):
    return {'t': 's_v', 
            'v': [{'t': 'subject', 'v': ast['subject']},
                  {'t':'verb', 'v': ast['verb']}]}

  def subject_verb_object(self, ast):
    return {'t': 's_v_o', 
            'v': [{'t': 'subject', 'v': ast['subject']},
                  {'t':'verb', 'v': ast['verb']},
                  {'t':'object', 'v': ast['object']}]}

  def verb_object(self, ast):
    return {'t': 'v_o', 
            'v': [{'t': 'verb', 'v': ast['verb']},
                  {'t':'object', 'v': ast['object']}]}

  def statement(self, clauses):
    "Sentence type."
    return {'t': 'statement', 'v': clauses }

  def question(self, clauses):
    "Sentence type."
    return {'t': 'question', 'v': clauses }

  def command(self, clauses):
    "Sentence type."
    return {'t': 'command', 'v': clauses }

  def conjunction(self, ast):
    "A conjunction is a triplet, the type is the middle element."
    if 'v' in ast:
      return ast
    else:  # base case
      return {'t': ast[1], 'v': [ast[0], ast[2]]}

  def kwl2text(self, sentences):
    ns = []
    for s in sentences:
      if 't' in s:  # Ignore semicolon parses
        ns.append(s)
    return {'t': 'story', 'v': ns}

