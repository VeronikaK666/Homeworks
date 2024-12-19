class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # атрибут класса

    def __init__(self, owner, model, color, engine_power): # каждый объект Vehicle содержит следующие атрибуты объекта
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    # каждый объект Vehicle содержит следующие методы:
    def get_model(self): # возвращает строку: "Модель: <название модели транспорта>"
        return f'Модель: {self.__model}'

    def get_horsepower(self): # возвращает строку: "Мощность двигателя: <мощность>"
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self): # возвращает строку: "Цвет: <цвет транспорта>"
        return f'Цвет: {self.__color}'

    def print_info(self): # распечатывает результаты методов, а так же владельца в конце в формате "Владелец: <имя>"
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец:', self.owner)

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle): # Класс наследника для Vehicle
    __PASSENGERS_LIMIT = 5 # атрибут класса


# Пример результата выполнения программы:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos','Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

