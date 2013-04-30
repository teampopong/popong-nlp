#! /usr/bin/python3
# -*- coding: utf=8 -*-

from babylon import canonizer
from utils import utils
import settings as s
import base

STARTS = s.education['countries']
ENDS = s.education['statuses']
STOPWORDS = s.education['stopwords']
ABBREVS = s.education['abbrevs']
ALIASES = s.education['aliases']
TERMS = ALIASES.keys() + ALIASES.values()
for i in s.education['to_ignore']: TERMS.remove(i)

def reverse_pop(word):
    popped = []
    '''
    exception = u'대학원'
    f = word.find(exception)
    if f > 0:
        popped = [word[:f], exception, word[f+3:]]
    else:
    '''
    for j in range(len(word), -1, -1):
        challenger, remainder = word[:j], word[j:]
        if challenger in TERMS:
            if word[j]==u'원':
                popped.append(word[:j+1])
                popped.append(word[j+1:])
            else:
                popped.append(challenger)
                popped.append(remainder)
            break
        if j==0:
            popped.append(word)
    return popped

def spacer(line):
    words = line.split()
    spaced = []
    for word in words:
        if word in ENDS+TERMS:
            spaced.append(word)
        else:
            spaced.extend(reverse_pop(word))
    return ' '.join(spaced)

def convert(line):
    endsplit = base.endsplitter(line, ENDS)
    startsplit = base.startsplitter(endsplit, STARTS)
    words = base.wordify(startsplit)
    erased = base.eraser(words, STOPWORDS)
    canonized = base.canonizer(erased, ABBREVS)
    canonized = base.canonizer(canonized, ALIASES)
    return ' '.join(canonized)

def struct(string, codemap):
    print 'tba'

def markup(string, codemap):

    def encode(token):
        codes = codemap.get(token)
        if type(codes)==list:
            return codes[0]
        else:
            return None

    converted = convert(string)
    tokens = converted.split()
    encoded = (encode(token) for token in tokens)
    return zip(tokens, encoded)

def main(codemap):

    def write_results(lines, marked, filename):
        with open(filename, 'w') as f:
            for l, m in zip(lines, marked):
                s = '%s -> %s\n' % (l, ' '.join('%s/%s' % (d, c) for d, c in m))
                f.write(s.encode('utf-8'))

        print 'Written to ' + filename

    ## Get data
    data = utils.read_text('./_output/people-all-education.txt')
    lines = data.split('\n')
    #lines = data.split('\n')[14460:14470]

    ## Convert data
    converted = [convert(line) for line in lines]
    spaced = [spacer(line) for line in converted]
    final = [convert(line) for line in spaced]
    marked = [markup(line, codemap) for line in final]

    ## Print results
    #for l, f in zip(lines, final): print '%s -> %s ' % (l, f)
    #for l, c, m in zip(lines, converted, marked): print '%s -> %s -> %s' % (l, c, ' '.join('%s/%s' % (d, c) for d, c in m))
    write_results(lines, marked, '_output/people-all-education-marked.txt')
