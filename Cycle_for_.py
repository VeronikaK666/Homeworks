cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(len(cars)):
    cars_count += 10
    print("Я езжу на автомобиле марки ", cars[i])

    print(cars_count)

#или так?

cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in range(len(cars)):
    print("Я езжу на автомобиле марки ", cars[i])

cars_count = 0
for i in range(len(cars)):
    cars_count += 10
    print(cars_count)

