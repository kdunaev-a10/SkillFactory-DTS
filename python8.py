import numpy as np
number = np.random.randint(1, 101) # загадываем число
count = 0
while True:
    count += 1
    #predict_number = int(input("Угадай число от 1 до 100"))
    predict_number = number

    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла

"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
def random_predict(number:int=50) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 50.

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
    random_array = np.random.randint(1, 100, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)
