# Дано 2 списка:
#
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Необходимо создать 2 генераторных сборки:
# В переменную first_result запишите генераторную сборку,
# которая высчитывает разницу длин строк из списков first и second, если их длины не равны.
# Для перебора строк попарно из двух списков используйте функцию zip.
first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))

# В переменную second_result запишите генераторную сборку,
# которая содержит результаты сравнения длин строк в одинаковых позициях из списков first и second.
# Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
second_result2 = (len(first[i]) != len(second[i]) for i in range(len(first)))

# Пример результата выполнения программы:

print(list(first_result))
print(list(second_result))
print(list(second_result2))

#
# Вывод в консоль:
# [1, 2]
# [False, False, True]
