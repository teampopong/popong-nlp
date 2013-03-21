Team POPONG NLP Package
=======================

## Packages 
1. `main.py`
2. `settings.py`
3. `README.md`

### babylon/
1. `babylon.py`
    - creates dictionaries
2. `canonizer/`
    - finds canonical names from Wikipedia

### bills/
1. `converter.sh`
    - converts `pdf` files to `txt` files
    - depends on [pdfminer](http://www.unixuser.org/~euske/python/pdfminer/)
2. `get.py`
    - retrieves `txt` files from a given `path`

### structurize/
1. `importer.py`
    - retrieves each attribute for officials
2. `eval.py`
    - evaluator

### translit/
1. `cn2ko.py`
    - read Chinese
1. `ko2en.py`
    - use this file to romanize names and parties
    - names:
        - ex: romanize.name2eng('박근혜')
    - parties:
        - ex: romanize.party2eng('새누리당')
2. `base.py`
    - basic methods used in `romanize.py`

### utils/
1. `counter.py`
    - counts eojeols

### _test/
Temporary test codes.
1. `bigrams.py`
    - TODO: currently broken!

## Data
### _input/
Temporary input files.

### _output/
Temporary output files.

