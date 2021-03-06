# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(my_list)
my_list1 = []
for idx, item in enumerate(my_list):
    print(idx, ' ', item)
    if item.isdigit() or (item[0] == '-' and item[1].isdigit()) or (item[0] == '+' and item[1].isdigit()):
        # my_list1.extend('"', item, '"') мне так не нравится будут дыры из пробелов
        my_list1.append(f'"{item}"')
    else:
        my_list1.append(item)

print(my_list1)

my_list2 = " ".join(my_list1)
print(my_list2)
