#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:27:49 2021

@author: santealtamura
"""
import csv

"""
Altamura       :	coppie nell'intervallo 201-250

"""
INTERVAL_START = 201
INTERVAL_END = 250

"""
Processo di annotazione manuale dell'utente'
"""

with open('annotations/annotations1.tsv', 'wt') as out_file:
    
    #processo di annotazione. vengono prese le coppie di parole
    #che vanno da INTERVAL_START  a INTERVAL_END e viene chiesto
    #all'utente il punteggio di similarità [1-4]
    tsv_writer = csv.writer(out_file, delimiter='\t')
    
    with open("utils/it.test.data.txt","r",encoding="utf8") as fp:
        for i, line in enumerate(fp):
            if i >= INTERVAL_START - 1:
                line = line.replace("\n", "").split("\t")
                print("==============================")
                word1,word2 = line[0],line[1]
                print(word1," ", word2)
                similarity_value = float(input("Inserire similarità(1-4): "))
                similarity_value = format(similarity_value,'.1f')
                tsv_writer.writerow([word1, word2, similarity_value])
                print("==============================")
            if i == INTERVAL_END - 1:
                break
    fp.close()
    out_file.close()
    
    