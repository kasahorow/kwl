#!/bin/bash
export python=python2.7
for testfile in `ls $1*_test.py`; do
  echo "Running tests in $testfile"
  python $testfile
done

cd kwl2text
./make.sh

cd ../text2kwl
./make.sh
