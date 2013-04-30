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
    split = base.endsplitter(line, ENDS)
    words = base.wordify(split)
    erased = base.eraser(words, STOPWORDS)
    canonized = base.canonizer(erased, ALIASES)
    return ' '.join(canonized)

def codepick(codes):
    codes = filter(None, codes)
    maxlen = max(len(c) for c in codes)
    return [str(c) for c in codes if len(c)==maxlen]

def markup(string, codemap):
    converted = convert(string)
    spaced = base.spacer(converted, codemap, ENDS)
    encoded = base.encoder(spaced, codemap)

    tokens = spaced.split()
    if len(tokens)==len(encoded):
        return zip(tokens, encoded)
    else:
        print 'This cannot be happening!'
        sys.exit(2)

def struct(string, codemap):
    converted = convert(string)
    spaced = base.spacer(converted, codemap, ENDS)
    encoded = base.encoder(spaced, codemap)
    picked = codepick(encoded)
    return picked


def main(codemap):

    def write_results(lines, spaced, encoded, filename):
        with open(filename, 'w') as f:
            for l, c, e in zip(lines, spaced, encoded):
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
    spaced = [base.spacer(line, codemap, ENDS) for line in converted]
    #encoded = [base.encoder(line, codemap) for line in spaced]
    #picked = [codepick(line) for line in encoded]
    marked = [markup(line, codemap) for line in spaced]

    ## Print results
    for l, c, m in zip(lines, spaced, marked): print '%s -> %s -> %s' % (l, c, m)
    #write_results(lines, spaced, marked, './_output/people-all-district-marked.txt')
    #for l, c, e, p in zip(lines, spaced, encoded, picked): print '%s -> %s -> %s -> %s' % (l, c, e, p)
    #get_status('\n'.join(spaced), codemap)
