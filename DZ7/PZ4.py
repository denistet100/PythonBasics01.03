# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

folder = r'my_project1'

dict_folder = {}


for list_folder in os.walk(folder):
    for file in list_folder[-1]:
        i = 1
        if '.' in file:
            address_file = os.path.join(list_folder[0], file)
            v_file = os.stat(address_file).st_size
            for _ in range(len(str(v_file))):
                i *= 10
            dict_folder.setdefault(i, 0)
            dict_folder[i] += 1

sorted_dict_folder = {}

sorted_key_folder = sorted(dict_folder)
for idx in sorted_key_folder:
    sorted_dict_folder[idx] = dict_folder[idx]

print(sorted_dict_folder)
