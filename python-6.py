python_string = 'Hello! My name is Python. I will help you to analyze some data'
count_sym = len(''.join(python_string.split()))
print(len(python_string)**3)

print(python_string[18:24])


python_string = python_string.replace("!","")
python_string = python_string.replace(".","")
string_list = list(python_string.split())
print(len(string_list))

def get_length(word):
    return len(word)

lens = map(get_length, string_list)
print(list(lens))

# Напишите свою функцию password_change, которая должна выводить на экран
# отформатированную строку в следующем виде:

# "User user_name changed password to new_password"

# Мы уже сделали заготовку функции вам осталось только задать строку
# Переменные, которые надо использовать, указаны в круглых скобках после имени функции
# user_name - имя пользователя, new_password - новый пароль
# запишите форматированную строку вместо знаков вопроса
# ! обязательное условие - задача должна быть решена с использованием метода format

def change_password(user_name, new_password):
    return "User {} changed password to {}".format(user_name,new_password)

print(change_password("Lena", "qwerty"))


#2.5
print("###2.5")
punctuation_list = ['.', ',', ';', ':', '...', '!', '?', '-', '"', '(', ')']
text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

# Напишите функцию get_unique_words(), которая избавляется от знаков препинаний
# и пробелов в тексте и возвращает упорядоченный список
# (слова расположены по алфавиту) из уникальных (неповторяющихся) слов.
def get_unique_words(text):
    #text = text.replace("\n", "")
    for sym in punctuation_list:
        text = text.replace(sym, "")
    text = text.lower()
    text_list = list(set(text.split()))
    text_list.sort()
    print(len(text_list))
    return(text_list)

print(get_unique_words(text_example))

#2.6
print("###2.6")
# Модифицируем предыдущую задачу.
# Теперь необходимо написать функцию get_most_frequent_word, которое возвращает самое часто встречающееся слово в тексте.

text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."

def get_most_frequent_word(text):
    for sym in punctuation_list:
        text = text.replace(sym, "")
    word_dict={}
    text = text.lower()
    text_list = text.split()
    for word in text_list:
        if word not in word_dict: word_dict[word] = 1
        else: word_dict[word] += 1
    word_list = sorted(word_dict.items(), key = lambda x: x[1], reverse=True)
    print(word_dict)
    return word_list[0][0]
print(get_most_frequent_word(text_example))

def get_most_frequent_word(text):
    for sym in punctuation_list:
        text = text.replace(sym, "")
    text = text.lower()
    text_list = text.split()
    unique_words = list(set(text_list))
    most_word = 0
    freq_word = ''
    for word in unique_words:
        if text_list.count(word) > most_word:
            most_word = text_list.count(word)
            freq_word = word
    return freq_word

print(get_most_frequent_word(text_example))


#2.7
print("###2.7")
# Разработайте функцию holes_count(), которая подсчитывает количество отверстий
# в заданном числе. Например, в цифре 8 два отверстия, в цифре 9 - одно.
# В числе 146 - два отверстия.
# Подсказка: используйте словарь для записи количества отверстий в цифрах


def holes_count(number):
    holes = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}
    holes_dict = {'0': 1, '4': 1, '6': 1, '8': 2, '9': 1}
    str_number = list(str(number))
    holes_number = 0
    for sym in str_number:
        #holes_number += holes[sym]
        holes_number += holes_dict.get(sym,0)
    return holes_number

print(holes_count(123))
print(holes_count(8888))
print(holes_count(4688890))

#2.8
print("###2.8")
user_list = []
user_analytics = {'username': [], 'age': [], 'email': []}
user_id = 0
user_number = 3
for i in range(1,user_number+1):
    user_dict = {}
    user_dict['username'] = "user"+str(i)
    user_dict['age'] = "age"+str(i)
    user_dict['email'] = "email"+str(i)
    user_id += 1
    user_list.append((user_id, user_dict))
    user_analytics['username'].append(user_dict['username'])
    user_analytics['age'].append(user_dict['age'])
    user_analytics['email'].append(user_dict['email'])
print(user_list)
print(user_analytics)


name_list = []
age_list = []
email_list = []
for users in user_list:
    name_list.append(users[1]['username'])
    age_list.append(users[1]['age'])
    email_list.append(users[1]['email'])

full_user_info = {'username': name_list, 'age':age_list, 'email':email_list}
print(full_user_info)


#3.4
print("###3.4")
def find_min_number(a, b, c):
  if a <= b and a <= c:
      return a
  elif b <= a and b <= c:
      return b
  else:
      return c

print(find_min_number(2,2,3))

#3.5
print("###3.5")
def sum_min_numbers(a, b, c):
    min1 = find_min_number(a, b, c)
    if min1 == a:
        min2 = find_min_number(b, b, c)
    if min1 == b:
        min2 = find_min_number(a, c, c)
    if min1 == c:
        min2 = find_min_number(a, a, b)
    return min1+min2

def sum_min_numbers1(a, b, c):
    min1 = find_min_number(a, b, c)
    if min1 == a:
        min2 = find_min_number(b, b, c)
    elif min1 == b:
        min2 = find_min_number(a, c, c)
    else:
        min2 = find_min_number(a, a, b)
    return min1+min2

print(sum_min_numbers1(1, 2, 3))

#3.6
print("###3.6")
# Напишите функцию is_divided_by_six(), которая проверяет, делится ли число на шесть.
# При решении воспользуйтесь тернарным оператором!
# Функция должна вернуть True, если число делится на шесть или False в обратном случае.
# Подсказка: число делится на шесть, если оно делится на 2 и на 3

