#! /usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json, regex

HH_DICTIONARY = '/home/e9t/data/hanja-hangul.json'

def translit(string):
    with open(HH_DICTIONARY, 'r') as f:
        dic = json.load(f)

    return ''.join(dic.get(char) for char in string)

if __name__ == "__main__":
    print translit('新新新新新')
