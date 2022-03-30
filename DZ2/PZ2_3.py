# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)

for idx, item in enumerate(my_list):
    print(idx, ' ', item)
    if item.isdigit() or (item[0] == '-' and item[1].isdigit()) or (item[0] == '+' and item[1].isdigit()):
        my_list.pop(idx)
        my_list.insert(idx, f'"{item}"')

print(my_list)

my_list = " ".join(my_list)
print(my_list)
