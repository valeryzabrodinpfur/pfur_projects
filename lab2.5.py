numbers = list(range(1, 21))

# 1. Фильтрация чётных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 2. Увеличение каждого числа на 10
incremented_numbers = list(map(lambda x: x + 10, numbers))

# 3. Сортировка по убыванию
sorted_numbers = sorted(numbers, key=lambda x: -x)  # или key=lambda x: x, reverse=True

# Вывод результатов
print("Чётные числа:", even_numbers)
print("Числа +10:", incremented_numbers)
print("Сортировка по убыванию:", sorted_numbers)
