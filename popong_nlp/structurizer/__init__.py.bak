#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os

from ..utils import encoder
from .. import settings as s
import district
import education

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CM_REGION = encoder.get_codemap('region')
CM_EDUCATION = encoder.get_codemap('education')

def structurize(string, _type):
    if _type in ['district','address']:
        return district.struct(string, CM_REGION)
    elif _type=='education':
        return education.struct(string, CM_EDUCATION)
    else:
        raise Exception('Invalid input')

def markup(string, _type):
    if _type in ['district','address']:
        return district.markup(string, CM_REGION)
    elif _type=='education':
        return education.markup(string, CM_EDUCATION)
    else:
        raise Exception('Invalid input')


if __name__=='__main__':
    print structurize('district', u'서울 관악구 봉천동')
