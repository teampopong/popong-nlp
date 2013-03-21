#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from base import firstname2eng, force_unicode, lastname2eng, romanize

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
