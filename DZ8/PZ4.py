# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
# ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
# return x ** 3
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
# © geekbrains.ru 16
# ...
# raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?



# def val_checker(func):
#     @wraps(func)
#     def wrapper(args):
#         if func(args):
#             return args
#         else:
#             raise ValueError(args)
#     return wrapper

# долго не мог понять ошибку, теперь вижу, не то функция принимала, точнее выдавала, надо было глубже опуститься
# def val_checker(decorator_check_func):
#     print(decorator_check_func)
#     def _val_checker(func_calc_cube):
#         print(func_calc_cube)
#         @wraps(func_calc_cube)  # нужно указать от какой функции
#         def wrapped(x):
#             print(x)
#             if decorator_check_func(x):
#                 return func_calc_cube(x)
#             else:
#                 raise ValueError(x)
#
#         return wrapped
#     return _val_checker

from functools import wraps


def val_checker(func):
    def val_checker1(args):
        @wraps(args)
        def wrapper(arg):
            if func(arg):
                return args(arg)
            else:
                raise ValueError(arg)
        return wrapper
    return val_checker1


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
# a = calc_cube(-5)
