#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import sys
import itertools
from collections import Counter

import settings as s
import regex
import pandas as pd

LEVELS = s.district['levels']
SUBLEVELS = s.district['sublevels']
STOPWORDS = s.district['stopwords']
ALIASES = s.district['aliases']

def read_data(data):
    with open(data, 'r') as f:
        return f.read().decode('utf-8')

def convert(line, ends):

    def spacer(line, ends):
        if any(line.endswith(e) for e in ends):
            line = '%s %s' % (line[:-1], line[-1])
        return line

    def eraser(word, stopwords):
        if any(word==stopword for stopword in stopwords):
            word = ''
        return word

    spaced = spacer(line, ends)
    words = regex.findall(ur'\p{Hangul}+', spaced)

    erased = filter(None, (eraser(word, STOPWORDS) for word in words))
    aliased = (ALIASES.get(word, word) for word in erased)

    return ' '.join(aliased)

def replace(line, codemap):

    def pop(word, codemap):
        # FIX: 부산 중동구 -> 부산광역시 중동
        i = 0
        popped = []
        for j in range(len(word)+1):
            challenger = codemap.get(word[i:j])
            if challenger!=None:
                popped.append(word[i:j])
                i = j
        return ' '.join(popped)

    replaced = []
    for word in line.split():
        if word in SUBLEVELS or codemap.get(word):
            replaced.append(word)
        else:
            replaced.append(pop(word, codemap))
    return ' '.join(replaced)

def encode(line, codemap):

    encoded = []
    for i, word in enumerate(line.split()):

        if i==0:
            codes = codemap.get(word)
            if len(codes)==1:
                encoded.append(codes[0])
            else:
                print 'uh-oh'
                sys.exit(2)
        else:
            if codemap.get(word):
                codes = [code for code in codemap.get(word)\
                    if code.startswith(encoded[0])]
                if len(codes)!=0:
                    encoded.append(codes[0])
                else:
                    encoded.append(None)
            else:
                encoded.append(None)

    return encoded

def codepick(codes):
    codes = filter(None, codes)
    maxlen = max(len(c) for c in codes)
    return [c for c in codes if len(c)==maxlen]

def struct(string, codemap):
    ends = [''.join(i) for i in list(itertools.product(LEVELS, SUBLEVELS))]
    converted = convert(string, ends)
    replaced = replace(converted, codemap)
    encoded = encode(replaced, codemap)
    picked = codepick(encoded)
    return picked

def write_results(lines, replaced, encoded, filename):
    with open(filename, 'w') as f:
        for l, c, e in zip(lines, replaced, encoded):
            s = '%s -> %s -> %s' % (l, c, e)
            f.write(s.encode('utf-8'))
            f.write('\n')
    print 'Results written to %s' % filename

def get_status(data, codemap):
    words = regex.findall(ur'\p{Hangul}+', data)
    cnt = Counter(words)

    encoded, unencoded = [], []
    for i, c in cnt.items():
        try:
            encoded.append('%s -> %s' % (codemap[i], i))
        except:
            unencoded.append(i)

    print '\n## Encoded'
    for e in encoded: print e
    print '\n## Not encoded'
    for u in unencoded: print u

def main(opt, codemap):
    ## Get data
    data  = read_data('./_output/people-all-%s.txt' % opt)
    #lines = data.split('\n')
    lines = data.split('\n')[500:600] # 경기 부천시원미구갑

    ## Convert data
    ends = [''.join(i) for i in list(itertools.product(LEVELS, SUBLEVELS))]
    converted = [convert(line, ends) for line in lines]
    replaced = [replace(line, codemap) for line in converted]
    encoded = [encode(line, codemap) for line in replaced]
    picked = [codepick(line) for line in encoded]

    ## Print results
    #for l, c in zip(lines, replaced): print '%s -> %s' % (l, c)
    for l, c, e, p in zip(lines, replaced, encoded, picked):
        print '%s -> %s -> %s -> %s' % (l, c, e, p)
    #write_results(lines, replaced, encoded, './_output/people-all-%s-encoded.txt' % opt)
    #get_status('\n'.join(replaced), codemap)

if __name__=='__main__':
    OPT = 'district'
    main(OPT)
