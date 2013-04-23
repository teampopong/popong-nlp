#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.append(parentdir)
from utils import encoder
import district

def structurizer(_type, string):
    if _type=='district':
        cm = encoder.get_codemap('region')
        district.struct(string, cm)
    else:
        print 'Warning: Invalid input'
        sys.exit(2)

if __name__=='__main__':
    print structurizer('district', u'서울 관악구 봉천동')
