#! /usr/bin/python3
# -*- coding: utf-8 -*-

import html5lib, urllib2
import settings, xpaths
import json

from pprint import pprint

def fetch_branch(query):
    branch = dict()
    page = request_wiki_page(query)
    branch['name'] = get_canonical_name(page)
    branch['children'] = get_categories(page)
    return branch

def fetch_canonical_name(query):
    page = request_wiki_page(query)
    name = get_canonical_name(page)
    return name

def request_wiki_page(query):
    url = settings.WIKI_URL + query
    p = html5lib.HTMLParser(\
            tree=html5lib.treebuilders.getTreeBuilder("lxml"),\
            namespaceHTMLElements=False)
    r = urllib2.Request(url)
    r.add_header("User-Agent", settings.USER_AGENT)
    f = urllib2.urlopen(r)
    page = p.parse(f)
    return page

def get_canonical_name(page):
    return get_text_list(page, xpaths.CANONICAL_NAME)[0]
   
def get_categories(page):
    catlist = get_text_list(page, xpaths.CATEGORIES)[2:]
    catlist = [{"name": c} for c in catlist]
    return catlist

def get_text_list(page, x):
    elem = page.xpath(x)[0]
    l = list(elem.itertext())
    return l

if __name__ == '__main__':
    queries = [\
            u'서울대학교',u'서울대',u'경성제대',u'경성제국대학',\
            u'KAIST',u'카이스트',u'한국과학기술원',\
            u'고려대',u'보성전문학교',\
            u'법대',u'산업공학과']
    for q in queries:
        try:
            branch = fetch_branch(q.encode('utf-8'))
            canonical_name = branch['name']
        except:
            canonical_name = None
        print('"%s" -> "%s"' % (q, canonical_name))
