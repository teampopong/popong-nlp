#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter

import konlpy
import regex

def get_document(filename):
    with open(filename, 'r') as f:
        return f.read().decode('utf-8')

def sanitize_noun(noun):
    return regex.findall(ur'[\p{Hangul}|\p{Latin}|\p{Han}]+', noun)

def filter_noun(noun):
    return len(noun) > 1

if __name__=='__main__':
    h = konlpy.Hannanum()

    fn = '/home/e9t/data/popong/bill-docs/txt/19/1902751.txt'
    doc = get_document(fn)

    nouns = h.nouns(doc)
    # TODO: translit
    nouns = sum([sanitize_noun(n) for n in nouns], [])
    nouns = [n for n in nouns if filter_noun(n)]
    c = dict(Counter(nouns))
    for k, v in sorted(c.items(), key=lambda x: x[1]):
        print k, v


