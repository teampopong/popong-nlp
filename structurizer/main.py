#! /usr/bin/python3
# -*- coding: utf-8 -*-

from base import * 
from utils import *
from importer import *

from pprint import pprint 

opt = 'all'
fieldname = 'education'
nprint = 30

filenames = get_filenames('../../crawlers/election_commission/data/', opt)
fieldlist = get_rawlist(filenames, fieldname)
wordlist = list_parser(fieldlist)
wordlist = list(wordlist)
wordlist = flatten_list(wordlist)
dic = read_HHdic()
wordlist = (hanja2hangul(dic, word) for word in wordlist)
#wordlist = word_filter(wordlist, 1,2)

cnt = word_counter(wordlist)

pprint(cnt.most_common(nprint))
