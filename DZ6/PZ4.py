# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется,
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей и
# название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные,
# полученные в результате парсинга.

# копия!!!

from itertools import zip_longest
with open('task4.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobby:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)

            if num_lines_users < num_lines_hobby:
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobby):
                f.write(f'{line_user.strip()}: '
                        f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')
