#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import json
import os

import konlpy

from ..utils.counter import get_words, count
from ..utils.utils import cnt2ratio, chunk_list, get_groups

from .. import settings as s


currentdir = os.path.dirname(os.path.abspath(__file__))
rpath = os.path.join(currentdir, 'nouns.r')

with open(s.data['stopwords_ko'], 'r') as f:
    stops_ko = filter(None, f.read().decode('utf-8').split('\n'))

def remove_stopwords(nouns):
    for s in stops_ko:
        nouns = filter(lambda n: n!=s, nouns)
    return nouns

def select(cnt, minlen=0, mincnt=0):
    lengthy = (c for c in cnt if len(c[0])>=minlen)
    return [l for l in lengthy if l[1]>mincnt]

def keywords_from_string(string, h,\
        maxnum=5, minlen=2, mincnt=5, minratio=0.03, groupsize=1000):

    # FIXME: generalize this hotfix for empty files w/ mostly line carriages
    if len(string) < 1000:
        return []

    words = get_words(string, minlen)
    group = [chunk_list(words, idx) for idx in get_groups(len(words), groupsize)]
    # FIXME: enhance hannanum to handle input arrays of size > 10000
    nouns = h.nouns('\r'.join(group)[:10000])
    nouns = remove_stopwords(nouns)
    cnt = count(nouns)
    selected = select(cnt, minlen, mincnt)
    ratio = cnt2ratio(selected, len(nouns), minratio)

    if len(ratio)>maxnum:
        return ratio[:maxnum]

    return ratio

def keywords(f, h,\
        maxnum=5, minlen=2, mincnt=5, minratio=0.03, groupsize=1000):
    # h: KoNLPy Hannanum instance

    return keywords_from_string(f.read().decode('utf-8'), h,\
                maxnum, minlen, mincnt, minratio, groupsize)
