#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

# from __future__ import unicode_literals   # 'd3py' doesn't yet work with unicode!
import re
import numpy
import d3py, logging, pandas
from collections import Counter

from importer import get_filenames
import utils

INP = '/Users/lucypark/data/popong/people'
FIELD = 'education'

def get_files(filenames, fieldname):
    files = {}
    for f in filenames:
        num = utils.find_number(f)
        data = utils.read_json(f)
        field = [d[fieldname] for d in data]
        files[num] = field
    return files

def get_wordlengths(files):
    wlengths = []
    for f in files:
        wl = []
        for word in files[f]:
            wl.append(len(word))
        wlengths.append(wl)
    return wlengths

def main():
    fnames = get_filenames(INP, 'legislators'); print "Got filenames"
    files = get_files(fnames, FIELD); print "Got files"
    wlengths = get_wordlengths(files)
    wl = wlengths[0]

    logging.basicConfig(level=logging.DEBUG)
    for wl in wlengths:
        cnt, frq = numpy.histogram(wl)

        df = pandas.DataFrame ({
            # FIXME: '`'를 붙이지 않으면 "Uncaught TypeError: Object function h(a){return e(a)} has no method 'rangeBand'" 와 같은 에러 발생
            "num": [ '`' + str(i) for i in frq[:-1] ],
            "count": list(cnt),
        })

        i = 1
        # with d3py.PandasFigure(df) as p:
        p = d3py.PandasFigure(df)
        p += d3py.Bar(x="num", y="count", fill="MediumAquamarine")
        p += d3py.xAxis(x="num")
        p.show()

if __name__ == '__main__':
    main()
