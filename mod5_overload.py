class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

house1 = Building(5, 'пятиэтажка')
house2 = Building(140, 'небоскрёб')
print(house1 == house2)