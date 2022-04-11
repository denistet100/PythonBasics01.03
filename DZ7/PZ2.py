# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os
import yaml
# -------------------------------------------------------------------------------------------------------------------
tree_folder = {'my_project1': [{'settings': ['__init__.py', 'dev.py', 'prod.py']},
                              {'mainapp': ['__init__.py', 'models.py', 'views.py',
                                           {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
                              {'authapp': ['__init__.py', 'models.py', 'views.py',
                                           {'templates': [{'authapp': ['base.html', 'index.html']}]}]}]
               }

with open('config.yaml', 'w', encoding='utf-8') as tree_file:
    tree_file.write(yaml.dump(tree_folder))

# -------------------------------------------------------------------------------------------------------------


def tree_mk(folder_tree):
    for main_folder, sub_folders in folder_tree.items():
        if not os.path.exists(main_folder):
            os.mkdir(main_folder)
        os.chdir(main_folder)
        for sub_folder in sub_folders:
            if isinstance(sub_folder, dict):
                tree_mk(sub_folder)
            else:
                if not os.path.exists(sub_folder):
                    if '.' in sub_folder:
                        with open(sub_folder, 'w', encoding='utf-8') as my_file:
                            my_file.write('')
    else:
        os.chdir('../')


with open('config.yaml', 'r', encoding='utf-8') as conf_file:
    tree_folder = yaml.safe_load(conf_file)

tree_mk(tree_folder)
