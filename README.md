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
This means that you can get functional representations suitable for *children's comprehension* into these languages. **You still need a native speaker to confirm correctness!**

* akan
* chewa
* gadangme
* gbe
* gikuyu
* hausa
* igbo
* lingala
* luganda
* luwo
* oromoo
* shona
* swahili
* yoruba
* zulu

## How to add a new language **foo**
This is simple to do. There are 2 main steps:
- add a dictionary of the **foo** in the data/ directory: data/english_foo_woaka.tsv
- set up grammar rules for **foo** the data/ directory: data/sua_foo.py

### Testing language **foo**
There are 2 main testing steps:
- Run python kwl_coverage.py foo to see what tests you need to add in the next step
- Run python kwl_tests.py foo by adding **foo** into the KWL_TESTS dictionary.

# Known issues
- No support for noun-adjective alliteration (relevant for Bantu languages such as Shona, Swahili, Ururimi)
- No support for vowel-harmony (relevant for Kwa languages such as Akan)
- Partial support for pluralization
- Partial support for stemming