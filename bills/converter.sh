#! /bin/bash

for i in *.pdf
do 
    echo $i
    pdf2txt.py -o ${i%.*}.txt $i
done
