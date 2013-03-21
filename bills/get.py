#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from glob import glob

def rawdata(path):
    data = glob("%s/*.txt" % path)
    for d in data:
        print d
