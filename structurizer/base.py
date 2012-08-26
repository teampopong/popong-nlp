#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is a library to structurize 
short free texts written in the Korean language.

[Params]
 - fieldname:
    votenum, district, elected, name_kr, voterate, name_cn, 
    experience, sex, birthyear, job, party, assembly_no, education

 - opt:
    Integer in [1,82] || String in {'all', 'test'}
"""

import re, os, json 
from pprint import pprint
from collections import Counter
from glob import glob

import utils
from importer import importer
from preprocessor import preprocessor
from rules import apply_rules


settings = {
    'DIR': '''../../crawlers/election_commission/data/''',
    'MAX_PRINT': 30,
    'MAX_ELECTIONS': 20,
    'DELIMS': '[ .,()0-9]'
    }

def test(fieldname, nprint, flatten, opt):

    rawlist = importer(settings['DIR'], opt, fieldname)
    fieldlist = preprocessor(rawlist)
    fieldlist = apply_rules(fieldname, fieldlist)

    tmp = list(zip(fieldlist, rawlist))
    pprint(tmp)
    print(len(tmp))

    if flatten == 1:
        wordlist = list_parser(fieldlist)
        wordlist = flatten_list(wordlist)
    else:
        wordlist = fieldlist

    cnt = word_counter(wordlist)

    #pprint(cnt.most_common(nprint))

    return cnt

def word_counter(wordlist):
    cnt = Counter()
    for word in wordlist:
        cnt[word] += 1
    return cnt

def flatten_list(listoflist):

    def str2list(item):
        if isinstance(item, str):
            item = [item]
        else:
            pass
        return item

    listoflist = [str2list(item) for item in listoflist]
    return [item for sublist in listoflist for item in sublist]

def list_parser(rawlist):
    wordlist = (filter(None, re.split(settings["DELIMS"],item))\
            for item in rawlist)
    return wordlist

if __name__ == '__main__':
    test()
