# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"],
# "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется
# сортировка по ключам? Можно ли использовать словарь в этом случае?


def thesaurus(*args):
    dict_thes_def = {}
    list(args).sort()
    for name in args:
        list_name = []
        first_chr = name[0]
        list_name.append(name)

        if dict_thes_def.setdefault(first_chr, list_name) != {first_chr: list_name}:
            list_name.pop()
            list_name.extend(dict_thes_def.get(first_chr))
            list_name.append(name)
            dict_thes_def[first_chr] = list_name
    print(dict_thes_def)


thesaurus("Иван", "Мария", "Петр", "Илья")

# решение преподователя
#
#
# def thesaurus(*names):
#     out_dict = dict()
#     for name in names:
#         out_dict.setdefault(name[0], [])
#         out_dict[name[0]].append(name)
#     return out_dict
#
#
# print(thesaurus("Иван", "Мария", "Петр", "Илья"))
