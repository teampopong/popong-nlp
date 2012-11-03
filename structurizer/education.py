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
from wordify import wordify

settings = {
    'DIR': '''../../crawlers/election_commission/data/''',
    'MAX_PRINT': 30,
    'MAX_ELECTIONS': 20,
    'DELIMS': '[^\w\.]',
    'NCOLUMNS': 6,
    }

keywords = {
    'STATUS': ['졸업', '수료', '중퇴', '제적', '재학'],
    'COURSE': ['석사', '박사'],
    }

regexes = {
    'INSTITUTIONS': re.compile('([\w\s]*(University|학교|\s대학원))'),
    'MAJOR': re.compile('\w+대학원?'),
    'DEPTS': re.compile('\w+학과?|\w+학|\w+전공'),
    'TIME': re.compile(
        '([0-9]+(\.[0-9]*)?(\.[0-9]*)?)\~([0-9]+(\.[0-9]*)?(\.[0-9]*)?)'),
    }

def test(fieldname, nprint, flatten, opt):
    
    def printer():
        birthyear = importer(settings['DIR'], opt, 'birthyear')
        name_kr = importer(settings['DIR'], opt, 'name_kr')
        tmp = list(zip(birthyear, name_kr, wordlist, rawlist))
        print(len(tmp))
        utils.print_csv('edu.csv', fieldlist)

    rawlist = importer(settings['DIR'], opt, fieldname)

    fieldlist = preprocessor(rawlist)
    fieldlist = apply_rules(fieldname, fieldlist)
    fieldlist = wordify(fieldlist, ['졸업','수료','박사','석사', '대학원'])
    fieldlist = list(fieldlist)

    # list 생성
    def listify():
        return ['']*(settings['NCOLUMNS'])
    wordlist = [listify() for item in fieldlist]

    # pop keywords
    testlist = list(zip(wordlist, fieldlist))
    testlist = [pop_keywords(a, b, keywords['STATUS'], 5)\
            for a, b in testlist]
    testlist = [pop_keywords(a, b, keywords['COURSE'], 1)\
            for a, b in testlist]
    testlist = [pop_regexes(a, b, regexes['INSTITUTIONS'], 0)\
            for a, b in testlist]
    testlist = [pop_regexes(a, b, regexes['DEPTS'], 2)\
            for a, b in testlist]
    testlist = [pop_regexes(a, b, regexes['MAJOR'], 2)\
            for a, b in testlist]
    testlist = [pop_time(a, b) for a, b in testlist]


    #pop_major(testlist)
    #pop_time(testlist)

    for key, item in enumerate(testlist):
        item = list(item)
        item[1] = item[1].strip('[ ()]')
        testlist[key] = tuple(item)
    #'''
    # print results 
    for item in testlist:
        if item[1] != '':
            print(item)
            pass
    #'''
    #pprint(testlist)
    l = [t[0] for t in testlist]
    name_kr = importer(settings['DIR'], opt, 'name_kr')
    aa = list(zip(name_kr, l))
    d = dict()
    for a, b in aa:
        d[a] = b
    print()

    with open('output/edu.json', 'w') as f:
        json.dump(d, f, indent=2)
        pprint(d)
    #utils.print_csv('edu.csv', d)

def pop_keywords(outputlist, inputstring, keywords, outputidx):
    for k in keywords:
        if k in inputstring:
            outputlist[outputidx] = k
            inputstring = pop_string(inputstring, k)
    return outputlist, inputstring
 
def pop_regexes(outputlist, inputstring, regex, outputidx):
    m = regex.search(inputstring)
    if m:
        outputlist[outputidx] = outputlist[outputidx] + m.group(0)
        inputstring = pop_string(inputstring, m.group(0))
    return outputlist, inputstring

def pop_major(testlist):
    for a, b in testlist:
        m = regexes['MAJOR'].search(b)
        if m:
            matched = m.group(0)
            #if not a[2]:
            a[2] = a[2] + matched
            b = pop_string(b, matched)

def pop_time(outputlist, inputstring):
    m = regexes['TIME'].search(inputstring)
    if m:
        s, e = m.group(1), m.group(4)
        outputlist[3], outputlist[4] = s, e
        inputstring = pop_string(inputstring, m.group(0))
    return outputlist, inputstring
    
def pop_string(s1, s2):
    idx = s1.index(s2)
    return '%s %s' %(s1[:idx], s1[idx+len(s2):])

if __name__ == '__main__':
    test()
