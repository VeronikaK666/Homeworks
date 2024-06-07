# Недостатки:
# Метод `go_to` должен принимать параметр `new_floor`, а не запрашивать его у пользователя внутри метода.
# Внутри `go_to` не используется переданный в конструктор `number_of_floors`, вместо этого значение жёстко задаётся (`self.number_of_floors = 30`).
# Отсутствие вывода этажей: Метод `go_to` не выводит на экран номера этажей от 1 до `new_floor`, как требуется в задании.
# Избыточный вызов `int()`:В условии `if` уже выполняется сравнение с целым числом 1, поэтому `int(new_floor) >= 1` избыточно.
#
# Рекомендации:
# 1. Передавать `new_floor` как параметр метода `go_to`.
# 2. Использовать переданный в конструктор `number_of_floors` для проверки допустимости этажа.
# 3. Добавить вывод номеров этажей в методе `go_to`.
# 4. Убрать избыточный вызов `int()` в условии `if`.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self):
        new_floor = input('Введите номер этажа')
        self.number_of_floors = 30
        if self.number_of_floors >= int(new_floor) and int(new_floor) >= 1:
            print(f'Едем на этаж {new_floor}')
        else:
            print('Такого этажа не существует')


building = House('Elbrus', 30)

building.go_to()