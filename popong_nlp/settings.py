#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os.path
from .utils import utils

def get_path(f):
    return os.path.join(os.path.dirname(__file__), 'data', f)


# Settings -----------------------------------------

data = {
    "dict"      : get_path("dict"),
    "HHdic"     : get_path("dict/hanja-hangul.json"),
    "lastnames" : get_path("dict/lastnames.json"),
    "stopwords_ko" : get_path("corpus/stopwords-ko.txt")
}

codebook = {
    "region"    : get_path("codebooks/cb-administrative-divisions-20100401-edited.csv"),
    "education" : get_path("codebooks/cb-higher-education-institutes-d20130501-unique.csv")
}


# Variables -----------------------------------------

district = {
    "levels"    : ["시", "군", "구"],
    "sublevels" : ["갑", "을", "병"],
    "stopwords" : ["제", "선거구", "지역구"],
    "aliases"   : {
        "서울시": "서울특별시",
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

education = {
    "countries" : ["일본", "미국", "만주"],
    "statuses"  : ["졸", "졸업", "수료", "중퇴", "제적", "박사", "석사", "수학"],
    "stopwords" : ["미기재", "현", "한문수학", "한수", "한문", "독학"],
    "to_ignore"   : ["대학", "박사"],     # Words to ignore when spacing (rule-based)
    "aliases" : utils.read_json(get_path('dict/aliases-education.json')),
    "abbrevs"   : {
        # General
        "졸": "졸업",
        "대": "대학",
        "원": "대학원",
        "중": "중학교",
        "소": "소학교",
        "전": "전문대학",
        "고": "고등학교",
        "국": "국민학교",
        "보": "보통학교",
        "초": "초등학교",
        "고보": "고등보통학교",
        "전문": "전문대학",
        "대퇴": "대학 중퇴",
        "미": "미국",
        "일": "일본",
        # Rules
        "고대": "고려대학교"
    }
}

canonizer = {
    "user_agent": "Mozilla/5.0",
    "wiki_url"  : "http://ko.wikipedia.org/wiki/",
    "google_url": "http://www.google.com/search?hl=en&q=",
    "xpaths"    : {
        "wiki_canonical_name"  : '//h1[@id="firstHeading"]/span',
        "wiki_categories"      : '//div[@id="mw-normal-catlinks"]',
        "google_search_results": '//li[@class="g"]',
        "google_cites"         : '//body//li[@class="g"]//h3[@class="r"]//@href',
        "google_titles"        : '//body//li[@class="g"]//h3[@class="r"]//text()'
    }
}
