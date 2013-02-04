#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re
import json
import codecs
import csv
from collections import Counter

HH_DICTIONARY = 'dict/hanja-hangul.json'

def read_json(filename):
    with open(filename, 'r') as f:
        j = f.read()
        data = json.loads(j)
    return data

def read_text(filename):
    with open(filename, 'r') as f:
        return f.read()

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

def write_csv(filename, data, headers=None):
    with open(filename, 'wb') as f:
        w = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if headers:
            w.writerow(headers)
        for d in data:
            w.writerow(d)

def print_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def print_text(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

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

def flatten_list(listoflist):
    def str2list(item):
        if isinstance(item, str):
            item = [item]
        else:
            pass
        return item

    listoflist = [str2list(item) for item in listoflist]
    return [item for sublist in listoflist for item in sublist]

def count(text):
    cnt = Counter()
    for word in text:
        cnt[word] += 1
    return cnt

def textify(obj, opt=''):
    if isinstance(obj, list):
        if opt=='stag':
            return '<s> ' + ' </s>\n<s> '.join(obj) + ' </s>'
        elif opt=='filter':
            obj = filter(None, obj)
            return '\n'.join(obj)
        else:
            return '\n'.join(obj)
    else:
        raise ValueError

def find_number(s):
    return int(re.findall(r'[0-9]+', s)[0])

if __name__ == '__main__':
    print(hanja2hangul('丁'))
