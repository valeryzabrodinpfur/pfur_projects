     # -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

a = int(input("1st input int: "))
b = int(input("2nd input int: "))
c = int(input("3rd input int: "))

if a == b and b == c:
    print("The numbers are all equal")

elif a > b and a > c:
    print(a + 'is the largest value')

elif c > b and a < c:
    print(c + 'is the largest value')

elif a < b and b > c:
    print(b + 'is the largest value')

