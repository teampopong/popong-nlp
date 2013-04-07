#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

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
