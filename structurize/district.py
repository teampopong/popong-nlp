#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import itertools
from collections import Counter

import regex
import pandas as pd

LEVELS = ['시', '군', '구']
SUBLEVELS = ['갑', '을']

ALIASES = {
    '서울': '서울특별시',
    '대전': '대전광역시',
    '대구': '대구광역시',
    '부산': '부산광역시',
    '울산': '울산광역시',
    '광주': '광주광역시',
    '인천': '인천광역시',
    '제주': '제주특별자치도',
    '경기': '경기도',
    '강원': '강원도',
    '충북': '충청북도',
    '충남': '충청남도',
    '전남': '전라남도',
    '전북': '전라북도',
    '경남': '경상남도',
    '경북': '경상북도'
}

STOPWORDS = ['제', '선거구', '지역구']

def read_data(data):
    with open(data, 'r') as f:
        return f.read().decode('utf-8')

def spacer(line, ends):
    if any(line.endswith(e) for e in ends):
        line = '%s %s' % (line[:-1], line[-1])
    return line

def eraser(word, stopwords):
    if any(word==stopword for stopword in stopwords):
        word = ''
    return word

def convert(line, ends):

    spaced = spacer(line, ends)
    words = regex.findall(ur'\p{Hangul}+', spaced)

    erased = filter(None, (eraser(word, STOPWORDS) for word in words))
    aliased = (ALIASES.get(word, word) for word in erased)

    return ' '.join(aliased)

def encode(line, codemap):
    # TODO: 지역의 hierarchy를 따라 searching하도록 ('서울특별시 중구'같은 애들때문)
    encoded = []
    for i, word in enumerate(line.split()):
        code = codemap.get(word)
        encoded.append(code)

        if i==0 and code!=None:
            codemap = {k:v for k,v in codemap.iteritems() if v.startswith(code)}
            for k, v in codemap.items(): print k, v
            import sys
            sys.exit(2)
    return encoded

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

def replace(line, codemap):
    replaced = []
    for word in line.split():
        if word in SUBLEVELS or codemap.get(word):
            replaced.append(word)
        else:
            replaced.append(pop(word, codemap))
    return ' '.join(replaced)

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
    lines = data.split('\n')

    ## Convert data
    ends = [''.join(i) for i in list(itertools.product(LEVELS, SUBLEVELS))]

    converted = [convert(line, ends) for line in lines]
    replaced = [replace(line, codemap) for line in converted]
    encoded = [encode(line, codemap) for line in replaced]

    ## Print results
    for l, c, e in zip(lines, replaced, encoded): print '%s -> %s -> %s' % (l, c, e)
    #write_results(lines, replaced, encoded, './_output/people-all-%s-encoded.txt' % opt)
    get_status('\n'.join(replaced), codemap)

if __name__=='__main__':
    OPT = 'district'
    main(OPT)
