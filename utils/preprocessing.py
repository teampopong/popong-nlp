#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

def english(doc):
    # to lower case (그렇다면 약어는 어떻게?)
    doc = doc.lower()
    # TODO: remove stopwords
    return doc

def korean(doc):
    # TODO: morpheme analysis, spacing
    # TODO: hanja transliteration?
    return doc
