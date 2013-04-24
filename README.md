Team POPONG NLP Package
=======================

## Dependencies
- `pip install regex unidecode`

## Usage

2. Structurize

        >>> from nlp.structurizer import structurize
        >>> structurize(u'경기도 부천시원미구을', 'district')
        ['31050', '31051']

3. Canonize

        >>> from nlp.babylon.canonizer import canonize
        >>> canonize(u'서울대')
        u'\uc11c\uc6b8\ub300\ud559\uad50'

1. Translit

        >>> from nlp.utils.translit import translit
        >>> translit('박근혜', 'ko', 'en', 'name')
        'Park Geun-hye'
        >>> translit('한나라당', 'ko', 'en', 'party')
        'Hannara Party'
        >>> translit('안녕하세요', 'ko', 'en')
        'Annyeonghaseyo'
        >>> translit(u'丁新闻', 'cn', 'ko')
        u'\uc815\uc2e0\ubb38'

1. Word count

        >>> from nlp.utils.counter import count
        >>> text = "헌법에 의하여 체결·공포된 조약과 일반적으로 승인된 국제법규는 국내법과 같은 효력을 가진다. 국가는 법률이 정하는 바에 의하여 재외국민을 보호할 의무를 진다. 대한민국의 국민이 되는 요건은 법률로 정한다. 모든 국민은 직업선택의 자유를 가진다. 대한민국은 국제평화의 유지에 노력하고 침략적 전쟁을 부인한다. 국가는 사회보장·사회복지의 증진에 노력할 의무를 진다.\nLorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.\n今美令朝徳管層船期済惑約専訓馬著。心太発野姿禁記髄訃就大県育出際銀子。応採聞開続曲左感康著路毎避案。力内倒粒保自訴並殺聴阪職用区者婚順図霊院。止棚側烈掲物小下侵転躍央改原乳。要園今治図社盟討水慎北場素土投。要素区東組月懸法目大真申番稿。美酬募車中装視産解高提都門調革多語。際育馬塁竹週崩汚背念無浩。"
        >>> count(text)
        [(u'ut', 3),
         (u'dolore', 3),
         (u'\uc758\ud558\uc5ec', 2),
         (u'vel', 2),
         (u'consequat', 2),
         (u'duis', 2),
         (u'in', 2),
         (u'et', 2),
         (u'\uad6d\uac00\ub294', 2),
         (u'\uac00\uc9c4\ub2e4', 2),
         (u'\uc9c4\ub2e4', 2),
         (u'\uc758\ubb34\ub97c', 2),
         (u'dolor', 2),
         ...
         (u'autem', 1)]


## Structure
    .
    ├── README.md
    ├── main.py
    ├── settings.py
    │
    ├── babylon/
    │   ├── babylon.py          # creates dictionaries
    │   ├── canonizer/          # finds canonical names from Wikipedia
    │   └── __init__.py
    ├── bills/
    │   ├── converter.sh        # converts `pdf` files to `txt` files (depends on [pdfminer](http://www.unixuser.org/~euske/python/pdfminer/))
    │   ├── get.py              # retrieves `txt` files from a given path
    │   └── __init__.py
    ├── __init__.py
    ├── _input/                 # temporary input files
    │   ├── cb-region.csv
    │   ├── lastnames.json
    ├── _output/                # temporary output files
    ├── structurizer
    │   ├── district.py
    │   ├── education.py
    │   ├── __init__.py
    │   ├── preprocessor.py
    │   └── replace.py
    ├── _test/                  # temporary test codes
    │   ├── bigrams.py
    │   ├── count.csv
    │   └── counter.py
    └── utils/
        ├── counter.py          # counts eojeols
        ├── encoder.py
        ├── eval.py             # evaluator (in preparation)
        ├── importer.py         # retrieves each attribute for officials
        ├── __init__.py
        ├── preprocessing.py
        ├── structurizer.py
        ├── translit/
        └── utils.py
