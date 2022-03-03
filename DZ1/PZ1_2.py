# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# c) * Решить задачу под пунктом b, не создавая новый список.

my_list = []

for i in range(1, 1001, +2):
    my_list.append(i)

print(my_list)

# a
sum_not_mod = 0

for key in my_list:
    if key % 7 == 0:
        sum_not_mod = sum_not_mod+key

print(sum_not_mod)

#b

sum_not_mod_b = 0

my_list1 = (key+17 for key in my_list)
for key in my_list1:
    if key % 7 == 0:
        sum_not_mod_b = sum_not_mod_b + key

print(sum_not_mod_b)

#c

#  какая разница?

sum_not_mod_c = 0
my_list = (key+17 for key in my_list)
for key in my_list:
    if key % 7 == 0:
        sum_not_mod_c = sum_not_mod_c + key

print(sum_not_mod_c)
