def generate_password(param):
    result = ""
    for i in range(1, param):
        for j in range(i + 1, param + 1):
            if param % (i + j) == 0:
                result += str(i) + str(j)
    return result
param = int(input("Введи число, путник!: "))
password = generate_password(param)
if param < 3 or param > 20:
    print("Не пойдёт, должны быть числа от 3 до 20")
else:
    print(password)

import random

def number():
    list_ = list(range(3, 20))
    case = random.choice(list_)
    return case