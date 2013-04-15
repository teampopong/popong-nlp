#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

data = {
    "officials" : "/home/e9t/data/popong/people",
    "bills"     : "/home/e9t/data/popong/bills/pdf",
    "test"      : "./_input",
    "HHdic"     : "/home/e9t/data/hanja-hangul.json"
}

results = {
    "dict"      : "./_output",
    "test"      : "./_output"
}

structurizer = {

# Available fields:
#   name_kr, name_cn, assembly_no,
#   education, party, district,
#   birthday, birthmonth, birthyear, image, sex, cand_no, elected

# TODO: Fix erroneous fields (address, key error) (experience, list found)

    "fieldname" : "district",
# Available options: test, all, [any number]
    "runopt"    : "all"
}
