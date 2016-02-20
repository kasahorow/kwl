#!/bin/bash

python -m grako kwl2text.ebnf -o kwl2text.py

python parser_test.py

