# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:24:59 2020

@author: ATUL AGARWAL
"""


#similar pair

a=[]
t=int(input())
for i in range(t):
    i=int(input())
    lis=list(map(int,input().split()))
    lis.sort()
    for u in range(len(lis)-1):
        res=lis[u]+lis[u+1]
        a.append(res)
    print(a[0])
