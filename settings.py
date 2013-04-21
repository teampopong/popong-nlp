#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

data = {
    "officials" : "/home/e9t/data/popong/people",
    "bills"     : "/home/e9t/data/popong/bills/pdf",
    "test"      : "./_input",
    "HHdic"     : "/home/e9t/data/hanja-hangul.json"
}

# Available features:
#   name_kr, name_cn, assembly_no,
#   education, party, district,
#   birthday, birthmonth, birthyear, image, sex, cand_no, elected
# TODO: Fix erroneous features (address, key error) (experience, list found)
feature = {
    "district"  : "./_output/people-all-district.txt",
    "education" : "./_output/people-all-education.txt"
}

codebook = {
    "region"    : "./_input/cb-region.csv"
}

results = {
    "dict"      : "./_output",
    "test"      : "./_output"
}

structurizer = {
    "fieldname" : "district",
# Available options: test, all, [any number]
    "runopt"    : "all"
}
