#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
from collections import Counter
from pprint import pprint

ENDDELIMS = '[\.\!\?]'
TOKENDELIMS = '\W'
ndecimals = 4

def main(corpus, instring):
    # get doc
    lines = open_file(corpus)
    doc = strip_n_and_merge_lines(lines)

    # get words
    words = doc.split()

    # get bigram counts
    setofwords = set(words) #13776 words
    nvoca = len(setofwords)
    counter = create_counter(setofwords)
    bigram_cnt = count_bigrams(counter, words)

    # preprocessing
    tokenlist = instring.split()

    # get matrices
    cm = get_count_matrix(bigram_cnt, tokenlist)
    pm = get_prob_matrix(bigram_cnt, tokenlist)
    lm = get_laplace_matrix(bigram_cnt, tokenlist, nvoca)
    print(tokenlist)
    pprint(cm)
    '''
    # get Good-Turing frequencies
    N = get_turing_calcs(bigram_cnt)
    #turing_bigram_cnt = calc_turing_bigrams(bigram_cnt, N)

    # print results
    print '\n+ Count matrix'; print tokenlist; pprint(cm)
    print '\n+ Probability matrix'; print tokenlist; pprint(pm)
    print '\n+ Laplace matrix'; print tokenlist; pprint(lm)
    print '\n+ Turing frequencies'; print N
    '''

def open_file(filename):
    with open(filename, 'r') as f:
        doc = f.readlines()
    return doc

def print_info(doc):
    a = re.findall('[\!\?\.]', doc)
    aa = len(a)

    b = re.findall('\w+', doc)
    bb = len(b)

    c = re.findall('\W', doc)
    cc = len(c)

    print aa, bb, cc
    print bb/aa

def strip_n_and_merge_lines(lines):
    d = (line.strip('\r\n') for line in lines)
    doc  = ' '.join(d)
    return doc

def collapse_listoflist(listoflist):
    return [item for sublist in listoflist for item in sublist]

def create_counter(setofwords):
    counter = dict()
    for word in setofwords:
        counter[word] = dict()
    return counter

def count_bigrams(counter, words):
    i = 0
    for i in range(len(words)-1):
        try:
            counter[words[i]][words[i+1]] += 1
        except:
            counter[words[i]][words[i+1]] = 1
        i += 1
    return counter

def get_count_matrix(bigram_cnt, tokenlist):
    i = 0
    L = []
    nwords = len(tokenlist)
    for i in range(nwords):
        l = list()
        for j in range(nwords):
            try:
                l.append(bigram_cnt[tokenlist[i]][tokenlist[j]])
            except:
                l.append(0)
        L.append(l)
    return L

def get_prob_matrix(bigram_cnt, tokenlist):
    i = 0
    L = []
    nwords = len(tokenlist)
    for i in range(nwords):
        vals = bigram_cnt[tokenlist[i]].values()
        total = sum(vals)
        l = list()
        for j in range(nwords):
            try:
                n = round(bigram_cnt[tokenlist[i]][tokenlist[j]]/float(total), ndecimals)
                l.append(n)
            except:
                l.append(0.0)
        L.append(l)
    return L

def get_laplace_matrix(bigram_cnt, tokenlist, nvoca):
    i = 0
    L = []
    nwords = len(tokenlist)
    for i in range(nwords):
        vals = bigram_cnt[tokenlist[i]].values()
        total = sum(vals)
        l = list()
        for j in range(nwords):
            try:
                n = round((bigram_cnt[tokenlist[i]][tokenlist[j]]+1)/\
                        float(total+nvoca), ndecimals)
                l.append(n)
            except:
                n = round(1/float(total+nvoca), ndecimals)
                l.append(n)
        L.append(l)
    return L

def get_turing_calcs(bigram_cnt):
    vals = []
    for word in bigram_cnt:
        vals.append(bigram_cnt[word].values())
    vals = collapse_listoflist(vals)

    cnt = Counter()
    for v in vals:
        cnt[v] += 1
    return dict(cnt)

def calc_turing_bigrams(bigram_cnt, N):
    #TODO: something wrong here! (count에 0이 있어서 생기는 문제임)
    for word in bigram_cnt:
        for nextword in bigram_cnt[word]:
            c = bigram_cnt[word][nextword]
            bigram_cnt[word][nextword] = (c+1) * N[c+2] / N[c+1]
    return bigram_cnt

if __name__ == '__main__':
    main('../_output/education.txt', '<s> 서울대학교 법과대학 졸업 </s>')
