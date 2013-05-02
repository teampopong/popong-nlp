#! /usr/bin/python3
# -*- coding: utf=8 -*-

from ..babylon import canonizer
from ..utils import utils
from .. import settings as s
from . import base

STARTS = s.education['countries']
ENDS = s.education['statuses']
STOPWORDS = s.education['stopwords']
ABBREVS = s.education['abbrevs']
ALIASES = s.education['aliases']
TERMS = ALIASES.keys() + ALIASES.values()
for i in s.education['to_ignore']: TERMS.remove(i)

def reverse_pop(word):
    popped = []
    for j in range(len(word), -1, -1):
        challenger, remainder = word[:j], word[j:]
        if challenger in TERMS:
            if word[j]==u'원':
                popped.append(word[:j+1])
                popped.append(word[j+1:])
            else:
                popped.append(challenger)
                popped.append(remainder)
            break
        if j==0:
            popped.append(word)
    return popped

def spacer(line):
    words = line.split()
    spaced = []
    for word in words:
        if word in ENDS+TERMS:
            spaced.append(word)
        else:
            spaced.extend(reverse_pop(word))
    return ' '.join(spaced)

def convert(line):
    endsplit = base.endsplitter(line, ENDS)
    startsplit = base.startsplitter(endsplit, STARTS)
    words = base.wordify(startsplit)
    erased = base.eraser(words, STOPWORDS)
    canonized = base.canonizer(erased, ABBREVS)
    canonized = base.canonizer(canonized, ALIASES)
    return ' '.join(canonized)

def struct(string, codemap):
    print 'tba'

def markup(string, codemap):

    def encode(token):
        codes = codemap.get(token)
        if type(codes)==list:
            return codes[0]
        else:
            return None

    converted = convert(string)
    spaced = spacer(converted)
    final = convert(spaced)

    tokens = final.split()
    encoded = (encode(token) for token in tokens)
    return zip(tokens, encoded)
