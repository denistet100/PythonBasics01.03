# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
# решена, например, во фреймворке django.

import os
import shutil

folder = r'my_project1'
sub_folder = r'templates'
os.chdir(folder)
if not os.path.exists(sub_folder):
    os.mkdir(sub_folder)
address = os.path.abspath(sub_folder)
print(address)
os.chdir('../')

for list_folder in os.walk(folder):
    for progr in list_folder[-1]:
        if not sub_folder in list_folder[0]:
            if '.html' in progr:
                new_address = os.path.join(address, os.path.basename(list_folder[0]))
                if not os.path.exists(new_address):
                    os.mkdir(new_address)
                new_file = os.path.join(new_address, progr)
                old_file = os.path.join(list_folder[0], progr)
                shutil.copyfile(old_file, new_file)
