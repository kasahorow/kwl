# coding: utf-8
# Calculate the implementation coverage (using tests) of each kasahorow language in KWL

import kwl as g
import kwl_test as t
import kasahorow as k
import sys

def get_coverage(language, show_details=False):
  coverage = []
  for grade in t.COVERAGE:
    total = len(t.COVERAGE[grade])
    implemented = 0
    details = []
    if language in t.DATA_TESTS:
      implemented = len(set(t.COVERAGE[grade]).intersection(set(t.DATA_TESTS[language].keys())))
      if show_details:
        details = set(t.COVERAGE[grade]) - set(t.COVERAGE[grade]).intersection(set(t.DATA_TESTS[language].keys()))
    
    coverage.append("%s = %s%% %s" % (grade, 100*implemented/total, '//'.join(details)))

  return '\t'.join(coverage) + '\t' + language


if __name__ == '__main__':
  if len(sys.argv) > 1:
    language = sys.argv[1]
    print get_coverage(language, True)
    total = 1
  else:
    total = 0
    for kasa in k.get_kasahorow():
      print get_coverage(k.get_kasa_from_language(kasa))
      total = total + 1

  print "%s out of %s languages" % (total, len(k.get_kasahorow()))
    
