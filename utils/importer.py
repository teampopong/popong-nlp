#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, sys
import json
from glob import glob
from pprint import pprint

def data_importer(path, opt='test', fieldname='name_kr', source='file'):
    #TODO(lucypark): Get multiple fields

    def printer():
        print('## Fieldname: ' + fieldname.upper())
        if opt != 'all':
            print('- Filename(s):')
            pprint(filenames)
        else:
            pass
        print('- n(files)\t: '+ str(len(filenames)))
        print('- n(items)\t: '+ str(len(fieldlist)))

    if source=='file':
        # Elected officials are included in candidates
        allfiles = glob(os.path.join(path, '*_candidates_*.json'))
        filenames = select_files(allfiles, opt)

        fieldlist = [p.get(fieldname)\
        for f in filenames for p in read_people(f) if p.get(fieldname)]
        printer()

    elif source=='db':
        #TODO(lucypark): extract data from db
        fieldlist = None

    else:
        print 'Warning: Invalid source (file, db)'
        sys.exit(2)

    return fieldlist

def select_files(filenames, opt):
    opt = opt.encode('utf-8')

    if isinstance(opt, int):
        filenames = [filenames[opt]]

    elif isinstance(opt, str):

        if opt == 'all':
            pass
        elif opt == 'test':
            filenames = [filenames[0], filenames[20], filenames[40]]
        elif opt == 'legislators':
            filenames = filenames[:19]
        elif opt == 'mayors':
            filenames = filenames[19:24]
        elif opt == 'presidents':
            filenames = filenames[24:]
        else:
            print "Warning: Invalid option\
                    ('all', 'test', 'legistlators', 'mayors', 'presidents')"
            sys.exit(2)

    else:
        print "Warning: \
                Options should either be an integer in [0,40] or string in\
                {'all', 'test', 'legistlators', 'mayors', 'presidents'}"
        sys.exit(2)

    return filenames

def read_people(filename):
    with open(filename, 'r') as f:
        j = f.read()
        people = json.loads(j)
    return people

if __name__ == '__main__':
    fieldlist = data_importer('/home/e9t/data/popong/people'
            , fieldname='education')

    for item in fieldlist:
        print item.encode('utf-8')
