import math

class Figure:

    sides_count = 0 # Атрибут класса Figure
    # Каждый объект класса Figure должен обладать следующими атрибутами:
    # -Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
    # -Атрибуты(публичные): filled(закрашенный, bool)
    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = self.__is_filled()  # Устанавливает значение атрибута filled.

    def get_color(self): # Метод возвращает список RGB цветов.
        return self.__color

    def __is_valid_color(self, r, g, b):
        # Этот метод служебный, принимает параметры r, g, b, который проверяет корректность
        # переданных значений перед установкой нового цвета. Корректный цвет: все значения r, g и b - целые числа
        # в диапазоне от 0 до 255 (включительно).
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        # Этот метод принимает параметры r, g, b - числа и изменяет атрибут __color
        # на соответствующие значения, предварительно проверив их на корректность.
        # Если введены некорректные данные, то цвет остаётся прежним.
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = self.__is_filled()

    def __is_filled(self):
        # Этот метод проверяет, установлен ли цвет фигуры в значение, отличное от (0, 0, 0).
        return self.__color != [0, 0, 0]

    def __is_valid_sides(self, *sides):
        # Этот метод служебный, принимает неограниченное кол-во сторон, возвращает True
        # если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False -
        # во всех остальных случаях.
        # Также метод __is_valid_sides проверяет, что все стороны являются положительными целыми числами
        # и их количество len(sides) совпадает с sides_count.
        return all(isinstance(s, int) and s > 0 for s in sides) and len(sides) == self.sides_count

    def get_sides(self): # Этот метод должен возвращать значение атрибута __sides.
        return self.__sides

    def __len__(self): # Этот метод должен возвращать периметр фигуры (сумма сторон)
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        # Этот метод должен принимать новые стороны,
        # если их количество не равно sides_count, то не изменять,
        # в противном случае - менять.
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure): # Наследует все атрибуты и методы класса Figure
    sides_count = 1  # Атрибут класса

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        # Если количество сторон не соответствует изначальным данным, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(1)
        # Атрибут __radius рассчитывается исходя из длины окружности (одной единственной стороны).
        # Радиус = Длина_окружности / (2 * 3,14)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    def get_square(self):
        # Метод get_square возвращает площадь круга (можно рассчитать как через длину,
        # так и через радиус).
        # Считаем так: Площадь_круга = 3,14 * Радиус ^ 2
        return math.pi * (self.__radius ** 2)


class Triangle(Figure): # Наследует все атрибуты и методы класса Figure
    sides_count = 3  # Атрибут класса

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        # Если количество сторон не соответствует изначальным данным, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))
        # Введём атрибут __height - высота треугольника (можно рассчитать, зная все стороны треугольника).
        self.__height = self.__calculate_height()

    def get_height(self):  # Метод для получения высоты треугольника
        return self.__height

    def __calculate_height(self):   # Метод для вычисления высоты треугольника по формуле Герона.
        first, second, third = self.get_sides() # Стороны треугольника
        half_of_per = sum([first, second, third]) / 2  # Полупериметр
        # Считаем площадь треугольника:
        area = math.sqrt(half_of_per * (half_of_per - first) * (half_of_per - second) * (half_of_per - third))
        return 2 * area / first  # Высота = 2 * Площадь_треугольника / Основание


    def get_square(self): # Метод get_square возвращает площадь треугольника: 0,5 * Основание * Высота
        first, _, _ = self.get_sides()
        return 0.5 * first * self.__height


class Cube(Figure): # Наследует все атрибуты и методы класса Figure
    sides_count = 12 # Атрибут класса

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)
        # Если количество сторон не соответствует изначальным данным, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))

    def get_volume(self): # Метод возвращает объём куба.
        side_length = self.get_sides()[0]
        return side_length ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма куба
print(cube1.get_volume())  

