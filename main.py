#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import time
from pprint import pprint

from structurize.importer import data_importer
from structurize.preprocessor import preprocessor
from babylon.babylon import build_dict
from utils import counter
import settings

opts = {
    1: "Extract bills",
    2: "Structurize"
}

def interface(opts):
    print "== Team POPONG NLP Library =="
    pprint(opts)
    opt = raw_input("Enter a number: ")
    print '=============================\n'
    return opt

def do_bills(path=settings.data["bills"]):
    from bills.get import rawdata
    rawdata(path)

def do_structurize():
    INP = '/home/e9t/data/popong/people'
    OPTION = 'test'
    FIELDNAME = 'education' # 'education', 'party'
    stime = time.time()

    obj     = data_importer (INP, OPTION, FIELDNAME)
    items   = preprocessor (obj)
    dic     = build_dict (FIELDNAME, items)
    # TODO: spacer()
    # TODO: calc_bigrams()

    etime = time.time()

    print etime - stime, "seconds"

if __name__ == "__main__":
    import sys

    opt = interface(opts)
    print ">> " + opts[int(opt)]

    if opt=='1':
        do_bills()
    elif opt=='2':
        do_structurize()
    else:
        print "! Warning: Input a given number"
        sys.exit(2)
