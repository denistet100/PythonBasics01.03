# Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
#

# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
# Пробуйте их решать, если уверены в своих силах.

number = int(input('Пользователь, введите целое положительне число n: '))


def draw(number_a):
    end_number = number_a % 10
    if end_number == 0 or 10 > end_number > 4 or 21 > number_a > 4:
        print(number_a, 'процентов')
    elif end_number == 1:
        print(number_a, 'процент')
    elif 1 < end_number < 5:
        print(number_a, 'процента')


draw(number)

for i in range(0, 21, +1):
    draw(i)
