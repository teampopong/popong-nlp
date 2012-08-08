#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
This is a library to structurize short free texts 
written in the Korean language
'''

import json, re, os
from pprint import pprint
from collections import Counter

settings = {
    'DIR': '''../../crawlers/election_commission/data/''', #base_directory
    'MAX_PRINT': 30,
    'MAX_ELECTIONS': 20
    }

def main():
    '''
    l = get_filenames()
    pprint(l)
    # '''   
    
    edu, files = get_rawlist('education', 'all')
    #edu, files = get_rawlist('party', 'all')
    #print(edu)
    #print(files)

    print('n(items)\t: '+ str(len(edu)))
    print('n(files)\t: '+ str(len(files)))

    wordlist = flatten_list(list_parser(edu))
    #print(wordlist)

    word_counter(wordlist)

def get_rawlist(fieldname, opt='test'):
    '''
    Get list for a specific fieldname from 'people'.

    [Params]
         - Fieldnames:
            votenum, district, elected, name_kr, voterate, name_cn, 
            experience, sex, birthyear, job, party, assembly_no, education
         - opt:
            Integer in [1,82] || String in {'all', 'test'}
    '''

    files = get_filenames()

    if isinstance(opt, int):
        files = [files[opt]]
    elif isinstance(opt, str):
        if opt == 'all':
            pass
        elif opt == 'test':
            files = [files[0], files[39], files[50]]
        else:
            raise "Error: String options should be in {'all', 'test'}"

    else:
        raise "Error: Options should either be\
                an integer in [1,82] or string in {'all', 'test'}"

    rawlist = [p[fieldname] for f in files for p in read_people(f)]
    return rawlist, files

def get_filenames(directory=settings["DIR"]):
    ELECTION_TYPE = ['assembly', 'mayor', 'president']
    ELECTION_RESULT = ['candidates', 'elected']
    ELECTION_NO = [str(n) for n in range(settings["MAX_ELECTIONS"])] 
    FILE_TYPE = '.json'

    filenames = []
    for t in ELECTION_TYPE:
        for r in ELECTION_RESULT:
            for n in ELECTION_NO:
                filename = '%s%s-%s-%s%s'\
                    % (directory, t, r, n, FILE_TYPE)
                if os.path.exists(filename):
                    filenames.append(filename)
    return filenames

def read_people(filename):
    with open(filename, 'r') as f:
        j = f.read()
        people = json.loads(j)
    return people

def word_counter(wordlist):
    cnt = Counter()
    for word in wordlist:
        cnt[word] += 1

    print(cnt.most_common(settings["MAX_PRINT"]))

def flatten_list(listoflist):
    return [item for sublist in listoflist for item in sublist]

def list_parser(rawlist):
    return (re.split('[ ()0-9]',item) for item in rawlist)

if __name__ == '__main__':
    main()
