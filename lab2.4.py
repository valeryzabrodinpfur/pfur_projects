import re

# Регулярные выражения
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
capital_word_pattern = r'\b[A-Z][a-zA-Z]+\b'

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    capital_words = re.findall(capital_word_pattern, text)

    # Сохранение результатов
    with open('emails.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(emails))

    with open('phones.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(phones))

    with open('capital_words.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(capital_words))

except FileNotFoundError:
    print("Ошибка: файл text.txt не найден.")
