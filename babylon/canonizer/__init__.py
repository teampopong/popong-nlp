#! /usr/bin/python

import wikipedia

def canonize(string):
    return wikipedia.canonical_name(string.encode('utf-8'))
