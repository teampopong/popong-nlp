#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import json
import os
from subprocess import PIPE, Popen

from ..utils.counter import get_words, count
from ..utils.utils import cnt2ratio, chunk_list, get_groups


currentdir = os.path.dirname(os.path.abspath(__file__))
rpath = os.path.join(currentdir, 'nouns.r')


def get_nouns(string):
    nouns = []
    with open(os.devnull, 'w') as DEVNULL:
        p = Popen([rpath], stdin=PIPE, stdout=PIPE, stderr=DEVNULL)
        (result, _) = p.communicate(string + '\n')
        nouns = result.split()
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
