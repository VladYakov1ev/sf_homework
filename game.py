"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем число, равное середине интервала, а затем увеличиваем левую границу на 1
    если искомое число больше, либо уменьшаем правую границу на 1, если искомое число меньше. 
    И так до тех пор пока не отгадаем.
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lower = 1
    upper = 100
    while True:
        predict = (lower + upper) // 2    # предполагаемое число
        count += 1
        if number > predict:
            lower = predict + 1
        elif number < predict:
            upper = predict - 1
        else:
            break    # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
