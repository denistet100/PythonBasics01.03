# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


vocabulary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
              'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(en_def_str, vocab):
    if 64 < ord(en_def_str[0]) < 91:
        ru_def_str = vocab.get(en_def_str.lower())
        print(ru_def_str.capitalize())
    else:
        print(vocab.get(en_def_str))


print("input en_str")
en_str = input()

num_translate_adv(en_str, vocabulary)
