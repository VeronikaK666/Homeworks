# Класс исключений IncorrectVinNumber,
# объект которого обладает атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

#  Класс исключений IncorrectCarNumbers,
#  объект которого обладает атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Класс Car обладает следующими свойствами:
class Car:

    def __init__(self, model, vin, numbers):
        # Атрибут объекта model - название автомобиля (строка):
        self.model = model
        # Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private:
        self.__vin = vin
        # # Атрибут __numbers - номера автомобиля (строка).
        self.__numbers = numbers
        # Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
        #  (в __init__ при объявлении атрибутов __vin и __numbers).
        if not self.__is_valid_vin(self.__vin):
            # Для выбрасывания исключений используем оператор raise
            raise IncorrectVinNumber("Некорректный тип vin номер или неверный диапазон для vin номера")
        if not self.__is_valid_numbers(self.__numbers):
            # Для выбрасывания исключений используем оператор raise
            raise IncorrectCarNumbers("Некорректный тип данных для номеров или неверная длина номера")

    # Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
    # Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    def __is_valid_vin(self, vin_number):
        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
        # если передано не целое число.
        # (тип данных можно проверить функцией isinstance).
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        # если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        # # Возвращает True, если исключения не были выброшены.
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    # Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
    # Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    def __is_valid_numbers(self, numbers):
        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        # если передана не строка.
        # (тип данных можно проверить функцией isinstance).
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
        # переданная строка должна состоять ровно из 6 символов.
        # Возвращает True, если исключения не были выброшены.
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True



# Пример выполняемого кода:
#
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
#
# Вывод на консоль:
# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера