#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import regex
import json

def write_json(data, filename, opt=None):
    with open(filename, 'w') as f:
        if opt=='compact':
            json.dump(data, f)
        else:
            json.dump(data, f, indent=2)

def chk_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
