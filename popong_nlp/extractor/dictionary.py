#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import regex
from collections import Counter
from gensim import corpora

from .utils import write_json, chk_dir
from ..utils.counter import get_words

def make_dictionary(documents, stoplist, dictfile, jsonfile, option='batch'):

    if option=='batch':
        texts = [get_words(document, stoplist) for document in documents]
        tokens = [k for k, v in list(Counter(sum(texts, [])).items()) if v>1]
        texts = [[word for word in text if word in tokens] for text in texts]
        dictionary = corpora.Dictionary(texts)

    elif option=='online':
        words = [[word for word in regex.findall(r'[\p{Hangul}|\p{Latin}|\p{Han}]+', doc.lower()) if len(word)>1] for doc in documents]
        dictionary = corpora.Dictionary(words)

        stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
                if stopword in dictionary.token2id]
        once_ids = [tokenid for tokenid, docfreq in list(dictionary.dfs.items())\
                if docfreq==1]

        dictionary.filter_tokens(stop_ids + once_ids)
        dictionary.compactify()

    else:
        dictionary = None

    dictionary.save(dictfile)
    write_json(dictionary.token2id, jsonfile)

    return dictionary
