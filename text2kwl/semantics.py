# coding: utf-8
class Semantics:
  def _default(self, ast):
    return ast if ast else ''

  def adjective(self, ast):
    return self.entry(ast)

  def conjugated_verb(self, ast):
    return ''.join(ast)

  def conjunction(self, ast):
    return ' '.join(ast)

  def determiner(self, ast):
    return self.entry(ast)

  def entry(self, ast):
    if 't' in ast['v'] and 'v' in ast['v']:
      return '%s(%s)' % (ast['t'], self.entry(ast['v']))
    else:
      return ast['t'] + ':' + ast['v']

  def noun(self, ast):
    return self.entry(ast)

  def plural(self, ast):
    return '%s(%s)' % (ast['t'], ast['v'])

  def preposition_p(self, ast):
    # in(adj:perfect_nom:peace)
    ast[0] = ast[0]['v']
    return '%s(%s)' % tuple(ast)

  def pronoun(self, ast):
    return self.entry(ast)

  def subject_verb_object(self, ast):
    # act:eat nom:food
    return '%s %s %s' % (ast['subject'], ast['verb'], ast['object'])

  def title(self, ast):
    return '%s(%s)' % (ast['t'], ast['v'].lower())

  def tuple(self, ast):
    # adj:good_nom:dog
    if 'raw(' in ast[0] and 'raw(' in ast[1]:
      return ast[0].replace(')', '') + ast[1].replace('raw(', ' ')
    else:
      return '_'.join([ast[0], ast[1]])

  def triple(self, ast):
    # det:the(adj:good_nom:dog)
    return '%s(%s_%s)' % (ast[0], ast[1], ast[2])

  def verb_object(self, ast):
    # act:eat nom:food
    return '%s %s' % (ast['verb'], ast['object'])


  def verb(self, ast):
    return self.entry(ast)

  def sentence(self, ast):
    if type([]) == type(ast):
      return ' '.join(ast)
    else:
      return ast
    
