import random
import time
from datetime import datetime

def save_stats(attempts, duration, result):
    with open("stats.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | Попыток: {attempts} | Время: {duration:.2f} сек | Результат: {result}\n")

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуйте угадать!")
    start_time = time.time()
    while True:
        try:
            guess = int(input("Ваш вариант: "))
            attempts += 1
            if guess < number:
                print("Больше!")
            elif guess > number:
                print("Меньше!")
            else:
                duration = time.time() - start_time
                print(f"Поздравляю! Вы угадали число за {attempts} попыток и {duration:.2f} секунд.")
                save_stats(attempts, duration, "Угадал")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

def main():
    while True:
        play_game()
        again = input("Сыграть ещё раз? (д/н): ").strip().lower()
        if again != 'д':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
