Team POPONG NLP Package
=======================

- **Pull requests are always welcome.**

## Requirements

- [KoNLPy](http://github.com/e9t/konlpy)

## Install

    # pip install git+https://github.com/teampopong/popong-nlp.gi

or

    $ git clone git@github.com:teampopong/popong-nlp.git
    $ cd popong-nlp
    # python setup.py install

## Usage

### Structurizer

    >>> from popong_nlp.structurizer import structurize
    >>> structurize(u'경기도 부천시원미구을', 'district')
    ['31050', '31051']
    >>> from popong_nlp.structurizer import markup
    >>> markup(u'경기도 부천시원미구을', 'district')
    [(u'\uacbd\uae30\ub3c4', u'31'), (u'\ubd80\ucc9c\uc2dc', u'31050'), (u'\uc6d0\ubbf8\uad6c', u'31051'), (u'\uc744', None)]
    >>> markup(u'고려대경영대학원졸', 'education')
    [(u'\uace0\ub824\ub300\ud559\uad50', u'7001504'), (u'\uacbd\uc601\ub300\ud559\uc6d0', None), (u'\uc878\uc5c5', None)]

### Canonizer

Finds canonical names of entities using Wikipedia.

    >>> from popong_nlp.babylon.canonizer import canonize
    >>> canonize(u'서울대')
    u'\uc11c\uc6b8\ub300\ud559\uad50'

### Transliterator

    >>> from popong_nlp.utils.translit import translit
    >>> translit(u'박근혜', 'ko', 'en', 'name')
    'Park Geun-hye'
    >>> translit(u'한나라당', 'ko', 'en', 'party')
    'Hannara Party'
    >>> translit(u'안녕하세요', 'ko', 'en')
    'Annyeonghaseyo'
    >>> translit(u'丁新闻', 'cn', 'ko')
    u'\uc815\uc2e0\ubb38'

### Word counter

    >>> from popong_nlp.utils.counter import count
    >>> text = u"헌법에 의하여 체결·공포된 조약과 일반적으로 승인된 국제법규는 국내법과 같은 효력을 가진다. 국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다. 대한민국의 국민이 되는 요건은 법률로 정한다. 모든 국민은 직업선택의 자유를 가진다. 대한민국은 국제평화의 유지에 노력하고 침략적 전쟁을 부인한다. 국가는 사회보장·사회복지의 증진에 노력할 의무를 진다.\nLorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.\n今美令朝徳管層船期済惑約専訓馬著。心太発野姿禁記髄訃就大県育出際銀子。応採聞開続曲左感康著路毎避案。力内倒粒保自訴並殺聴阪職用区者婚順図霊院。止棚側烈掲物小下侵転躍央改原乳。要園今治図社盟討水慎北場素土投。要素区東組月懸法目大真申番稿。美酬募車中装視産解高提都門調革多語。際育馬塁竹週崩汚背念無浩。"
    >>> words = text.split()
    >>> count(words)
    [(u'dolore', 3),
     (u'ut', 2),
     (u'\uc758\ud558\uc5ec', 2),
     (u'vel', 2),
     (u'in', 2),
     (u'et', 2),
     (u'\uad6d\uac00\ub294', 2),
     (u'\uc758\ubb34\ub97c', 2),
     (u'\uac00\uc9c4\ub2e4.', 2),
     ...
     (u'autem', 1)]


### Korean keyword extractor

    >>> import konlpy
    >>> h = konlpy.Hannanum()
    >>> from popong_nlp.extractor import extract
    >>> with open('some.txt', 'r') as f:
    ...     k = extract.keywords(f, h, maxnum=5, minlen=2, mincnt=5, minratio=0.01, g1oupsize=1000)
    ...
    >>> k
    [(u'\ud558\ub098', 0.0602), (u'\ub450\uc6b8', 0.0323)]
    >>> string = u'이것은 사랑노래가 노래가 사랑이 아닙니다.'
    >>> extract.keywords_from_string(string, h, mincnt=0, minratio=0)
    [(u'\ub178\ub798', 0.4), (u'\uc0ac\ub791', 0.4), (u'\uc774\uac83', 0.2)]


## Structure
    .
    ├── README.md
    ├── settings.py
    ├── codebooks/
    ├── dict/
    │
    ├── babylon/
    │   ├── babylon.py          # creates dictionaries
    │   └── canonizer/          # finds canonical names from Wikipedia
    ├── extractor/
    │   ├── extract.py
    │   └── nouns.r
    ├── structurizer/
    │   ├── district.py
    │   ├── education.py
    │   ├── preprocessor.py
    │   └── replace.py
    └── utils/
        ├── counter.py          # counts eojeols
        ├── encoder.py          # assigns codes to strings
        ├── eval.py             # evaluator (in preparation)
        ├── importer.py         # retrieves each attribute for officials
        ├── translit.py
        └── utils.py


## Author
[Lucy Park](http://github.com/e9t)

## License

[Apache v2.0](http://www.apache.org/licenses/LICENSE-2.0.html)