def is_divided_by_six(number):

  return True if (number % 2 == 0 and number % 3 == 0) else False

print(is_divided_by_six(13))
print(is_divided_by_six(12))

#3.7
print("###3.7")
# Напишите функцию check_number_sign(), которая возвращает 1, если число положительное,
# -1, если число отрицательное, 0, если число - 0.
# Используйте в коде конструкцию if-elif-else.
# Функция принимает на вход одно число.

def check_number_sign(x):
    if x > 0:
        result = 1
    elif x < 0:
        result = -1
    else:
        result = 0
    return result


print(check_number_sign(0))
print(check_number_sign(100))
print(check_number_sign(-1))

#3.8
print("###3.8")
# Напишите функцию def division(), которая осуществляет деление двух чисел.
# Необходимо реализовать внутри функции отлов исключения ZeroDivisionError,
# в случае, если пользователь, при вызове функции, пытается поделить на ноль.
# Функция принимает на вход два числа - делимое и делитель.

def division(a, b):
  try:
      return a / b
  except ZeroDivisionError:
      print('Error! Matrices dimensions are different!')
      return None

print(division(1, 0))
print(division(1, 1))

#4.4
print("###4.4")
# Напишите функцию lucky_ticket(), которая проверяет, является ли билетик счастливым.
# Памятка: билетик счастливый, если сумма первых трех цифр равна сумме последних трех цифр.
# На вход функция получает шестизначное число.

def lucky_ticket(ticket_number):
    first_three_num_str = str(ticket_number // 1000)
    last_three_num_str = str(ticket_number % 1000)
    print(first_three_num_str,last_three_num_str)

    str_number = str(ticket_number)
    first_3 = 0
    second_3 = 0
    for s in str_number[:3]:
        first_3 += int(s)
    for s in str_number[3:]:
        second_3 += int(s)
    print(first_3,second_3)
    return first_3 == second_3

print(lucky_ticket(111111))
print(lucky_ticket(123456))

#4.5
print("###4.5")

# Напишите функцию def fib_number(), которая получается на вход некоторое
# число n и выводит n-e число Фибоначчи.
# Задачу можно решить как с помощью цикла for, так и с помощью цикла while
# Примечание: числа Фибоначчи определяются так
# ```
# a0 = 0, a1 = 1, a2 = a1 + a0 = 1, an = a_n-1 + a_n-2
# ```
# Примечание: в модуле по функциям уже было задание на вычисление чисел Фибоначчи
# с помощью рекурсивных функций. Здесь необходимо реализовать те же вычисления,
# но без использования рекурсии.

def fib_number1(n):
    fib_n = 0
    fib_n_1 = 1
    temp = 0
    for counter in range(1,n+1):
        print(fib_n, fib_n_1, temp)
        fib_n += fib_n_1
        fib_n_1 = temp
        temp = fib_n

    return fib_n

def fib_number(n):
    fib_n = 0
    fib_n_1 = 1
    fib_n_2 = 0
    #counter = 0
    for counter in range(2,n+1):
        fib_n = fib_n_2 + fib_n_1
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
    if n == 1:
        return 1
    return fib_n

print(fib_number1(4))

#4.6
print("###4.6")
# Напишите функцию def even_numbers_in_matrix(),
# которая получает на вход матрицу (список из списков)
# и возвращает количество четных чисел в ней.

matrix_example = [
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]
]
matrix_example = [[117, 56, 38, 11, 0], [1, 4, 3, 2, 3], [-4, 5, 6, -10, 2]]

def even_numbers_in_matrix(matrix):
    even_num = 0
    for i in range(len(matrix)):
        print(matrix[i])
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                even_num += 1
    return even_num

def even_numbers_in_matrix(matrix):
    even_num = 0
    for line in matrix:
        for elm in line:
            if elm % 2 == 0:
                even_num += 1
    return even_num

print(even_numbers_in_matrix(matrix_example))


#4.7
print("###4.7")
# Напишите функцию def matrix_sum(), которая получает на вход две матрицы
# и возвращает их сумму.
# Примечание: чтобы найти сумму двух матриц, нужно просуммировать
# их соответствующие элементы. Но перед этим необходимо проверить, что размеры
# матриц одинаковы (одинаковое количество столбцов и одинаковое количество строк)
# Например:

# 1 2 3   2 3 4   3 5 7
# 2 3 4 + 4 5 6 = 6 8 10
# 5 6 7   4 3 2   9 9 9

matrix_example = [
          [1, 5, 4],
          [4, 2, -2],
          [7, 65, 88]
]
matrix_example1 = [
          [1, 5, 4, 6],
          [4, 2, -2, 8],
          [7, 65, 88, 9]
]

def matrix_sum(matrix1, matrix2):
    num_row_1 = len(matrix1)
    num_row_2 = len(matrix2)
    elm_count_1 = len(matrix1[0])
    elm_count_2 = len(matrix2[0])
    print(num_row_1, num_row_2,elm_count_1, elm_count_2)

    if (num_row_1 != num_row_2) or (elm_count_1 != elm_count_2):
        print('Error! Matrices dimensions are different!')
        return None
    matrix_s = matrix1.copy()

    for i,line in enumerate(matrix2):
        for j,elm in enumerate(line):
            matrix_s[i][j] += elm
    return matrix_s

print(matrix_sum(matrix_example, matrix_example))