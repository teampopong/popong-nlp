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


settings = {
    'DIR': '''../../crawlers/election_commission/data/''',
    'MAX_PRINT': 30,
    'MAX_ELECTIONS': 20,
    'DELIMS': '[ .,()0-9]'
    }

def test(fieldname, nprint, flatten, opt):

    def printer():
        print('\n===' + fieldname.upper() + '===')
        print_filenames(opt)
        print('n(files)\t: '+ str(len(filenames)))
        print('n(items)\t: '+ str(len(fieldlist)))
        print('n(words)\t: '+ str(len(wordlist)))
        pprint(cnt.most_common(nprint))

    def print_filenames(opt):
        if opt != 'all':
            print('Files:')
            pprint(filenames)
        else:
            pass
           
    filenames = get_filenames(settings["DIR"], opt)
    fieldlist = get_rawlist(filenames, fieldname)

    if flatten == 1:
        wordlist = list_parser(fieldlist)
        wordlist = flatten_list(wordlist)
    else:
        wordlist = fieldlist

    cnt = word_counter(wordlist)
    printer()

def get_filenames(directory, opt='all'):

    def all_filenames(directory):
        return glob(os.path.join(directory, '*'))

    def select_filenames(filenames, opt):
        if isinstance(opt, int):
            filenames = [filenames[opt]]
        elif isinstance(opt, str):
            if opt == 'all':
                pass
            elif opt == 'test':
                filenames = [filenames[0], filenames[39], filenames[50]]
            else:
                raise "Error: String options should be in {'all', 'test'}"
        else:
            raise "Error: Options should either be\
                    an integer in [1,82] or string in {'all', 'test'}"
        return filenames

    allfilenames = all_filenames(settings['DIR'])
    filenames = select_filenames(allfilenames, opt)

    return filenames

def get_rawlist(filenames, fieldname):
    rawlist = (p[fieldname] for f in filenames for p in read_people(f))
    rawlist = flatten_list(rawlist)
    return rawlist

def read_people(filename):
    with open(filename, 'r') as f:
        j = f.read()
        people = json.loads(j)
    return people

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
