#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys
import time
from pprint import pprint

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.append(parentdir)
from utils import utils, counter, encoder
import settings as s


def interface():
    print "== Team POPONG NLP Library ==\n"
    pprint(s.main['opts'])

    opt = ''
    while(opt==''):
        opt = raw_input("\nEnter a number: ")

    print '=============================\n'
    return opt

def get_data(source=s.data["officials"],\
        fieldname=s.importer["fieldname"],\
        opt=s.importer["runopt"],\
        target=s.results["test"]):

    from utils.importer import data_importer

    data = data_importer(source, opt, fieldname)
    outf = "%s/people-%s-%s.txt" % (target, opt, fieldname)
    utils.write_text('\n'.join(data), outf)

    print 'Data written to ' + outf

def do_babylon(fieldname=s.babylon["fieldname"], filename=s.babylon["input_file"]):
    from babylon.babylon import build_alias_dict
    items = utils.read_text(filename)
    build_alias_dict(fieldname, items)

def do_bills(path=s.data["bills"]):
    # TODO(lucypark): counter
    from bills.get import rawdata
    rawdata(path)

def do_structurize():
    # TODO(lucypark): calc_bigrams()

    pprint(dict(enumerate(s.features, start=1)))
    opt = raw_input("Enter an option: ")

    if opt=='1':
        from structurizer import district
        cm = encoder.get_codemap('region')
        district.main(cm)

    elif opt=='2':
        from structurizer import education
        cm = encoder.get_codemap('highereducation')
        education.main(cm)

    else:
        print "Warning: Check your option"
        sys.exit(2)

def do_count():
    #TODO(lucypark)
    return 'good'

def main():
    opt = int(interface())
    opts = s.main['opts']

    if 0 < int(opt) < len(opts)+1:
        print "# " + opts[opt]
        stime = time.time()
        eval(opts[opt])()
        etime = time.time()

    else:
        print "Warning: Input an integer from 1 to", len(opts)
        sys.exit(2)

    print "\n## Runtime: %f seconds" % (etime - stime)

if __name__ == "__main__":
    main()
