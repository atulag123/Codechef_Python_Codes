# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:19:06 2020

@author: ATUL AGARWAL
"""

#chef and steps

t=int(input())
for u in range(t):
    lis=list(map(int,input().split()))
    lis1=list(map(int,input().split()))
    for i in range(len(lis1)):
        if (lis1[i] % lis[1]==0):
            print("1", end="")
        else:
            print("0", end="")