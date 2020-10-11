# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:21:51 2020

@author: ATUL AGARWAL
"""

#RECTANGLES
t=int(input())
for i in range(t):
    lis=list(map(int,input().split()))
    lis.sort()
    if lis[0]==lis[1] and lis[2]==lis[3]:
        print("YES")
    else:
        print("NO")