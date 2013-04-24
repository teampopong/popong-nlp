#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

## Settings
data = {
    "officials" : "/home/e9t/data/popong/people",
    "bills"     : "/home/e9t/data/popong/bills/pdf",
    "HHdic"     : "/home/e9t/data/hanja-hangul.json",
    "test"      : "./_input"
}

results = {
    "dict"      : "./_output",
    "test"      : "./_output"
}

path = {
    "codebook": {
        "region": "_input/cb-region.csv"
    }
}

structurizer = {
    "fieldname" : "district",
    "runopt"    : "all" # test, all, [some integer]
}

## Global variables
features = ["district", "address", "education"]
others = ["name_kr", "name_cn", "assembly_no", "party", "birthday",\
    "birthmonth", "birthyear", "image", "sex", "cand_no", "elected"]

main = {
    "opts" : {
        1: "get_data",
        2: "do_babylon (in preparation)",
        3: "do_bills (in preparation)",
        4: "do_structurize",
        5: "do_count (in preparation)"
    }
}

district = {
    "levels"    : ["시", "군", "구"],
    "sublevels" : ["갑", "을", "병"],
    "stopwords" : ["제", "선거구", "지역구"],
    "aliases"   : {
        "서울": "서울특별시",
        "대전": "대전광역시",
        "대구": "대구광역시",
        "부산": "부산광역시",
        "울산": "울산광역시",
        "광주": "광주광역시",
        "인천": "인천광역시",
        "제주": "제주특별자치도",
        "경기": "경기도",
        "강원": "강원도",
        "충북": "충청북도",
        "충남": "충청남도",
        "전남": "전라남도",
        "전북": "전라북도",
        "경남": "경상남도",
        "경북": "경상북도"
    }
}
