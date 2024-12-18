class Animal: #Класс родителя
    def __init__(self, name):
        self.alive = True  #Живой
        self.fed = False   #Накормленный
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant: #Класс родителя
    def __init__(self, name):
        self.edible = False  #Съедобность
        self.name = name #Индивидуальное название каждого растения


class Mammal(Animal):  #Класс наследника для Animal
    pass


class Predator(Animal): #Класс наследника для Animal
    pass


class Flower(Plant): #Класс наследника для Plant
    pass


class Fruit(Plant): #Класс наследника для Plant
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  #Переопределить при наследовании


#Объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

#Выполняемый код для проверки:
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)  #Хищник погиб
print(a2.fed)    #Млекопитающее насытилось