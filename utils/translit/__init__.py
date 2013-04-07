#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import ko2en
import cn2ko

def translit(string, _from, _to, _type=None):

    if _from=='ko'and _to=='en':

        if _type=='name':
            return ko2en.name2eng(string)
        elif _type=='party':
            return ko2en.party2eng(string)
        elif _type==None:
            return ko2en.romanize(string)
        else:
            print 'Warning: Invalid type (name, party)'
            sys.exit(2)

    elif _from=='cn' and _to=='ko':
        return cn2ko.translit(string)

    else:
        print 'Warning: Invalid mapping (ko2en, cn2ko)'
        sys.exit(2)

if __name__=='__main__':
    print translit('박근혜', 'ko', 'en', 'name')
    print translit('한나라당', 'ko', 'en', 'party')
    print translit('안녕하세요', 'ko', 'en')
    print translit('丁新闻', 'cn', 'ko')
