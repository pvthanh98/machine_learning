#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
# In[12]:



def preprocessing(file):
    data = pd.read_csv(file)
    names = ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health', 'application']
    encoder = {}
    for name in names:
        lbEncode = LabelEncoder()
        lbEncode.fit(data[name])
        encoder[name] = lbEncode
        print(data[name])
        data[name] = lbEncode.transform(data[name])
    return data, encoder

data1 , encoder = preprocessing('nursery.csv')