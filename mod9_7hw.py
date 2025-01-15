# Напишите 2 функции:
#

# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            for i in range(2, int(result) // 2 + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return result
    return wrapper  # Функция is_prime должна возвращать wrapper


# Функция, которая складывает 3 числа (sum_three)
@is_prime  # @is_prime - декоратор для функции sum_three
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)

print(result)

# Результат консоли:
# Простое
# 11






