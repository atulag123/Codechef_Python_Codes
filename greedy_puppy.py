# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:22:52 2020

@author: ATUL AGARWAL
"""


#GREEDY PUPPY

t=int(input())
for i in range(t):
    lis=list(map(int,input().split()))
    print(lis[0]%lis[1])
