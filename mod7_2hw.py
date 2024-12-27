# Создайте функцию custom_write(file_name, strings), которая принимает аргументы:
# file_name - название файла для записи,
# strings - список строк для записи.
def custom_write(file_name, strings):
    # Создаем пустой словарь strings_positions
    strings_positions = {}

    # для чтения и записи информации из/в файл потребуется кодировка utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1): # Функция enumerate() принимает два параметра: iterable и start.
            # Для получения номера байта начала строки используется метод tell() перед записью.
            position = file.tell()  # Это текущая позиция в файле
            # Функция записывает в файл file_name все строки из списка strings, каждая на новой строке - \n.
            file.write(string + '\n')  # Записываем строку и переходим на новую строку
            # Создаем словарь strings_positions, где ключом будет кортеж:
            # (i = <номер строки>, position = <байт начала строки>),
            # а значением - записываемая строка = string.
            strings_positions[(i, position)] = string  # Добавляем информацию о строке в словарь

    # Возвращаем словарь strings_positions
    return strings_positions


# Пример использования:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)