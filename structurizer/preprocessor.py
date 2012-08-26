#! /usr/bin/python3
# -*- coding: utf-8 -*-

import utils

def preprocessor(fieldlist):
    dic = utils.read_HHdic()

    fieldlist = nullify(fieldlist)
    fieldlist = remove_periods(fieldlist)
    fieldlist = trans_hanja(fieldlist, dic)
    #fieldlist = trans_roman(fieldlist)
    fieldlist = check_parenthesis(fieldlist)

    return list(fieldlist)

# nullify 'null', '미기재' cells
def _nullify(item):
    if item=='미기재':
        item = ''
    return item

def nullify(fieldlist):
    return (_nullify(item) for item in fieldlist)

# eliminate periods
def remove_periods(fieldlist):
    return (item.replace('.','') for item in fieldlist)

# transliterate hanja to hangul
def trans_hanja(fieldlist, dic):
    return (utils.hanja2hangul(dic, item) for item in fieldlist)

# check parentheses
def _check_parenthesis(item):
    s, e = item.find('('), item.find(')')
    inword, outword = item[s+1:e], item[2*s-e+1:s] 
    if inword==outword:
        item = item.replace(item[s:e+1],'')
    return item

def check_parenthesis(fieldlist):
    return (_check_parenthesis(item) for item in fieldlist)
