#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import with_statement

from setuptools import find_packages, setup


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except (IOError, OSError):
        pass


setup(name='popong_nlp',
      version='0.1',
      description='Team POPONG NLP package',
      long_description=readme(),
      url='http://github.com/teampopong/popong-nlp',
      author='Team POPONG',
      author_email='contact@popong.com',
      license='Apache 2.0',
      packages=find_packages(),
      package_data={'popong_nlp': [
          'data/dict/*.json',
          'data/codebooks/*.csv',
          'data/corpus/*.txt',
      ]},
      install_requires=[
          'pandas>=0.15.1',
          'regex>=2014.02.19',
          'Unidecode>=0.04.14',
      ])
