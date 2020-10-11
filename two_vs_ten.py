# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:22:24 2020

@author: ATUL AGARWAL
"""

#two vs ten

for _ in range(int(input())):
    n = int(input())
    if n % 10 == 0:
        print(0)
    elif n % 5 == 0:
        print(1)
    else:
        print(-1)