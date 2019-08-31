#! /usr/bin/python3
# -*- coding: utf-8 -*-

from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.error, urllib.parse

from . import get
from ... import settings as s

USER_AGENT = s.canonizer["user_agent"]
WIKI_URL = s.canonizer["wiki_url"]
GOOGLE_URL = s.canonizer["google_url"]
XPATH_WIKI_CANONICAL_NAME = s.canonizer["xpaths"]["wiki_canonical_name"]
XPATH_WIKI_CATEGORIES = s.canonizer["xpaths"]["wiki_categories"]

'''
def branch(query):
    # TODO: try/except
    branch = dict()
    page = request(WIKI_URL+query)
    branch['name'] = get_canonical_name(page)
    branch['children'] = get_categories(page)
    return branch
'''

def canonical_name(query):
    url = WIKI_URL + urllib.parse.quote(query)
    tree = get.htmltree(url)
    page = get.webpage(tree)
    canon = get_canonical_name(page)
    return canon

def get_canonical_name(page):
    return get.text(page, XPATH_WIKI_CANONICAL_NAME)[0]

'''
def get_categories(page):
    catlist = get.text(page, XPATH_WIKI_CATEGORIES)[2:]
    catlist = [{"name": c} for c in catlist]
    return catlist
'''
