#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pandas as pd

'''
- 데이터 다운로드: [기관코드조회](https://www.code.go.kr/std/jsp/index.jsp) > 기관유형선택 '고등교육기관' > 'cb-highereducation-specific.csv'로 저장
- 데이터 처리: `python highereducation.py`
'''

inp = 'cb-highereducation-specific.csv'
outp = 'cb-highereducation.csv'

cb = pd.read_csv(inp, encoding='utf-8')
with open(outp, 'w') as f:
    f.write('code,ko\n')
    for a, b, c in zip(cb[u'기관코드'], cb[u'전체기관명'], cb[u'최하위기관명']):
        if b==c:
            s = '%s,%s\n' % (a, b)
            f.write(s.encode('utf-8'))
