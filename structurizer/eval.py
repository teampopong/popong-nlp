#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

from pprint import pprint 
import utils

    
def oov_rate(words, entries):
    """
    Calculates OOV(out of vocabulary) rate.
    """
    words, entries = set(words), set(entries)
    diff = words.difference(entries)

    nw = len(words)
    ne = len(entries)
    nd = len(diff)
    
    oovr = nd/float(nw)
    return oovr

def perplexity():
    """
    perplexity: measure for predictive power
    """
    # TODO: calculate perplexity
    return p

if __name__ == '__main__':
    FIELDNAME = 'party'
    WORDSET = 'dict/%s-wordlist.json' % (FIELDNAME)
    DIC = 'dict/%s.json' % (FIELDNAME)

    with open(WORDSET, 'r') as f:
        words = json.load(f)

    with open(DIC, 'r') as f:
        dic = json.load(f)

    oovr = oov_rate(words, dic.values())
    print oovr
    #p = perplexity()
