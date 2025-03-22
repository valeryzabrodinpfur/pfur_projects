# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:12:51 2025

@author: 1032242353
"""

counter = 1
n = int(input("input a number"))
list1 = []
sum = 0

while counter <= n:
    list1.append(counter)
    counter += 1

for i in list1:
    print(i)
    print(i**2)
    sum += 0
print(sum)