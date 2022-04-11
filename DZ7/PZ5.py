# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
# а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
#
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.


import os

folder = r'my_project1'

dict_folder = {}


for list_folder in os.walk(folder):
    for file in list_folder[-1]:
        i = 1
        list_extension = []
        if '.' in file:
            address_file = os.path.join(list_folder[0], file)
            v_file = os.stat(address_file).st_size
            for _ in range(len(str(v_file))):
                i *= 10
            dict_folder.setdefault(i, [0, list_extension])
            list_extension = dict_folder[i][1]
            list_extension.append(os.path.splitext(file)[1])
            list_extension = list(set(list_extension))
            dict_folder[i] = (dict_folder[i][0]+1, list_extension)

sorted_dict_folder = {}

sorted_key_folder = sorted(dict_folder)
for idx in sorted_key_folder:
    sorted_dict_folder[idx] = dict_folder[idx]

print(sorted_dict_folder)
