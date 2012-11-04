#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import html5lib, urllib2
import settings, xpaths

from pprint import pprint

def create_category_tree(query):
    #TODO: make tree
    q = '서울대'
    bone = fetch(['all'], query)
    
    '''
    for c in bone['categories']:
        print c
        q = '분류:' + querify(c)
        bone = fetch(['all'], q)
        pprint(bone)
    '''
    return tree

def fetch(optlist, query):
    bone = dict()
    page = request_page(q)
    for opt in optlist:
        if opt in ['canonical','name','n','all']:
            bone['canonical_name'] = get_canonical_name(page)
        if opt in ['category','categories','c','all']:
            bone['categories'] = get_categories(page)
    return bone
 
def request_page(query):
    url = settings.BASE_URL + query
    p = html5lib.HTMLParser(\
            tree=html5lib.treebuilders.getTreeBuilder("lxml"),\
            namespaceHTMLElements=False)
    r = urllib2.Request(url)
    r.add_header("User-Agent", settings.USER_AGENT)
    f = urllib2.urlopen(r)
    page = p.parse(f)
    return page

def querify(query):
    encoded = query.encode('utf-8')
    engaged = encoded.replace(' ', '_')
    return engaged

def get_canonical_name(page):
    return get_text_list(page, xpaths.CANONICAL_NAME)[0]
   
def get_categories(page):
    return get_text_list(page, xpaths.CATEGORIES)[2:]

def get_text_list(page, x):
    elem = page.xpath(x)[0]
    l = list(elem.itertext())
    return l

if __name__ == '__main__':
    '''
    q = '서울대'
    bone = fetch(['all'], q)
    print(bone)
    '''
    tree = create_category_tree(query)
    print tree
