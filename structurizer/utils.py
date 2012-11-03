#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
import codecs

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

def print_csv(filename, data):
    with open(filename, 'w') as f:
        for d in data:
            f.write(','.join(d))
            f.write('\n')

def prettify(wordlist):
    def right_align(_list, max_length):
        tmp_list = []
        for i in range(max_length - len(_list)):
            tmp_list.append('')
        aligned = tmp_list + _list
        return aligned 

    max_length = max(len(i) for i in wordlist)
    wordlist = [right_align(l, max_length) for l in wordlist]
    return wordlist

if __name__ == '__main__':
    print(hanja2hangul('丁'))
