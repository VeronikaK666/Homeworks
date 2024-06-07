class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors
        # self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.floors = self.numberOfFloors
        print(self.numberOfFloors)

my_house = House(1)
my_house.setNewNumberOfFloors(0)