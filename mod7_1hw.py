class Product:
# Объекты этого класса обладают следующими атрибутами:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name # название продукта
        self.weight = weight # общий вес товара
        self.category = category # категория товара

# И методом, который возвращает строку в формате '<название>, <вес>, <категория>'.
# Все данные в строке разделены запятой с пробелами.
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    # Инкапсулированный атрибут:
    __file_name = 'products.txt'

    # Метод, который считывает всю информацию из файла __file_name,
    # закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
    def get_products(self):
        # обращение к чтению файла products.txt (self.__file_name)
        get_file = open('products.txt', 'r')
        name_prods = get_file.read()
        get_file.close()
        # возвращение работы метода self.get_products()
        return name_prods

    #Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
    # Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
    # Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
    def add(self, *products):
        # цикл перебора наименований product в products
        for product in products:
            # условие проверки, когда product нет в списке products.txt
            if str(product) not in self.get_products():
                # добавление отсутствующего product в файл products.txt
                file = open('products.txt', 'a+')
                file.write(f'{str(product)}\n')
                file.close()
            # когда запись product уже есть в файле products.txt
            else:
                print(f'Продукт {product} уже есть в магазине')

# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


