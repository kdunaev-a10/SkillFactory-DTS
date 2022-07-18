import numpy as np

"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def half_predict(number:int=50) -> int:
    """Guess using half/divide

    Args:
        number (int, optional): _description_. Defaults to 50.

    Returns:
        int: _description_
    """

    count = 0
    predict_number = int(range_random / 2) # предполагаемое число
    min_last = 1
    max_last = range_random
    while True:
        count += 1
        if number > predict_number:
            min_last = predict_number
            predict_number = int((min_last + max_last)/2)
            
        elif number < predict_number:
            max_last = predict_number
            predict_number = int((min_last + max_last)/2)
            
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)


def score_game(random_predict) -> int:
    """
    The score_game function will take a function that randomly guesses a number between 1 and 99
    (inclusive) and returns how many guesses it took to get the right answer.
    The function will also take an integer parameter determining how many times the game is played.
    The score_game function will return the average number of guesses it took to win each game.

    :param random_predict: Pass the function that will be used to predict the number
    :return: ?
    :doc-author: Trelent"""


    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, range_random, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    range_random = 500
    #score_game(random_predict)
    score_game(half_predict)
#end   
#end
