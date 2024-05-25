#module fake_math
def divide():
    try:
        first = int(input("Введите делимое: "))
        second = int(input("Введите делитель: "))
        result = first / second
    except ZeroDivisionError:
        return "Ошибка"
    return result


print("Результат деления: ", divide())


#module true_math
from math import inf

def divide():
    try:
        first = int(input("Введите делимое: "))
        second = int(input("Введите делитель: "))
        result = first / second
    except ZeroDivisionError:
        result = inf
    return result


print("Результат деления: ", divide())

#module main
from fake_math import divide as f1
f1()
from true_math import divide as f2
f2()

