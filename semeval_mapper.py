#!/usr/bin/env python
# coding: utf-8

# #### Mappa un cognome su uno dei 10 insiemi di coppie da annotare
# 
# assegnare la variabile `input_name` con il proprio cognome

# In[1]:


import hashlib
import matplotlib.pyplot as plt


def get_range(surname):
    nof_elements = 500
    base_idx = (abs(int(hashlib.sha512(surname.encode('utf-8')).hexdigest(), 16)) % 10)
    idx_intervallo = base_idx * 50+1
    return idx_intervallo
 

input_name = "Altamura"

values = []
sx = get_range(input_name)
values.append(sx)
dx = sx+50-1
intervallo = "" + str(sx) + "-" + str(dx)
print('{:15}:\tcoppie nell\'intervallo {}'.format(input_name, intervallo))





