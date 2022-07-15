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

#3.4
print("###3.4")
def sum_min_numbers(a, b, c):
    min1 = find_min_number(a, b, c)
    if min1 == a:
        min2 = find_min_number(b, b, c)
    if min1 == b:
        min2 = find_min_number(a, c, c)
    if min1 == c:
        min2 = find_min_number(a, a, b)
    return min1+min2

print(sum_min_numbers(-2, -1, -3))