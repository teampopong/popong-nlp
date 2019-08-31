#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import csv
import pandas as pd


from .. import settings as s

def get_codemap(opt, lang='ko'):
    path = s.codebook[opt]

    cb = pd.read_csv(path, encoding='utf-8', dtype={'code': object})
    cb = cb.dropna()
    cm = {}

    for d, c in zip(cb[lang], cb['code']):
        if cm.get(d)==None:
            cm[d] = [c]
        else:
            cm[d].append(c)
    return cm

def encode(word, codemap):
    try:
        return codemap[word]
    except:
        return None
