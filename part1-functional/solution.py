#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 14:03:09 2025

@author: chedm
"""

def remove_duplicates(s):           
    new_list = []                #Define empty list called new_list
    for d in s:                  #Use for loop to iterate through each number in s
       if d not in new_list:
            new_list.append(d)   #If d is not in new_list, it'll be added, otherwise it'll be ignored
    return new_list            

#The three example lists
f = [1, 2, 3, 2, 4, 1, 5]
g = [1, 1, 1]
h = []

#This is where to test the function for each of the 3 example lists 
print(remove_duplicates(f))
print(remove_duplicates(g))
print(remove_duplicates(h))





