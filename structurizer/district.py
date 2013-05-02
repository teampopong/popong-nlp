#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
import sys
import itertools
from collections import Counter

import pandas as pd

from .. import settings as s
from ..utils import utils
from . import base

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
