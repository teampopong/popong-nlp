#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from hangul import translit

# List family names of (estimated population) > 50M
# Source: http://en.wikipedia.org/w/index.php?title=List_of_Korean_family_names
LAST_NAMES = {
    u"김": u"Kim",
    u"이": u"Lee",
    u"박": u"Park",
    u"정": u"Jeong",
    u"최": u"Choi",
    u"조": u"Cho",
    u"강": u"Kang",
    u"윤": u"Yoon",
    u"장": u"Jang",
    u"신": u"Shin",
    u"한": u"Han",
    u"오": u"Oh",
    u"서": u"Seo",
    u"전": u"Jeon",
    u"권": u"Kwon",
    u"황": u"Hwang",
    u"송": u"Song",
    u"안": u"Ahn",
    u"임": u"Lim",
    u"류": u"Ryu",
    u"고": u"Ko"
    }

def force_unicode(f):
    '''Python 2.x 기준, 유니코드가 아닌 str타입이 인자로 들어오면
    유니코드로 변환한 뒤 원 함수에 인자로 넘기고, 그 결과는 다시
    원래의 인코딩으로 변환해서 반환하는 decorator'''

    def interface(txt, encoding='utf-8'):

        # decode to unicode
        if isinstance(txt, str):
            txt = txt.decode(encoding)

        # actual processing
        result = f(txt)

        # return re-encoded results
        return result.encode(encoding)

    return interface

@force_unicode
def romanize(txt):
    '''한글을 영문으로 변환'''

    return translit.romanize(txt.encode('utf-8')).decode('utf-8')

@force_unicode
def firstname2eng(syls):
    '''한글 이름을 영문으로 변환'''

    syls = (romanize(syl) for syl in syls)
    firstname_en = '-'.join(syls)
    return firstname_en.capitalize()

@force_unicode
def lastname2eng(syl):
    '''한글 성을 영문으로 변환'''

    # TODO: 영문 성씨 순위 데이터 구해서 높은 percentage의 성씨로 변환
    lastname_en = LAST_NAMES.get(syl, romanize(syl))
    return lastname_en.capitalize()
