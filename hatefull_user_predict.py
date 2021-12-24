# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 22:43:45 2021

@author: amitr
"""

import numpy as np
import pandas as pd


#load the dataset
dataset = pd.read_csv(r'users_neighborhood_anon.csv')

x = dataset.iloc[:,2:].values
y = dataset.iloc[:,1].values