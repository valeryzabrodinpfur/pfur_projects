# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:11:21 2025

@author: 1032242353
"""

def divide_numbers():
    try:

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        result = num1 / num2
        
        print("Результат деления: " + result)
    
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    
    except ValueError:
        print("Ошибка: введено нечисловое значение.")

divide_numbers()
