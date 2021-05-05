#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:29:41 2021

@author: santealtamura
"""
import csv
from scipy import spatial

#crea un dizionario, in cui ad ogni parola (chiave) corrisponde una lista
#di babel synset presi del file "SemEval17_IT_senses2sysensts.txt"
#es. un estratto: 
"""{.....'cifra': ['bn:00019153n', 'bn:00025702n', 'bn:00055715n', 'bn:01412291n', 
'bn:00034392n', 'bn:00024979n', 'bn:00058287n', 'bn:00034394n', 'bn:00003601n', 
'bn:00019155n'], 
   'dollaro': ['bn:00010038n', 'bn:00007240n', 'bn:00028115n', 
 'bn:00028114n', 'bn:00044648n', 'bn:00071729n', 'bn:00050950n', 
 'bn:00013472n', 'bn:00016907n', 'bn:15584900n', 'bn:00042310n', 
 'bn:00034409n', 'bn:00079129n', 'bn:00047909n', 'bn:00057522n', 
 'bn:00007961n', 'bn:00078306n', 'bn:00082043n', 'bn:00075926n', 
 'bn:00008503n', 'bn:00009726n', 'bn:14987182n', 'bn:00013578n', 
 'bn:00015129n'].....}"""
def get_senses_dictionary(word_list):
    senses_for_words = dict()
    file = open("utils/SemEval17_IT_senses2synsets.txt","r",encoding="utf8")
    lines = file.readlines()
    for i in range(0,len(lines)):
        line = lines[i]
        line = line.replace("\n", "").replace("#","")
        if line in word_list:
            while True:
                i += 1
                babel_synset = lines[i].replace("\n", "")
                if "#" in babel_synset: #vuol dire che non sto considerando più un babel synset
                    break
                if line not in senses_for_words:
                    senses_for_words[line] = [babel_synset]
                else:
                    senses_for_words[line].append(babel_synset)
    return senses_for_words
                
                
#crea un dizionario delle annotazioni, in cui ad ogni coppia di parole
#prese dal file delle annotazioni "annotations1.tsv" associa il valore
#di similarità annotato da un essere umano
"""es: un estratto {('terremoto', 'scossa'): '3.4', ('patrimonio', 'azione'): 
                 '0.3', ('ebreo', 'Gerusalemme'): '2.0', 
                 ('nuvolosità', 'previsione'): '1.2', 
                 ('dizionario', 'enciclopedia'): '3.1'....}"""   
    
def get_human_similarities_dictionary():
    human_similarities = dict()
    annotations_file = open("annotations/annotations1.tsv")
    read_tsv = csv.reader(annotations_file, delimiter="\t")
    for row in read_tsv:
        if row: #verifico che non sia una riga vuota (può capitare)
            human_similarities[(row[0],row[1])] = row[2]
    annotations_file.close()
    return human_similarities


#restituisce tutte le parole presenti nella coppie valutate nel dizionario
#delle annotazioni umane che viene dato in input        
def get_word_list(human_similarities_dictionary):
    word_list = []
    for pair in human_similarities_dictionary.keys():
        word_list.append(pair[0])
        word_list.append(pair[1])
    return word_list

#crea una dizionario che associa ad ogni coppia di parole del dizionario
#delle annotazioni umane, un valore di similarità dato dalla massimizzazione della similarità
#del coseno tra l'insieme dei vettori nasari associati ad una parola
#e l'insieme dei vettori nasari associati all'altra parola
def get_NASARI_similarities_dictionary(human_similarities_dictionary,senses_dictionary):
    similarity_dictionary = dict()
    for word_pair in human_similarities_dictionary:
        
        try:
            word1_senses = senses_dictionary[word_pair[0]]
            word2_senses = senses_dictionary[word_pair[1]]
              
            word1_vectors = get_NASARI_vectors(word1_senses)
            word2_vectors = get_NASARI_vectors(word2_senses)
        
            similarity_value = max_cosine_similarity(word1_vectors,word2_vectors)
        
            similarity_dictionary[word_pair] = similarity_value
        
        except KeyError: #una delle due parole della coppia non c'è nel file "SemEval17_IT_senses2synsets.txt"
            print("La coppia ", word_pair, "non e' stata valutata")
            
    return similarity_dictionary
        
#cerca un vettore NASARI per ogni babel syset
#associato ad una parola (word). restituisce l'insieme dei
#vettori NASARI trovati nel file "mini_NASARI.tsv"
def get_NASARI_vectors(word_senses):
   word_vectors = list()
    
   NASARI_file = open("utils/mini_NASARI.tsv")
   read_tsv = csv.reader(NASARI_file, delimiter="\t")
   
   for row in read_tsv:
       babel_synset = row[0].split("__")[0]
       if babel_synset in word_senses:
           vector = [float(val) for val in row[1:]]
           word_vectors.append(vector)
   
   NASARI_file.close()
   return word_vectors

#massimizza la cosine_similarity tra due vettori distribuzionali 
def max_cosine_similarity(word_vector1,word_vectors2):
    max_cos_similarity = 0
    for vector1 in word_vector1:
        for vector2 in word_vectors2:
            cos_similarity = spatial.distance.cosine(vector1, vector2)
            if cos_similarity > max_cos_similarity:
                max_cos_similarity = cos_similarity
    return max_cos_similarity
        
          
human_similarities_dictionary = get_human_similarities_dictionary()
senses_dictionary = get_senses_dictionary(get_word_list(human_similarities_dictionary))
print(get_NASARI_similarities_dictionary(human_similarities_dictionary, senses_dictionary))

            
    