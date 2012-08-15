#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json

HH_DICTIONARY = 'hanja-hangul.json'

def read_json(filename):
    with open(filename, 'r') as f:
        j = f.read()
        data = json.loads(j)
    return data 

def hanja2hangul(hanja):
    dic = read_json(HH_DICTIONARY)
    hangul = dic[hanja]
    return hangul

if __name__ == '__main__':
    print(hanja2hangul('丁'))
