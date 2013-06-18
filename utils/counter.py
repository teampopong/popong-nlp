#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter
import re
import regex    # http://www.regular-expressions.info/unicode.html

def prep_english(doc):
    # to lower case (그렇다면 약어는 어떻게?)
    doc = doc.lower()
    # TODO: remove stopwords
    return doc

def prep_korean(doc):
    # TODO: morpheme analysis, spacing
    # TODO: hanja transliteration?
    return re.sub(unichr(int('318d', 16)), ' ', doc)

def get_words(string, minlen=None):
    #TODO: if not unicode convert to unicode
    #string = string.decode('utf-8')
    string = prep_english(string)
    string = prep_korean(string)
    words = regex.findall(ur'[\p{Hangul}|\p{Latin}|\p{Han}]+', string)
    if minlen:
        words = [w for w in words if len(w) >= minlen]
    return words

def count(words, num=None):
    cnt = Counter(words)
    if num==None:
        return sorted(dict(cnt).items(), key=lambda x:x[1], reverse=True)
    else:
        return cnt.most_common(num)
