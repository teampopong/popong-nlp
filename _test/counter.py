#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

# from __future__ import unicode_literals   # 'd3py' doesn't yet work with unicode!
import re, csv
from collections import Counter

from importer import get_filenames
import utils

INP = '/Users/lucypark/data/popong/people'
FIELD = 'education'

def get_files(filenames, fieldname):
    files = []
    for f in filenames:
        num = utils.find_number(f)
        data = utils.read_json(f)
        field = [d[fieldname] for d in data]
        files.append(field)
    return files

def parse(f):
    return [i for item in f for i in filter(None, re.split('[ \(\)]', item))]

def wordlengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

def count(lengths):
    c = Counter(lengths)
    return dict(c)

def tablarize(counts):
    ncols = max([i for c in counts for i in c.keys()])
    table = []
    for c in counts:
        arr = [0] * ncols
        for i in c.items():
            arr[i[0]-1] = i[1]
        print arr
        table.append(arr)
    return table, ncols

def main():
    fnames = get_filenames(INP, 'legislators'); print "Got filenames"
    files = get_files(fnames, FIELD); print "Got files"

    words = [parse(f) for f in files]
    lengths = [wordlengths(w) for w in words]
    counts = [count(l) for l in lengths]
    table, ncols = tablarize(counts)

    headers = ['no'] + range(1,ncols+1)
    table = [[table.index(t)+1] + t for t in table]
    utils.write_csv('count.csv', table, headers)

if __name__ == '__main__':
    main()
