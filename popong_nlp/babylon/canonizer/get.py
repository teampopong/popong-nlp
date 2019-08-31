#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.error, urllib.parse, html5lib

def htmltree(url):
    r = urllib.request.Request(url)
    r.add_header("User-Agent", "Mozilla/5.0")
    f = urllib.request.urlopen(r)
    return f

def webpage(f):
    page = html5lib.HTMLParser(\
        tree=html5lib.treebuilders.getTreeBuilder("lxml"),\
        namespaceHTMLElements=False)
    p = page.parse(f)
    return p

def text(p, x):
    elem = p.xpath(x)[0]
    e = list(elem.itertext())
    return e
