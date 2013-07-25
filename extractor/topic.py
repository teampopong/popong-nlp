#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from time import time

from nltk.corpus import stopwords
from gensim import corpora, models, similarities

from dictionary import get_dictionary
from data import get_reviews, testdocs
from utils import get_words, write_json

def get_documents(reviews):
    return sum(reviews.values(), [])

def get_bag_of_words(document, dictionary, stoplist):
    return dictionary.doc2bow(get_words(document, stoplist))

def bow_per_movie():
    d = {}
    for movie, review in reviews.items():
        ids = get_bag_of_words(' '.join(review), dictionary, stoplist)
        strings = ((dictionary[_id], cnt) for _id, cnt in ids if cnt>1)
        sorteds = sorted(strings, key=lambda x: x[1], reverse=True)
        d[movie] = sorteds
    write_json(d, countfile, opt='compact')

def movie_stopwords():
    with open('data/stopwords.txt', 'r') as f:
        return f.read().split('\n')

if __name__=='__main__':
    from pprint import pprint

    print('## Input parameters')
    NEW_DOC = "Human computer interaction"
    NEW_DOC = "컴퓨터 사용자 관계"
    dictfile, jsonfile = 'dict/dict_reviews.dict', 'dict/dict_reviews.json'
    infile = 'data/cmmt_withtotal.csv'
    outfile = 'data/raw_reviews.json'
    countfile = 'data/count_movies.json'
    ntopics = 10

    print('## Get all documents')
    reviews = get_reviews(infile); write_json(reviews, outfile) # 2438 movies
    documents = get_documents(reviews) # 17013 reviews
    #documents = testdocs('ko')

    print('## Get dictionary')
    stoplist = stopwords.words('english') + movie_stopwords()
    dictionary = get_dictionary(documents, stoplist, dictfile, jsonfile, 'online')
    dictionary = corpora.Dictionary.load(dictfile)
    print dictionary # 35289 tokens (35187 after stopword removal)

    print('## Calculate matrices')
    s = time()
    bow_per_movie()
    corpus_mat = (get_bag_of_words(doc, dictionary, stoplist) for doc in documents)
    new_vec = get_bag_of_words(NEW_DOC, dictionary, stoplist)
    print time() - s # 7s (generator, but this doesn't work)

    '''
    print('## TF-IDF')
    s = time()
    corpus_mat = list(corpus_mat)
    tfidf = models.TfidfModel(corpus_mat)
    corpus_tfidf = tfidf[corpus_mat]
    #corpus_tfidf.save('data/tfidf_reviews.mm')
    #corpus_tfidf = corpora.MmCorpus('data/tfidf_reviews.mm')
    print corpus_tfidf
    print time() - s # 123s

    print('## LSI')
    s = time()
    lsi = models.LsiModel(corpus_mat, id2word=dictionary, num_topics=ntopics)
    lsi.save('data/lsi.mm')
    corpus_lsi = lsi[corpus_mat]
    print time() - s # 8s
    with open('results/lsi.txt', 'w') as f:
        f.write('\n'.join(lsi.print_topics(ntopics)))
    #for doc in corpus_lsi: print doc

    print('## LDA')
    s = time()
    lda = models.LdaModel(corpus_mat, id2word=dictionary, num_topics=ntopics)
    lda.save('data/lda.mm')
    corpus_lda = lda[corpus_mat]
    print time() - s # 25s
    with open('results/lda.txt', 'w') as f:
        for i in range(ntopics):
            f.write(lda.print_topic(i))
            f.write('\n')
    #for doc in corpus_lda: print doc
    '''
