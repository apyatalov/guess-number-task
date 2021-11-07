"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    range_from = 1
    range_to = 101
    while True:
        count += 1
        predict_number = int((range_to + range_from) / 2)
        if number == predict_number:
            break  # выход из цикла если угадали
        if predict_number > number:
            range_to = predict_number
        else:
            range_from = predict_number
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    max_tries = int(np.max(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток, максимально за:{max_tries}")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
