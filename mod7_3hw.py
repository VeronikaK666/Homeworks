import string


class WordsFinder:
    def __init__(self, *file_names):
        # неограниченное количество названий файлов
        # записывается в атрибут file_names в виде списка или кортежа.
        self.file_names = file_names

    def get_all_words(self):
        #  подготовительный метод, который возвращает словарь следующего вида:
        #  названия файлов и списки слов из них.
        all_words = {}  # Создаем пустой словарь для хранения результатов

        # Задаем список символов для удаления
        chars_to_remove = list(string.punctuation + ' -')  # Правим пунктуацию и пробелы

        for file_name in self.file_names:  # Перебираем названия файлов
            try:
                with open(file_name, 'r', encoding='utf-8') as file:  # Открываем файл для чтения
                    # Читаем содержимое файла и переводим в нижний регистр, используя метод lower()
                    text = file.read().lower()

                    # Удаляем нежелательные символы
                    for char in chars_to_remove:
                        text = text.replace(char, " ")  # Заменяем каждый символ на пробел

                    # Разбиваем текст на слова по пробелам
                    words = text.split()  # Разбиваем текст на слова по пробелам методом split()

                    # Записываем в словарь: имя файла - список слов
                    all_words[file_name] = words

            except FileNotFoundError: # Исключаем ошибки, если файл не найден
                print(f"Файл {file_name} не найден.")

        return all_words  # Возвращаем словарь со всеми словами

    def find(self, word):
        #  метод, где word - искомое слово.
        #  Возвращает словарь, где ключ - название файла,
        #  значение - позиция первого такого слова в списке слов этого файла.
        word_positions = {}  # Словарь для хранения позиций искомого слова

        for file_name, words in self.get_all_words().items():  # Получаем все слова из файлов
            if word.lower() in words:  # Проверяем наличие слова в нижнем регистре
                position = words.index(word.lower())  # Находим позицию первого вхождения слова
                word_positions[file_name] = position  # Сохраняем позицию

        return word_positions  # Возвращаем словарь с позициями

    def count(self, word):
        #  метод, где word - искомое слово.
        #  Возвращает словарь, где ключ - название файла,
        #  значение - количество слова word в списке слов этого файла.
        word_counts = {}  # Словарь для хранения количества искомого слова

        for file_name, words in self.get_all_words().items():  # Получаем все слова из файлов
            count = words.count(word.lower())  # Подсчитываем количество вхождений слова
            if count > 0:  # Если слово встречается хотя бы один раз
                word_counts[file_name] = count  # Сохраняем количество вхождений

        return word_counts  # Возвращаем словарь с количеством


# Создаем тестовый файл test_file.txt с примером текста
with open('test_file.txt', 'w', encoding='utf-8') as f:
    f.write("It's a text for task Найти везде. Используйте его для самопроверки. Успехов в решении задачи!\n")
    f.write("text text text\n")

# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')  # Создаем объект класса с указанием файла

# Получаем все слова из файла
print(finder2.get_all_words())
# Вывод на консоль: {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти',
#                                    'везде', 'используйте', 'его', 'для',
#                                    'самопроверки', 'успехов', 'в',
#                                    'решении', 'задачи!',
#                                    'text', 'text', 'text']}

# Ищем слово 'TEXT' и выводим его позицию
print(finder2.find('TEXT'))
# Вывод на консоль: {'test_file.txt': 3} - 3 слово по счёту

# Подсчитываем количество вхождений слова 'teXT' и выводим результат
print(finder2.count('teXT'))
# Вывод на консоль: {'test_file.txt': 4} - 4 слова teXT в тексте всего
