import os
import time

directory = os.getcwd()
pathdirectory = 'm_7_5'
if os.path.exists(pathdirectory):
    print('Директория существует')
else:
    os.mkdir(pathdirectory)
for root, dirs, files in os.walk(directory):
    # print(f'Директория: {root}')
    # print(f'Поддиректория: {dirs}')
    # print(f'Файлы: {files}')
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')