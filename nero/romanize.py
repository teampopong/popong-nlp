#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from hangul import translit
import utils

def name2eng(name):
    syls = utils.getsyls(name)
    last_syl = syls[0]
    first_syls = syls[1:]
    name_en =  utils.firstname2eng(first_syls)\
            + ' ' + utils.lastname2eng(last_syl)
    return name_en

def party2eng(party):
    if party == '무소속':
        party = 'non-party'
    else: 
        if party.endswith('당'):
            party = translit.romanize(party[:-3]) + ' Party'
        else:
            party = translit.romanize(party)
    return capname(party)
