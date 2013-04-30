#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys, json
from urllib2 import HTTPError
import gevent
#FIXME(lucypark): Exception KeyError (http://stackoverflow.com/questions/8774958)
from gevent.monkey import patch_all; patch_all(thread=False)

from canonizer.wikipedia import canonical_name
from utils import utils
import settings as s

def build_alias_dict(fieldname, doc):
    terms = get_terms(doc)
    write_terms(fieldname, terms)

    alias_dic = get_aliases(terms)
    write_aliases(fieldname, alias_dic)

def get_terms(doc):
   terms = list(set(doc.split()))
   sys.stdout.write('n(terms)\t: '); print len(terms)
   return terms

def get_aliases(terms):
    i = 1
    jobs = []
    alias_dic = {}

    for term in terms:
        #hashing(word, terms, alias_dic, i)
        job = gevent.spawn(hashing, term, terms, alias_dic, i)
        jobs.append(job)
        i += 1
    gevent.joinall(jobs)

    return alias_dic

def hashing(word, terms, dic, i):
    try:
        canon = canonical_name(word.encode('utf-8'))
        selected = select(canon, terms)
        if selected not in [None, word]:
            dic[word] = selected
        print '%s\t%s\t: %s, %s' % (str(i), word, canon, selected)
    except:
        print '%s\t%s\t: pass' % (str(i), word)

def select(alias, terms):

    f = alias.find('(')
    if f > 0:
        selected = alias[:f]
    else:
        selected = alias

    r = selected.replace(' ', '')
    if r in terms:
        selected = r
    else:
        selected = None

    return selected

def write_terms(fieldname, terms):
    f = '%s/terms-%s.txt' % (s.results["dict"], fieldname)
    utils.write_text('\n'.join(terms), f)
    print 'Terms written to ' + f

def write_aliases(fieldname, aliases):
    f = '%s/aliases-%s.json' % (s.results["dict"], fieldname)
    utils.write_json(f, aliases)
    print 'Aliases written to ' + f


if __name__ == '__main__':
    print "Good"
    # etime - stime, "seconds"
    # education 전체로 돌렸을 때 9083 sec
    # party 전체로 돌렸을 때 82 sec

    # Update 2013-04-30:
    #   preprocessing 후 education 전체로 돌리니 354초!
