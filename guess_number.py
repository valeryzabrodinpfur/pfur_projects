import random

def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Попытка {attempts + 1}/{max_attempts}. Ваш вариант: "))
            
            if guess < secret_number:
                print("Загаданное число больше!")
            elif guess > secret_number:
                print("Загаданное число меньше!")
            else:
                print(f"Поздравляю! Вы угадали число за {attempts + 1} попыток!")
                return
                
            attempts += 1
        except ValueError:
            print("Пожалуйста, вводите только целые числа!")
    
    print(f"Увы! Вы не угадали. Загаданное число было: {secret_number}")

# Запуск игры
guess_number()
