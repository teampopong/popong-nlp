#! /usr/bin/python3
# -*- coding: utf-8 -*-

def _wordify(item, word):
    s = item.find(word)
    if s > 0:
        f = s + len(word)
        item = ' '.join([item[:s], item[s:f], item[f:]])
    return item

def wordify(fieldlist, words):
    return (_wordify(item, word) for word in words for item in fieldlist)
