# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def un_repeat(my_list):
    result_dict = {}
    result = []
    for el in my_list:
        result_dict.setdefault(el, 0)
        if el in result_dict:
            result_dict[el] = result_dict.get(el) + 1
    for key, val in result_dict.items():
        if val == 1:
            result.append(key)
    return result


print(un_repeat(src))