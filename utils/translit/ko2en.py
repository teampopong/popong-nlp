#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os.path
import json
from unidecode import unidecode

from base import force_unicode

basepath = os.path.dirname(os.path.realpath(__file__))

def get_lastnames(filename):
    with open(os.path.join(basepath, filename), 'r') as f:
        return json.load(f)

@force_unicode
def romanize(txt):
    '''한글을 영문으로 변환'''

    return unidecode(txt)
    return translit.romanize(txt.encode('utf-8')).decode('utf-8')

@force_unicode
def firstname2eng(syls):
    '''한글 이름을 영문으로 변환'''

    syls = (romanize(syl) for syl in syls)
    firstname_en = '-'.join(syls)
    return firstname_en.capitalize()

@force_unicode
def lastname2eng(syl):
    '''한글 성을 영문으로 변환'''

    # TODO: 영문 성씨 순위 데이터 구해서 높은 percentage의 성씨로 변환
    lastnames = get_lastnames('lastnames.json')
    lastname_en = lastnames.get(syl, romanize(syl))
    return lastname_en.capitalize()

@force_unicode
def name2eng(name):
    last_syl, first_syls = name[0], name[1:]
    lastname, firstname = lastname2eng(last_syl), firstname2eng(first_syls)
    name_en =  u'%s %s' % (lastname, firstname)
    return name_en

@force_unicode
def party2eng(party):
    if party == u'무소속':
        return u'independent'

    if party.endswith(u'당'):
        party = '%s Party' % party[:-1]

    return romanize(party).title()

if __name__=='__main__':
    print name2eng('박근혜')
    print party2eng('새누리당')
