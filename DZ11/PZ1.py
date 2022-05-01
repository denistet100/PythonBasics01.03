"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random


def gen_num_barr_card():
    num = list(range(1, 91))
    random.shuffle(num)
    for num_on_cart in num:
        yield num_on_cart


class LotoCard:
    __N = 3
    __M = 9
    __count = 5

    def __init__(self):
        self.__matrix = []
        gen_num = gen_num_barr_card()

        for i in range(self.__N):
            nums = [next(gen_num) for _ in range(0, self.__count)]
            nums = sorted(nums)
            miss = self.__M - self.__count
            index = []
            matrix_str = []
            idx = 0
            for j in range(miss):
                index.append(random.randint(0, self.__M-1))
                while (j + 1) > (len(set(index))):
                    index.append(random.randint(0, self.__M-1))

            for j in range(0, self.__M):
                if j in index:
                    matrix_str.append(0)
                else:
                    matrix_str.append(nums[idx])
                    idx += 1
            self.__matrix.extend(matrix_str)

    def __str__(self):
        dash_string = '--------------------------'
        data = dash_string + '\n'
        for idx, val in enumerate(self.__matrix):
            if val == 0:
                data += '  '
            elif 0 < val < 10:
                data += f' {val}'
            elif val > 9:
                data += f'{val}'
            elif val == -1:
                data += ' -'

            if (idx + 1) % self.__M == 0:
                data += '\n'
            else:
                data += ' '
        data += dash_string
        return data

    def minus_num(self, num_minus):
        for idx, val in enumerate(self.__matrix):
            if val == num_minus:
                self.__matrix[idx] = -1

    def finish(self):
        return set(self.__matrix) == {0, -1}


class LotoGame:
    def __init__(self, player_1, player_2):
        self.__player_1 = LotoCard()
        self.__player_2 = LotoCard()
        self.__barrel = gen_num_barr_card()
        self.remains_barr = 91

    def start_game(self):
        barr = self.__barrel
        barr_next = next(barr)
        self.remains_barr -= 1
        print(f'Новый бочонок: {barr_next} (осталось {self.remains_barr})')
        print(f'----- Ваша карточка ------\n{self.__player_1}')
        print(f'-- Карточка компьютера ---\n{self.__player_2}')

        user_answer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        print(barr_next)
        print(self.__player_1)
        if (user_answer == 'y' and not barr_next in self.__player_1._LotoCard__matrix) or \
                (user_answer != 'y' and barr_next in self.__player_1._LotoCard__matrix):
            return 2

        if barr_next in self.__player_1._LotoCard__matrix:
            self.__player_1.minus_num(barr_next)
            if self.__player_1.finish():
                return 1
        if barr_next in self.__player_2._LotoCard__matrix:
            self.__player_2.minus_num(barr_next)
            if self.__player_1.finish():
                return 2

        return 0

    def start(self):
        while True:
            score = self.start_game()
            if score == 1:
                print('You win')
                break
            elif score == 2:
                print('You lose')
                break


if __name__ == '__main__':
    human_player = LotoCard()
    computer_player = LotoCard()

    game = LotoGame(human_player, computer_player)
    game.start()
