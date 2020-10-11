# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:20:33 2020

@author: ATUL AGARWAL
"""

#area or perimeter

l=int(input())
b=int(input())
area=l*b
peri=2*(l+b)
if (area>peri):
    print("Area")
    print(area)
elif (peri>area):
    print("Peri")
    print(peri)
else:
    print("Eq")
    print(area)