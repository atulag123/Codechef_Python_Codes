# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:23:29 2020

@author: ATUL AGARWAL
"""


#GRADE THE STEEL
    
t=int(input())
for i in range(t):
    lis=list(map(float,input().split()))
    if  (lis[0]>50 and lis[1]<0.7 and lis[2]>5600):
        print("10")
    elif (lis[0]>50 and lis[1]<0.7):
        print("9")
    elif (lis[1]<0.7 and lis[2]>5600):
        print("8")
    elif (lis[0]>50 and lis[2]>5600):
        print("7")
    elif (lis[0]>50 or lis[1]<0.7 or lis[2]>5600):
        print("6")
    else:
        print("5")  