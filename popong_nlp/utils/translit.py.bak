#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import re
from unidecode import unidecode

from .. import settings as s
from .utils import read_json

def _name2eng(name):
    #TODO(lucypark): Change to class
    last_syl, first_syls = name[0], name[1:]

    # Convert lastname
    lastnames = read_json(s.data["lastnames"])
    lastname_en = lastnames.get(last_syl, unidecode(last_syl)).title()

    # Convert firstname
    firstname_en = '-'.join(unidecode(syl) for syl in first_syls).title()

    name_en =  u'%s, %s' % (lastname_en, firstname_en)
    return name_en

def _party2eng(party):
    if party==u'무소속':
        return u'independent'

    else:
        if party.endswith(u'당'):
            party = '%s Party' % party[:-1]
        return unidecode(party).title()

def ko2en(string, _type):
    if _type=='name':
        return _name2eng(string)
    elif _type=='shortname':
        return shorten(_name2eng(string))
    elif _type=='party':
        return _party2eng(string)
    elif _type=='school':
        # TODO(cornchz): implement
        return unidecode(string)
    elif _type==None:
        return unidecode(string)
    else:
        raise Exception('Warning: Unknown type')

def cn2ko(string):
    with open(s.data["HHdic"], 'r') as f:
        dic = json.load(f)
    return ''.join(dic.get(char) for char in string)

def shorten(name_en):
    s = re.split('[,-]', name_en)
    return '%s, %s' % (s[0], ''.join(t.strip()[0] for t in s[1:]))

def translit(string, _from, _to, _type=None):
    if _from=='ko'and _to=='en':
        return ko2en(string, _type)
    elif _from=='cn' and _to=='ko':
        return cn2ko(string)
    else:
        raise Exception('Warning: Invalid mapping (ko2en, cn2ko)')

if __name__=='__main__':
    print translit('박근혜', 'ko', 'en', 'name')
    print translit('한나라당', 'ko', 'en', 'party')
    print translit('안녕하세요', 'ko', 'en')
    print translit('丁新闻', 'cn', 'ko')
