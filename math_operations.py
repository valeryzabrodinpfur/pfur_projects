# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:13:50 2025

@author: 1032242353
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"
