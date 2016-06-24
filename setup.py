# coding: utf-8

import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='kwl',
      license='BSD',
      version='0.2016.6.0',
      description='Utilities for KWL: kasahorow Writer\'s Language',
      long_description=read('README.md'),
      keywords='translation kasahorow',
      author='Paa Kwesi Imbeah',
      author_email='imbeah@yahoo.com',
      url='https://www.kasahorow.org/',
      data_files=[('', ['README.md'])],
      py_modules=['kasahorow', 'kwl', 'pronounce', 'voice'],
      packages=find_packages(),
      package_data={'data': ['data/*tsv']},
      include_package_data=True,
      install_requires=['grako==3.6.8'],
     )
