#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re, os, json 
from pprint import pprint
from collections import Counter
from glob import glob

import utils
from importer import importer
from preprocessor import preprocessor
from rules import apply_rules
from wordify import wordify
from base import *

fieldname = 'education'
nprint = 30
flatten =1
opt = 'test'

settings = {
    'DIR': '''../../crawlers/election_commission/data/''',
    'MAX_PRINT': 30,
    'MAX_ELECTIONS': 20,
    'DELIMS': '[^\w]',
    'NCOLUMNS': 6
    }

rawlist = importer(settings['DIR'], opt, fieldname)
fieldlist = preprocessor(rawlist)
fieldlist = apply_rules(fieldname, fieldlist)
fieldlist = wordify(fieldlist, ['졸업','수료','박사','석사'])
fieldlist = list(fieldlist)

wordlist = list_parser(fieldlist)
wordlist = list(wordlist)
#wordlist = utils.prettify(wordlist)

utils.print_csv('output/edu.csv', wordlist)

birthyear = importer(settings['DIR'], opt, 'birthyear')
name_kr = importer(settings['DIR'], opt, 'name_kr')
tmp = list(zip(birthyear, name_kr, wordlist, rawlist))
#tmp = list(zip(birthyear, name_kr, fieldlist, rawlist))
pprint(tmp)
print(len(tmp))

if flatten == 1:
    wordlist = list_parser(fieldlist)
    wordlist = flatten_list(wordlist)
else:
    wordlist = fieldlist
'''
for word in wordlist:
    if len(word) < 3:
        print(word)
'''
cnt = word_counter(wordlist)
aa = cnt.most_common(nprint)
pprint(aa)
