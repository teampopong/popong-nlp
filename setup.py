#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(name='popong_nlp',
      version='0.1',
      description='Team POPONG NLP package',
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
          'regex>=2014.02.19',
          'Unidecode>=0.04.14',
      ],
      zip_safe=False)
