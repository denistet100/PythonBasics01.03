# 7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и
# новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию, когда
# пользователь вводит номер записи, которой не существует.


# копия!!!

import sys

edit_idx, new_val = sys.argv[1:]
with open('bakery.csv', 'r+') as f:
    tmp_file = open('bakery.tmp', 'w+')
    change = False
    for i, line in enumerate(f, 1):
        if i == int(edit_idx):
            tmp_file.write(f'{new_val}\n')
            change = True
        else:
            tmp_file.write(line)
    if not change:
        exit('error')

    tmp_file.seek(0)

    f.truncate(0)  # delete all content from current position
    for line in tmp_file:
        f.write(line)
    tmp_file.close()
