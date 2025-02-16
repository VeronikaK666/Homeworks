# Задача "Потоки гостей в кафе":
from threading import Thread
from time import sleep
from random import randint
from queue import Queue
# Необходимо имитировать ситуацию с посещением гостями кафе.

# Создайте 3 класса: Table, Guest и Cafe.

# Класс Table:
# Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# Объекты этого класса должны создаваться следующим способом - Table(1)


class Table:
    def __init__(self, number: int):
        self.number = number  # атрибут number - номер стола
        self.guest = None  # атрибут guest - гость, который сидит за этим столом (по умолчанию None)


# Класс Guest:
# Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
class Guest(Thread):  # Должен наследоваться от класса Thread (быть потоком).
    def __init__(self, name: str):
        super().__init__()
        self.name = name  # Атрибут name - имя гостя.

    def run(self):
        # Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
        sleep(randint(3, 10))

# Класс Cafe:
# Cafe - кафе, в котором есть определённое кол-во столов
# и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
# Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)


class Cafe:
    def __init__(self, *tables: Table):
        self.tables = tables  # атрибут tables - столы в этом кафе (любая коллекция).
        self.queue = Queue()  # атрибут queue - очередь (объект класса Queue)

    def is_vacant(self):
        # если кафе пустое
        return not any(t.guest for t in self.tables)

# Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).

# Метод guest_arrival(self, *guests):
# Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest),
# запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
# Если же свободных столов для посадки не осталось,
# то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
    def guest_arrival(self, *guests: Guest):  # прибытие гостей
        for guest in guests:
            vacant_table_found = False
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    vacant_table_found = True
                    break
            if not vacant_table_found:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
# Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
# то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
# Так же текущий стол освобождается (table.guest = None).
# Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None),
# то текущему столу присваивается гость взятый из очереди (queue.get()).
# Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
# Далее запустить поток этого гостя (start)

    def discuss_guests(self):
        while not (self.queue.empty() and self.is_vacant()):
            for table in self.tables:
                if not table.guest:
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди',
                              f'и сел(-а) за стол номер {table.number}')
                        table.guest.start()
                else:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
#


if __name__ == '__main__':
    tables = [Table(number) for number in range(1, 6)]  # Создание столов
    # Имена гостей
    guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()

# Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
#
# Maria сел(-а) за стол номер 1
#
# Oleg сел(-а) за стол номер 2
#
# Vakhtang сел(-а) за стол номер 3
#
# Sergey сел(-а) за стол номер 4
#
# Darya сел(-а) за стол номер 5
#
# Arman в очереди
#
# Vitoria в очереди
#
# Nikita в очереди
#
# Galina в очереди
#
# Pavel в очереди
#
# Ilya в очереди
#
# Alexandra в очереди
#
# Oleg покушал(-а) и ушёл(ушла)
#
# Стол номер 2 свободен
#
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
#
# .....
#
# Alexandra покушал(-а) и ушёл(ушла)
#
# Стол номер 4 свободен
#
# Pavel покушал(-а) и ушёл(ушла)
#
# Стол номер 3 свободен

