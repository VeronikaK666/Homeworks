

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.new_floor = new_floor

        if self.number_of_floors >= self.new_floor and self.new_floor >= 1:
            print(f'Едем на этаж {new_floor}')
        else:
            print('Такого этажа не существует')


building = House('Elbrus', 30)

building.go_to(1)