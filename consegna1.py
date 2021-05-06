#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:05:39 2021

@author: santealtamura
"""

import utils
import numpy as np
import scipy as sp
import scipy.stats

def main():
    human_similarities_dictionary = utils.get_human_similarities_dictionary()
    
    senses_dictionary = utils.get_senses_dictionary(utils.get_word_list(human_similarities_dictionary))
    
    NASARI_similarities_dictionary = utils.get_NASARI_similarities_dictionary(human_similarities_dictionary, senses_dictionary)

    human_similarities = []
    NASARI_similarities = []
    for word_pair in human_similarities_dictionary.keys():
        if word_pair in NASARI_similarities_dictionary.keys():
            human_similarities.append(float(human_similarities_dictionary[word_pair]))
            NASARI_similarities.append(NASARI_similarities_dictionary[word_pair])
    
    print()
    print("VALUTAZIONI DI SIMILARITA' UMANE: ")
    print(human_similarities_dictionary)
    print()
    print("VALUTAZIONI DI SIMILARITA' DEL SISTEMA: ")
    print(NASARI_similarities_dictionary)
    
    
    print()
    print("Pearson Correlation: ",np.corrcoef(human_similarities, NASARI_similarities))
    print()
    print("Spearman Correlation: ",sp.stats.spearmanr(human_similarities, NASARI_similarities))

main()
    