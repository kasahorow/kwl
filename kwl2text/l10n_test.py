# coding: utf-8

import l10n as l
import unittest


class L10nTest(unittest.TestCase):
  def setUp(self):
    pass

  def testPlurals(self):
    # Regular nouns
    self.assertEquals(u'nkua', l.plural('akan', u'kua'))
    self.assertEquals(u'mbusua', l.plural('akan', u'busua'))
    # Foreign-imports nouns
    self.assertEquals(u'lɔre', l.plural('akan', u'lɔre'))
    self.assertEquals(u'bɔɔl', l.plural('akan', u'bɔɔl'))  # foreign-word imports
    
    # Activity nouns
    self.assertEquals(u'bɔɔlbɔ', l.plural('akan', u'bɔɔlbɔ'))  # foreign-word imports
    self.assertEquals(u'skuulkɔ', l.plural('akan', u'skuulkɔ'))  # foreign-word imports
    self.assertEquals(u'dwumayɛ', l.plural('akan', u'dwumayɛ'))  # foreign-word imports
    


if __name__ == '__main__':
  unittest.main()
