#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json

HH_DICTIONARY = 'hanja-hangul.json'

def read_json(filename):
    with open(filename, 'r') as f:
        j = f.read()
        data = json.loads(j)
    return data 

def read_HHdic():
    dic = read_json(HH_DICTIONARY)
    return dic

def hanja2hangul(dic, string):
    s = ''
    for letter in string:
        s = s + dic.get(letter, letter)
    return s

def get_alpha(string):
    s = string.encode('utf-8')
    return s.isalpha()

if __name__ == '__main__':
    print(hanja2hangul('丁'))
