#! /usr/bin/python3
# -*- coding: utf-8 -*-

import wikipedia

if __name__ == '__main__':
    queries = [\
            u'서울대학교',u'서울대',u'경성제대',u'경성제국대학',\
            u'KAIST',u'카이스트',u'한국과학기술원',\
            u'고려대',u'보성전문',\
            u'법대',u'산업공학과']

    for q in queries:
        try:
            canon = wikipedia.canonical_name(q.encode('utf-8'))
        except:
            canon = None
        print('"%s" -> "%s"' % (q, canon))
