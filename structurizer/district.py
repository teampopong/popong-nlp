#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
import sys
import itertools
from collections import Counter

import pandas as pd

import settings as s
from utils import utils
import base

ENDS = s.district['sublevels']
STOPWORDS = s.district['stopwords']
ALIASES = s.district['aliases']

def convert(line):
    spaced = base.spacer(line, ENDS)
    words = base.wordify(spaced)
    erased = base.eraser(words, STOPWORDS)
    canonized = base.canonizer(erased, ALIASES)
    return ' '.join(canonized)

def replace(line, codemap):
    replaced = []
    for word in line.split():
        if word in ENDS or codemap.get(word):
            replaced.append(word)
        else:
            replaced.append(base.pop(word, codemap))
    return ' '.join(replaced)

def codepick(codes):
    codes = filter(None, codes)
    maxlen = max(len(c) for c in codes)
    return [str(c) for c in codes if len(c)==maxlen]

def markup(string, codemap):
    converted = convert(string)
    replaced = replace(converted, codemap)
    encoded = base.encoder(replaced, codemap)

    tokens = replaced.split()
    if len(tokens)==len(encoded):
        return zip(tokens, encoded)
    else:
        print 'This cannot be happening!'
        sys.exit(2)

def struct(string, codemap):
    converted = convert(string)
    replaced = replace(converted, codemap)
    encoded = base.encoder(replaced, codemap)
    picked = codepick(encoded)
    return picked


def main(codemap):

    def write_results(lines, replaced, encoded, filename):
        with open(filename, 'w') as f:
            for l, c, e in zip(lines, replaced, encoded):
                s = '%s -> %s -> %s' % (l, c, ' '.join('%s/%s' % (d, c) for d, c in e))
                f.write(s.encode('utf-8'))
                f.write('\n')
        print 'Results written to %s' % filename

    def get_status(data, codemap):
        import regex
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

    ## Get data
    data  = utils.read_text('./_output/people-all-district.txt')
    lines = data.split('\n')
    #lines = data.split('\n')[500:600] # 경기 부천시원미구갑
    #lines = data.split('\n')[1200:1300] # 서울 노원구병

    ## Convert data
    converted = [convert(line) for line in lines]
    replaced = [replace(line, codemap) for line in converted]
    #encoded = [base.encoder(line, codemap) for line in replaced]
    #picked = [codepick(line) for line in encoded]
    marked = [markup(line, codemap) for line in replaced]

    ## Print results
    #for l, c, m in zip(lines, replaced, marked): print '%s -> %s -> %s' % (l, c, m)
    write_results(lines, replaced, marked, './_output/people-all-district-marked.txt')
    #for l, c, e, p in zip(lines, replaced, encoded, picked): print '%s -> %s -> %s -> %s' % (l, c, e, p)
    #get_status('\n'.join(replaced), codemap)
