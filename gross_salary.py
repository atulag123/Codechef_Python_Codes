# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:24:23 2020

@author: ATUL AGARWAL
"""

#gross salary

t=int(input())
for i in range(t):
    i=int(input())
    if i < 1500:
        res = (i*0.1)+(i*0.9) + i
        print(res)
    else:
        res = 500+(i*0.98) +i
        print(res)