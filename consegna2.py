#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:41:55 2021

@author: santealtamura
"""
import utils

def main():
    human_similarities_dictionary = utils.get_human_similarities_dictionary()
    
    senses_dictionary = utils.get_senses_dictionary(utils.get_word_list(human_similarities_dictionary))
    
    human_synsets_dictionary = utils.get_human_synsets_dictionary()
    
    word_pair_synset_pair_dictionary = utils.get_word_pair_synset_pair_dictionary(human_synsets_dictionary, senses_dictionary)
    
    print()
    print("ASSEGNAMENTI SYNSETS UMANI: ")
    print(human_synsets_dictionary)
    print()
    print("'ASSEGNAMENTI SYNSETS DEL SISTEMA: ")
    print(word_pair_synset_pair_dictionary)
    
    print()
    #calcolo accuratezza sui singoli elementi
    checked = 0
    for word_pair in human_synsets_dictionary.keys():
        synset_pair = word_pair_synset_pair_dictionary[word_pair]
        human_synsets_pair = human_synsets_dictionary[word_pair]
        if synset_pair[0] == human_synsets_pair[0]:
            checked += 1
        if synset_pair[1] == human_synsets_pair[1]:
            checked += 1
    evaluated = len(human_synsets_dictionary.keys()) * 2
    print("Accuratezza sui singoli elmenti: ", checked / evaluated)
            
        
    
    #calcolo accuratezza sulle coppie
    checked = 0
    for word_pair in human_synsets_dictionary.keys():
        synset_pair = word_pair_synset_pair_dictionary[word_pair]
        human_synsets_pair = human_synsets_dictionary[word_pair]
        if (synset_pair[0] == human_synsets_pair[0]) and (synset_pair[1] == human_synsets_pair[1]):
            checked += 1
    evaluated = len(human_synsets_dictionary.keys())
    print("Accuratezza sulle coppie: ", checked / evaluated)

main()