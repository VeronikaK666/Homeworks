#fake_math
def divide():
    try:
        first = int(input("Введите делимое: "))
        second = int(input("Введите делитель: "))
        result = first / second
    except ZeroDivisionError:
        return "Ошибка"
    return result


print("Результат деления: ", divide())