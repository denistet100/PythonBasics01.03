# 4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
# Алексеев", "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "И": {
# "И": ["Илья Иванов"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }
# Как поступить, если потребуется сортировка по ключам?


def thesaurus_adv(*args):
    dict_thes_def = {}
    for lastname_name in args:
        name, lastname = lastname_name.split(' ')
        list_lastname = []
        list_lastname.append(lastname_name)
        if lastname[0] in dict_thes_def:
            if name[0] in dict_thes_def[lastname[0]]:
                dict_thes_def[lastname[0]][name[0]].append(lastname_name)
            else:
                dict_thes_def[lastname[0]].update({name[0]: list_lastname})
        else:
            dict_thes_def.setdefault(lastname[0], {name[0]: list_lastname})
        list_lastname = []
    return dict_thes_def


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

# решение преподователя
#
#
# def thesaurus_adv(*names_surnames):
#     out_dict = dict()
#     for name_surname in names_surnames:
#         name, surname = name_surname.split()
#         out_dict.setdefault(surname[0], {})
#         out_dict[surname[0]]setdefault(name[0], [])
#         out_dict[surname[0]][name[0]].append(name_surname)
#
#     sorted_dict = {x: out_dict[x] for x in sorted(out_dict)}
#     return out_dict
#
#
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
