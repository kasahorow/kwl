#!/bin/bash
export python=python2.7

python -m grako text2kwl.ebnf -o text2kwl.py

for testfile in `ls $1*_test.py`; do
  echo "Running tests in $testfile"
  python $testfile
done

