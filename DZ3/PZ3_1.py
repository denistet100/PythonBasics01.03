# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
# русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
# информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
# снаружи.

vocabulary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
              'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(eng_def_str):
    return vocabulary.get(eng_def_str)


print("input en_str")
en_str = input()

print(num_translate(en_str))
