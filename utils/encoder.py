#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import csv
import pandas as pd

def get_codemap(opt, lang='ko'):
    #TODO: change absolute path
    cb = pd.read_csv('/home/e9t/dev/popong/nlp/_input/cb-%s.csv' % opt,
            encoding='utf-8', dtype={'code': object})
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

if __name__=='__main__':
    cm = get_codemap('region')
    #for k, v in cm.items(): print '%s %s' % (k, v)
    print encode(u'서울특별시', cm)
