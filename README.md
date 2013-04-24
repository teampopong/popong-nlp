Team POPONG NLP Package
=======================

## Dependencies
- `pip install regex unidecode`

## Usage
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

2. Structurize

        >>> from nlp.structurizer import structurize
        >>> structurize(u'경기도 부천시원미구을', 'district')
        ['31050', '31051']

3. Canonize

        >>> from nlp.babylon.canonizer import canonize
        >>> canonize(u'서울대')
        u'\uc11c\uc6b8\ub300\ud559\uad50'

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
    │   ├── eval.py             # evaluator (in preparation)
        ├── importer.py         # retrieves each attribute for officials
        ├── __init__.py
        ├── preprocessing.py
        ├── structurizer.py
        ├── translit/
        └── utils.py
