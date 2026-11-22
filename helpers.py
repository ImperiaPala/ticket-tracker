import datetime as dt
import os


def priority():
    while True:
        try:
            num = int(input("Введите приоритет от 1 до 3: "))
        except ValueError:
            print("Только числа")
            continue
        if 1 <= num <= 3:
            return num
        print("от 1 до 3")

def log(text):
    os.makedirs('data', exist_ok=True)
    with open('data/log.txt', 'a', encoding='utf-8') as file:
        file.write(dt.datetime.now().strftime('%Y-%m-%d %H:%M ') + text + '\n')

def logged(func):
    def wrapper(*args):
        text = f'Выполняется: {func.__name__}'
        log(text)
        return func(*args)
    return wrapper
