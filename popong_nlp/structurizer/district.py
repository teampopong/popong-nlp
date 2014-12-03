#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
import itertools
from collections import Counter

from .. import settings as s
from ..utils import utils
from . import base

ENDS = s.district['sublevels']
STOPWORDS = s.district['stopwords']
ALIASES = s.district['aliases']

def canonizer(words, aliases):
    return (aliases.get(word, word) for word in words)

def convert(line):
    split = base.endsplitter(line, ENDS)
    words = base.wordify(split)
    erased = base.eraser(words, STOPWORDS)
    canonized = canonizer(erased, ALIASES)
    return ' '.join(canonized)

def spacer(line, codemap, ignore=[]):

    def pop(word, codemap):
        # FIX: 부산 중동구 -> 부산광역시 중동
        i = 0
        popped = []
        for j in range(1, len(word)+1):
            challenger = codemap.get(word[i:j])
            if challenger!=None:
                popped.append(word[i:j])
                i = j
            if j==len(word) and not popped:
                popped.append(word)
        return ' '.join(popped)

    spaced = []
    for word in line.split():
        if word in ignore or codemap.get(word):
            spaced.append(word)
        else:
            spaced.append(pop(word, codemap))
    return ' '.join(spaced)

def encoder(line, codemap):
    encoded = []
    words = line.split()

    for i, word in enumerate(words):
        codes = codemap.get(word)
        if i==0:
            if codes and len(codes)==1:
                code = codes[0]
            else:
                code = None
        else:
            if codes:
                subcodes = [c for c in codes if c.startswith(encoded[0])]
                if len(subcodes)!=0:
                    code = subcodes[0]
                else:
                    code = None
            else:
                code = None
        encoded.append(code)

    return encoded

def codepick(codes):
    codes = filter(None, codes)
    maxlen = max(len(c) for c in codes)
    return [str(c) for c in codes if len(c)==maxlen]

def get_unique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def markup(string, codemap):
    converted = convert(string)
    spaced = spacer(converted, codemap, ENDS)
    encoded = encoder(spaced, codemap)

    tokens = spaced.split()
    if len(tokens)==len(encoded):
        marked = zip(tokens, encoded)
    else:
        raise Exception('This cannot be happening!')

    unique = get_unique(marked)
    return unique

def struct(string, codemap):
    converted = convert(string)
    spaced = spacer(converted, codemap, ENDS)
    encoded = encoder(spaced, codemap)
    picked = codepick(encoded)
    return picked
