# Задача "За честь и отвагу!":
from threading import Thread
from time import sleep
# Создайте класс Knight, наследованный от Thread


class Knight(Thread):
    def __init__(self, name: str, power: int, enemies: int = 100):
        super().__init__()
        self.name = name  # Атрибут name - имя рыцаря. (str)
        self.power = power  # Атрибут power - сила рыцаря. (int)
        self.enemies = enemies  # Количество врагов, у всех потоков их 100. (int)

# А также метод run, в котором рыцарь будет сражаться с врагами:

    def run(self):
        # При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
        print(f'{self.name} на нас напали!')
        days = 0
        # Рыцарь сражается до тех пор, пока не повергнет всех врагов.
        # В процессе сражения количество врагов уменьшается на power текущего рыцаря.
        while self.enemies > 0:
            self.enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days} дней, осталось {self.enemies} воинов.')
            sleep(1)  # нужно сделать задержку в 1 секунду
        # После победы над всеми врагами выводится надпись:
        # "<Имя рыцаря> одержал победу спустя <кол-во дней> дней (дня)!"
        print(f'{self.name} одержал победу спустя {days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

# Вывод на консоль:
# Sir Lancelot, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, на нас напали!
# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Galahad одержал победу спустя 5 дней(дня)!
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней(дня)!
# Все битвы закончились!
