#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from builtins import chr
from collections import Counter
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import regex    # http://www.regular-expressions.info/unicode.html


def prep_english(doc):
    # to lower case (그렇다면 약어는 어떻게?)
    doc = doc.lower()
    return doc

def prep_korean(doc):
    # TODO: morpheme analysis, spacing
    # TODO: hanja transliteration?
    return re.sub( '[%s|%s]' % (chr(int('318d', 16)), chr(int('ff65', 16))), ' ', doc)

def post_english(word):
    ps = PorterStemmer()
    stops = stopwords.words('english')
    word = ps.stem(word) if word not in stops else ''
    #word = word if nltk.pos_tag(words)[1]=='NN' else ''
    return word

def get_words(string, minlen=None):
    #TODO: if not unicode convert to unicode
    #string = string.decode('utf-8')
    string = prep_english(string)
    string = prep_korean(string)
    words = regex.findall(r'[\p{Hangul}|\p{Latin}|\p{Han}]+', string)
    words = [post_english(word) for word in words]
    if minlen:
        words = [w for w in words if len(w) >= minlen]
    return words

def count(words, num=None):
    cnt = Counter(words)
    if num==None:
        return sorted(list(dict(cnt).items()), key=lambda x:x[1], reverse=True)
    else:
        return cnt.most_common(num)
