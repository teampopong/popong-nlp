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
    return regex.findall(ur'[\p{Hangul}|\p{Latin}|\p{Number}]+', line)

def eraser(words, stopwords):

    def erase(word):
        if any(word==stopword for stopword in stopwords):
            word = ''
        return word

    return filter(None, (erase(word) for word in words))
