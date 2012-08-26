#! /usr/bin/python3
# -*- coding: utf-8 -*-

from base import * 
import utils
from importer import *

opt = 'test'
fieldname = 'education'
nprint = 300

filenames = get_filenames('../../crawlers/election_commission/data/', opt)
fieldlist = get_rawlist(filenames, fieldname)
wordlist = list_parser(fieldlist)
wordlist = flatten_list(wordlist)
dic = utils.read_HHdic()
wordlist = (utils.hanja2hangul(dic, word) for word in wordlist)
#wordlist = word_filter(wordlist, 1,2)

cnt = word_counter(wordlist)

pprint(cnt.most_common(nprint))
