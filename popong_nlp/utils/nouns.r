library('KoNLP')
library('wordcloud')
library('plyr')
library('stringr')

setwd('/home/e9t/dev/popong')
source_dir <- '/home/e9t/data/popong/bill-docs/txt'
assembly_id <- commandArgs()[5]
if(is.na(assembly_id)) assembly_id <- 19

path <- paste(source_dir, '/', assembly_id, sep='')
file.create('data.txt')
i = '1900001.txt'

#for (i in dir(path)) {
  filepath <- paste(path, '/', i, sep='')
  text <- readLines(filepath, encoding='utf-8')[1]
  encoded <- iconv(text, localeToCharset()[1], "UTF-8")  
  noun <- extractNoun(encoded)
  #TODO: write data in one row and append bill number
  nouns <- paste(noun, collapse=",")
  print(nouns)
  write(nouns, 'data.txt', append=TRUE)
  print(filepath)
#}