# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:25:37 2020

@author: ATUL AGARWAL
"""


#puppy and sum
    
t=int(input())
for i in range(t):
    lis=list(map(int,input().split()))
    for u in range(lis[0]):
        a=[]
        for j in range(1,lis[1]+1):
            a.append(j)
        z=sum(a)
        print(z)  