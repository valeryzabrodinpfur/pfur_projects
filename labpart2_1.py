     # -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:57:18 2025

@author: 1032242353
"""

def calculate_and_write(input_file, output_file):
    with open(input_file, 'r') as input_file:
        numbers = [int(line.strip()) for line in input_file.readlines()]
        
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
        
    with open(output_file, 'w') as output_file:
        output_file.write(f"Сумма: {total_sum}\n")
        output_file.write(f"Среднее: {average}\n")
        output_file.write(f"Максимум: {max_value}\n")
        output_file.write(f"Минимум: {min_value}\n")

input_file = 'data.txt'
output_file = 'result.txt'
calculate_and_write(input_file, output_file)
