#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import regex

def endsplitter(line, ends):
    for e in ends:
        if line.endswith(e):
            c = len(e)
            line = '%s %s' % (line[:-c], line[-c:])
    return line

def startsplitter(line, starts):
    for s in starts:
        if line.startswith(s):
            c = len(s)
            line = '%s %s' % (line[:c], line[c:])
    return line

def wordify(line):
    return regex.findall(ur'[\p{Hangul}|\p{Number}]+', line)

def eraser(words, stopwords):

    def erase(word):
        if any(word==stopword for stopword in stopwords):
            word = ''
        return word

    return filter(None, (erase(word) for word in words))

def canonizer(words, aliases):
    return (aliases.get(word, word) for word in words)

def pop(word, codemap):
    # FIX: 부산 중동구 -> 부산광역시 중동
    i = 0
    popped = []
    for j in range(len(word)+1):
        challenger = codemap.get(word[i:j])
        if challenger!=None:
            popped.append(word[i:j])
            i = j
    return ' '.join(popped)

def encoder(line, codemap):
    encoded = []
    words = line.split()

    for i, word in enumerate(words):
        codes = codemap.get(word)
        if i==0:
            if len(codes)==1:
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
