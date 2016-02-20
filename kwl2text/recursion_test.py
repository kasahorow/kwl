#!/usr/bin/env python
# coding: utf-8

import sys
import os
import recursion

import unittest


class KWLTest(unittest.TestCase):
  def setUp(self):
    self.psr = recursion.recursionParser()
    self.maxDiff = None

  def testToken(self):
    alpha = 'abc'
    number = '12'
    sem_alpha = {'t': 'alpha', 'v': 'abc'}
    sem_number = {'t': 'number', 'v': '12'}
    self.assertEquals("1",
                      self.psr.parse("1", rule_name='expression'))
    self.assertEquals([u'{', u'1', u'}'],
                      self.psr.parse("{1}", rule_name='expression'))
    self.assertEquals([u'{', [u'{', u'1', u'}'], u'}'],
                      self.psr.parse("{{1}}", rule_name='expression'))
    self.assertEquals([ '{', [u'{', [u'{', u'1', u'}'], u'}'], '}'],
                      self.psr.parse("{{{1}}}", rule_name='expression'))

    print self.psr.parse("{{{1}}}", rule_name='sentence')
    print self.psr.parse("{{{1}}} {1}", rule_name='sentence')
    print self.psr.parse("{{{1}}} {1} 1", rule_name='sentence')
                      

if __name__ == '__main__':
  unittest.main()
