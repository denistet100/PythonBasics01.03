# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный",
# "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
# сделать аргументы именованными?
from random import choice, sample


def get_jokes(count, flag=1):
    """function jokes"""
    if flag == 1:
        for idx in range(count):
            my_str_jokes = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            print(my_str_jokes)
    else:
        my_nouns = []
        my_adverbs = []
        my_adjectives = []
        my_nouns.extend(sample(nouns, count))
        my_adverbs.extend(sample(adverbs, count))
        my_adjectives.extend(sample(adjectives, count))
        for idx in range(count):
            my_str_jokes = f'{my_nouns[idx]} {my_adverbs[idx]} {my_adjectives[idx]}'
            print(my_str_jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

flags = 1
print('writing counter: ')
counter = int(input())
if counter < 6:
    print('writing flag "0", if not repetition or "1", if with repetition')
    flags = int(input())

get_jokes(counter, flags)
