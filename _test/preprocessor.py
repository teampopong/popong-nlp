#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
from utils import utils

def preprocessor(fieldlist):
    dic = utils.read_HHdic()

    #fieldlist = unicodify(fieldlist)
    fieldlist = nullify(fieldlist)
    fieldlist = remove_commas(fieldlist)
    fieldlist = remove_parentheses(fieldlist)
    fieldlist = trans_hanja(fieldlist, dic)
    #fieldlist = trans_roman(fieldlist)
    #fieldlist = check_parenthesis(fieldlist)
    return list(fieldlist)

# string to unicode
def _unicodify(item, encoding='utf-8'):
    if isinstance(item, basestring):
        if not isinstance(item, unicode):
            item = unicode(item, encoding)
    return item

def unicodify(fieldlist):
    return (_unicodify(item) for item in fieldlist)

# nullify 'null', '미기재' cells
def _nullify(item):
    if item==u'미기재':
        item = ''
    return item

def nullify(fieldlist):
    return (_nullify(item) for item in fieldlist)

# eliminate commas
def remove_commas(fieldlist):
    return (item.replace(',','') for item in fieldlist)

# eliminate parentheses
def remove_parentheses(fieldlist):
    return (re.sub(r'[\(\)]', ' ', item) for item in fieldlist)

# transliterate hanja to hangul
def trans_hanja(fieldlist, dic):
    return (utils.hanja2hangul(dic, item) for item in fieldlist)

# check word in parentheses and delete if repetitive
def _check_parenthesis(item):
    s, e = item.find('('), item.find(')')

    if s==-1 and e==-1:
        pass
    else:
        inword = item[s+1:e]
        if item[s-1]==u' ':
            outword = item[2*s-e:s-1]
        else:
            outword = item[2*s-e+1:s]
        if inword==outword:
            item = item.replace(item[s:e+1],'')
    return item

def check_parenthesis(fieldlist):
    return (_check_parenthesis(item) for item in fieldlist)
