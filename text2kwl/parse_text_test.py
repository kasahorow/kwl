# coding: utf-8

import parse_text as p
import unittest

class ParserTest(unittest.TestCase):
  def setUp(self):
    self.td = {
      'and-conjunction': '',
      'am-verb je tdy': 'be',
      'children-noun plural': 'child',
      'dog-noun': '',
      'eat-verb': '',
      'have-verb': '',
      'food-noun': '',
      'good-adjective': '',
      'in-preposition': '',
      'I-pronoun': '',
      'walk-verb': '',
      'my-possessive': '',
      'peace-noun': '',
      'perfect-adjective': '',
      'sleep-verb': '',
      'the-determiner': '',
      'white-adjective': '',
    }
    pass

  def testPosTagging(self):
    self.assertEquals('det:the', p.tag_pos('the', self.td, '-'))
    self.assertEquals('nom:dog', p.tag_pos('dog', self.td, '-'))
    self.assertEquals('adj:white', p.tag_pos('white', self.td, '-'))
    self.assertEquals('act:eat', p.tag_pos('eat', self.td, '-'))
    self.assertEquals('pos:my', p.tag_pos('my', self.td, '-'))
    self.assertEquals('pro:I', p.tag_pos('I', self.td, '-'))
    self.assertEquals('and', p.tag_pos('and', self.td, '-'))
    self.assertEquals('plural(nom:child)', p.tag_pos('children', self.td, '-'))
    self.assertEquals('tdy(je(act:be))', p.tag_pos('am', self.td, '-'))

  def testText2Raw(self):
    self.assertEqual('', p.text_to_kwl('', self.td))
    self.assertEqual('raw(UnknownWord)', p.text_to_kwl('UnknownWord', self.td))
    self.assertEqual('raw(Unknown Word)', p.text_to_kwl('Unknown Word', self.td))

  def testText2Title(self):
    self.assertEqual('title(det:the)', p.text_to_kwl('The', self.td))

  def testInteger2Adj(self):
    self.assertEqual('adj:150', p.text_to_kwl('150', self.td))

  def testText2DetNom(self):
    self.assertEqual('det:the_nom:dog', p.text_to_kwl('the dog', self.td))
    self.assertEqual('adj:white_nom:dog', p.text_to_kwl('white dog', self.td))
    self.assertEqual('act:eat nom:food', p.text_to_kwl('eat food', self.td))
    self.assertEqual('det:the(adj:good_nom:dog)', p.text_to_kwl('the good dog', self.td))
    self.assertEqual('pro:I act:eat nom:food', p.text_to_kwl('I eat food', self.td))
    self.assertEqual('pro:I act:have plural(nom:child)', p.text_to_kwl('I have children', self.td))
    self.assertEqual('act:sleep in(adj:perfect_nom:peace)', p.text_to_kwl('sleep in perfect peace', self.td))
    self.assertEqual('pro:I act:sleep in(adj:perfect_nom:peace)', p.text_to_kwl('I sleep in perfect peace', self.td))
    self.assertEqual('nom:food and nom:dog', p.text_to_kwl('food and dog', self.td))
    self.assertEqual('tdy(je(act:be))', p.text_to_kwl('am', self.td))
    self.assertEqual('tdy(je(act:be)) adj:white', p.text_to_kwl('am white', self.td))
    self.assertEqual('pro:I tdy(je(act:be)) adj:good', p.text_to_kwl('I am good', self.td))
    self.assertEqual('pro:I act:have adj:good', p.text_to_kwl('I have good', self.td))

if __name__ == '__main__':
  unittest.main()
