#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import json

from nlp.utils.counter import get_words, count
from nlp.utils.utils import cnt2ratio, chunk_list, get_groups

def get_nouns(string):
    #TODO(lucypark): change os.system to popen
    '''
    from subprocess import PIPE, Popen
    p = Popen(['./nlp/extractor/nouns.r'], stdin=PIPE, stdout=PIPE)
    print p.communicate(' '.join(words).encode('utf-8'))
    '''
    os.system('echo %s | ./nlp/extractor/nouns.r 2> /dev/null' % string)
    with open('nouns.txt', 'r') as f:
        nouns = f.read().decode('utf-8').split()
    return nouns

def select(cnt, minlen=0, mincnt=0):
    lengthy = (c for c in cnt if len(c[0])>=minlen)
    return [l for l in lengthy if l[1]>mincnt]

def keywords_from_string(string,\
        maxnum=5, minlen=2, mincnt=5, minratio=0.03, groupsize=1000):

    words = get_words(string, minlen)
    nouns = get_nouns('\r'.join(\
                chunk_list(words, idx)\
                for idx in get_groups(len(words), groupsize)).encode('utf-8'))
    cnt = count(nouns)
    selected = select(cnt, minlen, mincnt)
    ratio = cnt2ratio(selected, len(nouns), minratio)

    if len(ratio)>maxnum:
        return ratio[:maxnum]

    return ratio

def keywords(f,\
        maxnum=5, minlen=2, mincnt=5, minratio=0.03, groupsize=1000):

    return keywords_from_string(f.read().decode('utf-8'),\
                maxnum, minlen, mincnt, minratio, groupsize)
