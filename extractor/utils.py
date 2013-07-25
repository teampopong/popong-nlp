#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import regex
import json

import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tag.stanford import StanfordTagger

def write_json(data, filename, opt=None):
    with open(filename, 'w') as f:
        if opt=='compact':
            json.dump(data, f)
        else:
            json.dump(data, f, indent=2)

def get_words(document, stopwords):
    ps = PorterStemmer()
    words = regex.findall(ur'[\p{Hangul}|\p{Latin}|\p{Han}]+', document.lower())
    words = [ps.stem(word) for word in words if word not in stopwords]
    words = [word for word in words if len(word)>1]
    #words = [word for word, tag in nltk.pos_tag(words) if tag!='NN']
    return words

def chk_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
