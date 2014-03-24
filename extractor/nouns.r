#! /usr/bin/env Rscript

library('KoNLP')

f <- file("stdin")
open(f)
while(length(line<- readLines(f, n=1)) > 0) {
  noun <- extractNoun(line)
  nouns <- paste(noun, collapse=" ")
  write(nouns, stdout(), append=TRUE)
}
