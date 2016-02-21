# kwl
KWL is a semantic representation of natural language. A KWL representation can be transformed into any natural language with a grammar and a dictionary of that language.

For example, 
&lt;kwl nom:dog ; kwl&gt; becomes [kraman (Akan), dog (English), chien (French)]

&lt;kwl pro:you tdy(tu(act:be)) det:a(adj:important_nom:person). ; kwl&gt; becomes [ You are an important person (English) ]

Try it here: http://write.kasahorow.org/kwl 

# Installation

python setup.py install


# Testing

You can transform simple English into KWL representation, and then convert the KWL representation into any of the supported languages. Note that all the text is in lowercase.

## Text to KWL

* python -m kwl 'the dog'

## KWL to Text

* python -m kwl 'det:the_nom:dog' akan
* python -m kwl 'det:the_nom:dog' english
* python -m kwl 'det:the_nom:dog' oromo
* python -m kwl 'det:the_nom:dog' swahili


# Supported kasahorow languages
This means that you can get functional representations into these languages. **You still need a native speaker to confirm correctness!**

* akan
* chewa
* gadangme
* gbe
* gikuyu
* hausa
* lingala
* luganda
* luwo
* zulu

## How to add a new language
This is simple to do (but not well documented yet). However, there are 2 main steps:
- add a dictionary of the language in the data/ directory
- set up grammar rules for the language in the kwl2text/models.py, kwl2text/l10n.py and kwl2text/libconjugate.py files
