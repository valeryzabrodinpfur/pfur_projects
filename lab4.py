# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:20:28 2025

@author: 1032242353
"""
import random
randlist = [random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50),random.randint(1,50)]
maxnum = 0
minnum = 500
totalsum = 0
print(randlist)
for i in randlist:
    if i > maxnum:
        maxnum = i
    if i < minnum:
        minnum = i
    totalsum += i
sortlist = randlist.sort()
print(maxnum)
print(minnum)
print(totalsum)

'''
randlist = []
for i in range(10):
    randlist.append(random.randint(1,50))
    
print(randlist)
'''