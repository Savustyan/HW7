"""
2. Взять код, который писали для игры кубики на лекции 7 https://github.com/VitaliiFisenko95/python_lk/blob/master/lk7/
class_work.py#L150 ,
проанализировать его (по возможности улучшить). Результат игры в кубики нужно записать в файл (json, yaml, csv, xlsx) по
 раундам.
В данных раунда должно быть:
 - время хода каждого из игроков
 - количество очков за раунд
 - номер игрока (или имя)
"""

import json
from datetime import datetime
import random

def first_player():
    input('Игрок 1, ваш ход')
    return random.randint(1, 6), str(datetime.now().time())


def second_player():
    input('Игрок 2, ваш ход')
    return random.randint(1, 6), str(datetime.now().time())


def main():
    start = input('Start game yes|no')
    player_1_sum = 0
    player_2_sum = 0
    if start == 'yes':
        data = {}
        counter = 10
        while counter:
            player_1_value, time_1 = first_player()
            player_2_value, time_2 = second_player()
            if player_1_value == player_2_value:
                continue
            player_1_sum += player_1_value
            player_2_sum += player_2_value

            print(player_1_value)
            print(player_2_value)

            counter -= 1
            data[f'Round_{10 - counter}'] = {
                'player_1': {
                    'name': 'player_1',
                    'round_sum': player_1_value,
                    'time': time_1
                },
                'player_2': {
                    'name': 'player_2',
                    'round_sum': player_2_value,
                    'time': time_2
                }
            }

        with open('res.json', 'w') as file:
            json.dump(data, file, indent=4)

        if player_1_sum > player_2_sum:
            print(' First player win')
            print(player_1_sum)
            print(player_2_sum)
            return

        if player_1_sum == player_2_sum:
            print('Победила дружба')
            print(player_1_sum)
            print(player_2_sum)
            return

        print(' Second player win')
        print(player_1_sum)
        print(player_2_sum)


main()

