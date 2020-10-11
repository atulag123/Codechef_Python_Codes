# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:21:03 2020

@author: ATUL AGARWAL
"""

#Is it a VOWEL or CONSONANT

v=['a','e','i','o','u','A','E','I','O','U']
t=input()
for i in range(len(v)):
    if (v[i]==t):
        print("Vowel")
else:
    print("Consonant")