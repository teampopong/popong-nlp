#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import re
import sys
import itertools
from collections import Counter

import regex
import pandas as pd

LEVELS = ['시', '군', '구']
SUBLEVELS = ['갑', '을']
STOPWORDS = ['제', '선거구', '지역구']
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
                encoded.append(codes[0])
            else:
                encoded.append(None)

    return encoded

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

    ## Print results
    #for l, c in zip(lines, replaced): print '%s -> %s' % (l, c)
    for l, c, e in zip(lines, replaced, encoded): print '%s -> %s -> %s' % (l, c, e)
    #write_results(lines, replaced, encoded, './_output/people-all-%s-encoded.txt' % opt)
    #get_status('\n'.join(replaced), codemap)

if __name__=='__main__':
    OPT = 'district'
    main(OPT)
