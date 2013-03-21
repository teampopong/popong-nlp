#! /usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json, regex

HH_DICTIONARY = '/home/e9t/data/hanja-hangul.json'

if __name__ == "__main__":
    with open(HH_DICTIONARY, 'r') as f:
        dic = json.load(f)

    text = '../_input/lorem-ipsum-multi.txt'
    with open(text, 'r') as f:
        chinese = regex.findall(ur'[\p{Han}]+', f.read().decode('utf-8'))

    import sys
    for word in chinese:
        hangul = ''.join([dic.get(char) for char in word])
        print word, hangul

    #print hanja2hangul('丁', dic=dic)
