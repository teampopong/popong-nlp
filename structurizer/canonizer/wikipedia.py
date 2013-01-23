#! /usr/bin/python3
# -*- coding: utf-8 -*-

import get
import settings, xpaths

'''
def branch(query):
    # TODO: try/except
    branch = dict()
    page = request(settings.WIKI_URL+query)
    branch['name'] = get_canonical_name(page)
    branch['children'] = get_categories(page)
    return branch
'''

def canonical_name(query):
    page = request(settings.WIKI_URL+query)
    canon = get_canonical_name(page)
    return canon

def request(url):
    f = get.htmltree(url)
    p = get.webpage(f)
    return p

def get_canonical_name(page):
    return get.text(page, xpaths.WIKI_CANONICAL_NAME)[0]

'''
def get_categories(page):
    catlist = get.text(page, xpaths.WIKI_CATEGORIES)[2:]
    catlist = [{"name": c} for c in catlist]
    return catlist
'''
