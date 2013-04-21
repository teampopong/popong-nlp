#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import time
from pprint import pprint

from utils import utils, counter, encoder
import settings as s

opts = {
    1: "Import data",
    2: "Babylon",
    3: "Bills",
    4: "Structurize",
    5: "Count"
}

def interface(opts):
    print "== Team POPONG NLP Library =="
    pprint(opts)

    opt = ''
    while(opt==''):
        opt = raw_input("Enter a number: ")

    print '=============================\n'
    return opt

def get_data(source=s.data["officials"],\
        fieldname=s.structurizer["fieldname"],\
        opt=s.structurizer["runopt"],\
        target=s.results["test"]):

    from utils.importer import data_importer

    data = data_importer(source, opt, fieldname)
    outf = "%s/people-%s-%s.txt" % (target, opt, fieldname)
    utils.write_text('\n'.join(data), outf)

    print 'Data written to ' + outf

def do_babylon(path=s.data["officials"],\
        fieldname=s.structurizer["fieldname"],\
        opt=s.structurizer["runopt"]):

    # FIX(lucypark): broken function
    from structurize.importer import data_importer
    from structurize.preprocessor import preprocessor
    from babylon.babylon import build_dict

    obj     = data_importer (path, opt, fieldname)
    items   = preprocessor (obj)
    dic     = build_dict (fieldname, items)

    return dic

def do_bills(path=s.data["bills"]):
    # TODO(lucypark): counter
    from bills.get import rawdata
    rawdata(path)

def do_structurize():
    # TODO: spacer()
    # TODO: calc_bigrams()

    pprint(dict(enumerate(s.feature, start=1)))
    opt = raw_input("Enter an option: ")

    if opt=='1':
        from structurize import district
        cm = encoder.get_codemap('region')
        district.main('district', cm)

    elif opt=='2':
        from structurize import education
        education.main()

    else:
        print "Warning: Check your option"
        sys.exit(2)

def do_count():
    #TODO(lucypark)
    return 'good'

def main():
    opt = interface(opts)

    if 0 < int(opt) < len(opts)+1:

        print "# " + opts[int(opt)]

        stime = time.time()

        if opt=='1': get_data()
        elif opt=='2': do_babylon()
        elif opt=='3': do_bills()
        elif opt=='4': do_structurize()
        elif opt=='5': do_count()
        else: raise

        etime = time.time()

    else:
        print "Warning: Input an integer from 1 to", len(opts)
        sys.exit(2)

    print "\n## Runtime: %f seconds" % (etime - stime)

if __name__ == "__main__":
    main()
