# coding: utf-8
# Calculate the implementation coverage (using tests) of each kasahorow language in KWL

import kwl as g
import kwl_test as t
import kasahorow as k
import sys

def get_coverage(kasa, show_details=False):
  language = g.get_lc(kasa)
  coverage = []
  for grade in t.COVERAGE:
    total = len(t.COVERAGE[grade])
    implemented = 0
    details = []
    if language in t.KWL_TESTS:
      implemented = len(set(t.COVERAGE[grade]).intersection(set(t.KWL_TESTS[language].keys())))
      if show_details:
        details = set(t.COVERAGE[grade]) - set(t.COVERAGE[grade]).intersection(set(t.KWL_TESTS[language].keys()))
    
    coverage.append("%s = %s%% %s" % (grade, 100*implemented/total, '//'.join(details)))

  return '\t'.join(coverage) + '\t' + language


if __name__ == '__main__':
  if len(sys.argv) > 1:
    kasa = sys.argv[1]
    print get_coverage(kasa, True)
    total = 1
  else:
    total = 0
    for kasa in k.get_kasahorow():
      print get_coverage(kasa)
      total = total + 1

  print "%s out of %s languages" % (total, len(k.get_kasahorow()))
    
