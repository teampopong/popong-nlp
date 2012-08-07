#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from hangul import translit
import crawlers

# List family names of (estimated population) > 50M
# Source: http://en.wikipedia.org/w/index.php?title=List_of_Korean_family_names
LAST_NAMES = {
    "김": "Kim",
    "이": "Lee",
    "박": "Park",
    "정": "Jeong",
    "최": "Choi",
    "조": "Cho",
    "강": "Kang",
    "윤": "Yoon",
    "장": "Jang",
    "신": "Shin",
    "한": "Han",
    "오": "Oh",
    "서": "Seo",
    "전": "Jeon",
    "권": "Kwon",
    "황": "Hwang",
    "송": "Song",
    "안": "Ahn",
    "임": "Lim",
    "류": "Ryu",
    "고": "Ko"
    }
    
def getsyls(name):
    syls = [syl.encode('utf-8') for syl in list(name.decode('utf-8'))]
    return syls

def firstname2eng(syls):
    syls = [translit.romanize(syl) for syl in syls]
    firstname_en = '-'.join(syls)
    return capname(firstname_en)

def lastname2eng(syl):
    # TODO: 영문 성씨 순위 데이터 구해서 높은 percentage의 성씨로 변환
    try:
        lastname_en = LAST_NAMES[syl]
    except:
        lastname_en = translit.romanize(syl)
    return capname(lastname_en)

def capname(string):
    return string[0].capitalize() + string[1:]
