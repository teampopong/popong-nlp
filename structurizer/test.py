#! /usr/bin/python3
# -*- coding: utf-8 -*-

import base
from pprint import pprint

# distrcit
'''
지역구의 경우
    1. 먼저 데이터를 읽어옴
    2. list flatten 단계까지 간 후 
    3. string이 '.+갑' 또는 '.+을'인 경우, strip '갑'과 '을'
    4. word count

base.test('district', 100, 1, 'all')

'''
# education
# base.test('education', 300, 1, 29) # 19대 당선자
base.test('education', 30, 1, 'test')

'''
for e in edu:
    #if e.endswith('졸'):
        # TODO: change entity's status to '졸업'
        #e = e[:-1]
        container.append(e)
print(container)
pprint(files)
print
print('n(strings)\t: ' + str(len(container)))
print('n(files)\t: ' + str(len(files)))
'''

"""
#experience
'''
경력의 경우
    list가 입력되므로, 이것에 대한 preprocessing 필요
'''

base.test('experience', 10, 1, 'all')


#gender
base.test('sex', 10, 1, 'all')


# job
'''
직업의 경우
    '무', '주', '대'... 가 뭔지 확인
'''

base.test('job', 10, 1, 1)


# party

#cnt = base.get_counter('party', flatten=0)
base.test('party', 10, 0, 'test')
"""
