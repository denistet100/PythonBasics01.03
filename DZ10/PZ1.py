# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86
# 3 5 32
# 2 4 6
# -1 64 -8
# 3 5 8 3
# 8 3 7 1
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
# виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.


class Matrix:
    def __init__(self, data_matrix):
        self.data = data_matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.data])+'\n'
        # return '\n'.join([' '.join([i for i in line]) for line in self.data]) почему не работает?

    def __add__(self, other):
        add = str()
        if len(self.data) == len(other.data):
            for line1, line2 in zip(self.data, other.data):
                if len(line1) == len(line2):
                    add += ' '.join(map(str, [l1+l2 for l1, l2 in zip(line1, line2)])) + '\n'
                else:
                    return 'ошибка размера матриц'
        else:
            return 'ошибка размера матриц'
        return add


matrix_1 = Matrix([[31, 22], [37, 43], [51, 84]])
matrix_2 = Matrix([[27, 67], [34, 30], [28, 15]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)





















#
#
# class Matrix:
#     def __init__(self, data_matrix):
#         self.data = data_matrix
#
#     def __str__(self):
#         return '\n'.join([' '.join(map(str, line)) for line in self.input])
#
#     def __add__(self, other):
#         answer = ''
#         if len(self.input) == len(other.input):
#             for line_1, line_2 in zip(self.input, other.input):
#                 if len(line_1) != len(line_2):
#                     return 'Problems with shape'
#
#                 summed_line = [x + y for x, y in zip(line_1, line_2)]
#                 answer += ' '.join(map(str, summed_line)) + '\n'
#         else:
#             return 'Problems with shape'
#         return answer
#
