import random # для вывода случайного числа


class Animal: # Класс обладает следующими атрибутами:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed): # Объект этого класса обладает следующими атрибутами:
        self._cords = [0, 0, 0]
        self.speed = speed

    # И методами:
    def move(self, dx, dy, dz): # меняет соответствующие кооординаты в _cords на dx, dy и dz, множетель - speed
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self): # выводит координаты: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self): # показывает степень опасности
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal): # Наследуется от Animal
    beak = True # обладает атрибутом

    def lay_eggs(self): # обладает методом
        num_of_eggs = random.randint(1, 4) # вывод случайного числа от 1 до 4
        print(f"Here are(is) {num_of_eggs} eggs for you")


class AquaticAnimal(Animal): #Наследуется от Animal
    _DEGREE_OF_DANGER = 3 # обладает атрибутом

    def dive_in(self, dz): # обладает методом
        # Этот метод должен всегда уменьшать координату z в _coords.
        # Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
        # Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
        # Ну или можно умножить на 0.5
        new_z = self._cords[2] - abs(dz) * .5 * self.speed
        self._cords[2] = max(new_z, 0)


class PoisonousAnimal(Animal): # Наследуется от Animal
    _DEGREE_OF_DANGER = 8 # обладает атрибутом


# И класс утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal:
class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click" # Объект этого класса должен обладать одним дополнительным атрибутом

    def __init__(self, speed):
        super().__init__(speed) # использовние метода super

    def speak(self): # выводит строку со звуком sound
        print(self.sound)

# Пример работы программы:
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs() # Число может быть от 1 до 4
