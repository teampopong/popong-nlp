#! /usr/bin/python

from __future__ import absolute_import
#! /usr/bin/python

from . import wikipedia

def canonize(string):
    return wikipedia.canonical_name(string.encode('utf-8'))
