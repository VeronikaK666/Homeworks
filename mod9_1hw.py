# Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
# int_list - список из чисел (int, float)
# *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
def apply_all_func(int_list, *functions):
    # В функции apply_all_func создайте пустой словарь results.
    results = {}
    # Переберите все функции из *functions.
    for func in functions:
        try:
            # Функция apply_all_func(int_list, *functions) должна:
            # вызвать каждую функцию к переданному списку int_list
            # При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
            results[func.__name__] = func(int_list)
        except Exception as e:
            # Исключение может возникнуть, если функция не предназначена для работы с переданным типом данных.
            results[func.__name__] = str(e)
    # Верните словарь results.
    # Функция apply_all_func(int_list, *functions) должна:
    # Возвращать словарь, где ключом будет название вызванной функции,
    # а значением - её результат работы со списком int_list.
    return results

# Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
# Пример результата выполнения программы:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
