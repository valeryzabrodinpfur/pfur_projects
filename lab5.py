# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:35:31 2025

@author: 1032242353
"""
import random
randlist = []
list_even = []
list_divisible3 = []
avg = 0

for i in range(20):
    randlist.append(random.randint(1,100))




for i in randlist:
    if i % 2 == 0:
        list_even.append(i)
    if i % 3 == 0:
        list_divisible3.append(i)
    avg += i
avg /= 20
print(randlist)
print(list_even)
print(list_divisible3)
print(avg)
        
