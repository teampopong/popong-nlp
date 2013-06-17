#! /usr/bin/env Rscript

library('KoNLP')

setwd('/home/e9t/dev/popong')
source_dir <- '/home/e9t/data/popong/bill-docs/nouns'

f <- file("stdin")
open(f)
while(length(line<- readLines(f, n=1)) > 0) {
  noun <- extractNoun(line)
  nouns <- paste(noun, collapse="\n")
  write(nouns, 'tmp.txt')
}
