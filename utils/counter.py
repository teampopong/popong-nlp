#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter
import regex    # http://www.regular-expressions.info/unicode.html

def count(text):
    with open(text, 'r') as f:
        # TODO: morpheme analysis, spacing
        # TODO: Hanja transliteration?
        words = regex.findall(ur'[\p{Hangul}|\p{Latin}|\p{Han}]+',\
                f.read().decode('utf-8'))
    cnt = Counter(words)
    # for c in cnt.most_common(num): print c[0], c[1]
    return sorted(dict(cnt).items(), key=lambda x:x[1], reverse=True)

def keywords(words, num=20):
    if num < len(words):
        keys = []
        for w in words:
            if len(w[0]) > 1: keys.append(w)
            if len(keys)==num: break
        return keys
    else:
        return words

if __name__=="__main__":
    import sys
    fp = sys.argv[1:]
    if len(sys.argv)!=2:
        print "Usage: python counter.py [textfile]"
        sys.exit(2)
    else:
        words = count(fp[0])
        keys = keywords(words, num=20)
        for i, t in enumerate(keys, start=1):
            print i, t[0], t[1]
