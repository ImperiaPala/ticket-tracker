from ticket import Ticket
from storage import TicketStorage
import time
from helpers import priority
import os

os.makedirs('data', exist_ok=True)
s = TicketStorage('data/tickets.json')
s.load()

while True:
    print(f'-----------------\n Ticket Tracker\n-----------------\n1. Создать заявку\n2. Показать всё\n3. Сменить статус\n4. Удалить\n5. Выход')
    try:
        choice = int(input('> '))
        if not 1 <= choice <= 5:
            raise ValueError
    except ValueError:
        print('Неверный выбор')
        time.sleep(1)
        continue
    if choice == 5:
        break
    elif choice == 4:
        if not s.tickets:
            print('Заявок нет')
            time.sleep(1)
            continue
        for i, t in enumerate(s.tickets, 1):
            print(i, t.title)
        try:
            num = int(input('Введите номер: '))
            s.delete(num - 1)
            print('Заявка удалена')
            time.sleep(1)
        except ValueError:
            print('Только числа')
            time.sleep(1)
        except IndexError:
            print('Такого номера нет')
            time.sleep(1)
    elif choice == 3:
        if not s.tickets:
            print('Заявок нет')
            time.sleep(1)
            continue
        for i, t in enumerate(s.tickets, 1):
            print(i, t.title, '-', t.status)
        try:
            num = int(input('Введите номер: '))
        except ValueError:
            print('Только числа')
            time.sleep(1)
            continue
        try:
            s.advance(num - 1)
            print('Статус заявки изменен')
            time.sleep(1)
        except ValueError as e:
            print(e)
            time.sleep(1)
        except IndexError:
            print('Такой заявки нет')
            time.sleep(1)
    elif choice == 2:
        if not s.tickets:
            print('Заявок нет')
            time.sleep(1)
        for t in s.tickets:
            print(t.get_data())
            time.sleep(0.5)
    elif choice == 1:
        title = input('Введите заголовок: ').strip()
        if not title:
            print('Заголовок не может быть пустым')
            time.sleep(1)
            continue
        description = input("Введите описание: ").strip()
        prio = priority()
        s.add(Ticket(title, description, prio))
        print('Заявка создана')
        time.sleep(0.5)