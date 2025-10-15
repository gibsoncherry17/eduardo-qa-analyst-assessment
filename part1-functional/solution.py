#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 14:03:09 2025

@author: chedm
"""

def remove_duplicates(s):           #Create new function remove_duplicates()
    new_list = []                   #Define empty list called new_list
    for d in s:                     #Use for loop to iterate through each num in s
       if d not in new_list:
            new_list.append(d)      #If d is already in new_list, it's a duplicate and won't be added
    return new_list


f = [1, 2, 3, 2, 4, 1, 5]
g = [1, 1, 1]
h = []
i = [30, 56, 76, 68, 30, 69, 100, 100]

print(remove_duplicates(f))
print(remove_duplicates(g))
print(remove_duplicates(h))
print(remove_duplicates(i))




