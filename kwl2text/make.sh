#!/bin/bash

python -m grako kwl2text.ebnf -o kwl2text.py
#python -m grako ../kw.ebnf -o ../kwp.py

python parser_test.py

