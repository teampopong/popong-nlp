#! /usr/bin/env Rscript

library('KoNLP')

setwd('/home/e9t/dev/popong/nlp/extractor')
tmp <- file.create('nouns.txt')

f <- file("stdin")
open(f)
while(length(line<- readLines(f, n=1)) > 0) {
  noun <- extractNoun(line)
  nouns <- paste(noun, collapse=" ")
  write(nouns, 'nouns.txt', append=TRUE)
}
