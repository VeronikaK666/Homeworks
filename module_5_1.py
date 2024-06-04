
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