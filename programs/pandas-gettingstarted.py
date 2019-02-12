# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:47:44 2018

@author: Raghu Prasad
"""

import pandas as pd

print("Hi! This is a cell. Press the ▶ button above to run it");

def print_10_nums():
    for i in range(10):
        print(i)

print_10_nums();

sum([x for x in range(100000)])