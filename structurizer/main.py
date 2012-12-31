#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys, time

from importer import data_importer
from preprocessor import preprocessor
from babylon import build_dict
import utils

INP = '../../crawlers/election_commission/data/'
OPTION = 'all'
FIELDNAME = 'party' # 'education', 'party'

def main():
    stime = time.time()

    obj     = data_importer (INP, OPTION, FIELDNAME)
    items   = preprocessor (obj)
    dic     = build_dict (FIELDNAME, items)
    # TODO: spacer()
    # TODO: calc_bigrams()

    etime = time.time()

    print etime - stime, "seconds"

main()
