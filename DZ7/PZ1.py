# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
# конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os


def tree_mk(folder_tree):
    for main_folder, subfolders in folder_tree.items():
        if os.path.exists(main_folder):
            print(f'folder {main_folder} exists')
        else:
            for subfolder in subfolders:
                if os.path.exists(subfolder):
                    print(f'folder {subfolder} exists')
                else:
                    os.makedirs(os.path.join(main_folder, subfolder))


folder = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

tree_mk(folder)
