from random import randint
class Building:
    total = 0
    def __init__(self, name):
        self.name = name
        self.numberOfFloors = randint(1, 40)
        Building.total +=1

    def __str__(self):
        return str(self.__dict__)


build_list = [Building('Object №'+str(i)) for i in range(1, 41)]

print(*build_list)
print('Total objects:', Building.total)