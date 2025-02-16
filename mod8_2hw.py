# Функция personal_sum(numbers): принимает коллекцию numbers.
def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            # Подсчитываем сумму чисел в numbers путём перебора и увеличиваем переменную result.
            result += i
            # print(result)
        # Если же при переборе встречается даннsе типа отличного от числового,
        # то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы {exc} - {i}')
    # # В конечном итоге функция возвращает кортеж из двух значений:
    # # result - сумма чисел, incorrect_data - кол-во некорректных данных.
    return result, incorrect_data


# Функция calculate_average(numbers):
# принимает коллекцию numbers и возвращать: среднее арифметическое всех чисел.
def calculate_average(numbers):
    try:
        #  Внутри для подсчёта суммы используем функцию personal_sum, написанную ранее.
        total_sum, incorrect_data = personal_sum(numbers)
        # Count - количество чисел в numbers с учётом некорректных данных.
        count = len(numbers) - incorrect_data
        # Возврат суммы чисел total_sum, делённой на их количество count.
        # Если чисел 0 возвращает 0.
        return total_sum / count if count != 0 else 0
    # Т.к. коллекция numbers может оказаться пустой,
    # то обрабатываем исключение ZeroDivisionError при делении на 0 и вовзвращаем 0.
    except ZeroDivisionError:
        return 0
    # Обрабатываем исключение TypeError, выводя строку: 'В numbers записан некорректный тип данных'.
    # В таком случае функция просто вернёт None.
    except TypeError as exc:
        print(f'В numbers записан некорректный тип данных - {exc}')
        return None

# Пример выполнения программы:
#
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
#
#
#
# Вывод на консоль:
# Некорректный тип данных для подсчёта суммы - 1
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 2
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 3
# Результат 1: 0
# Некорректный тип данных для подсчёта суммы - Строка
# Некорректный тип данных для подсчёта суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5