import os
import time

directory = '.'
for root, dirs, files in os.walk(directory): # os.walk - для обхода каталога, путь к к-му указывает переменная directory
    for file in files:
        filepath = os.path.join(root, file) # os.path.join - для формирования полного пути к файлам
        #os.path.getmtime и модуль time - для получения и отображения времени последнего изменения файла
        # os.path.getmtime() возвращает время последнего изменения файла в виде числа с плавающей точкой:
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        filesize = os.path.getsize(filepath) # os.path.getsize - для получения размера файла
        parent_dir = os.path.dirname(filepath) # os.path.dirname - для получения родительской директории файла
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')