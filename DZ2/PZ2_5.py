# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

my_list = [57.8, 46.51, 97, 34.5, 45, 453.45, 3, 34.04, 45, 55.02]
print(my_list)


def func_prise(prise_list):
    for prise_goods in prise_list:
        if isinstance(prise_goods, float):
            rub, cent = str(prise_goods).split('.')
        else:
            rub = prise_goods
            cent = 0

        prise = f'{int(rub)} руб {int(cent):02d} копеек'
        print(prise)


# A
func_prise(my_list)
# B
print("before sorting ", id(my_list), type(my_list))
my_list.sort()
print(my_list)
print("after sorting ", id(my_list), type(my_list))
func_prise(my_list)
# C
my_list.reverse()
print("after reversing ", id(my_list), type(my_list))
func_prise(my_list)
# D
print("five max price: ")
func_prise(my_list[:5])
