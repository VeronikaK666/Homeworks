#true_math
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
