incomes = [120, 38.5, 40.5, 80] #список доходов семьи Быковых
S = 0 #задаём начальное значение суммы доходов
#создаём цикл for, в котором будем проходиться по элементам списка incomes
for income in incomes: #income — текущее значение элемента списка
    print('Current income', income) #выводим текущее значение переменной income
    print('Current S', S) #выводим текущее значение переменной S
    S += income #увеличиваем сумму доходов на значение income, равносильно S = S + income
    print('New S', S) #выводим обновлённое значение переменной S
    print() #выводим пустую строку для красивого отображения
print('Answer: s=', S) #выводим результат

print(sum(incomes))

lst = [98, 24, 23, 12, 3]
product = 1
for item in lst:
    print("current item", item)
    product *= item
print("Product", product)

S = 0
Number = 3
for num in range(1, Number+1):
    S += num
print("Sum of {} numbers {}".format(Number, S))

#1.3
print("1.3")
print(len(range(20,1,-2)))
for i in range(20,1,-2):
    print(i)
print("---")
print(len(range(10,1,-1)))
for i in range(10,1,-1):
    print(i)

#1.4
print("###1.4")
S = 1
Number = 5
for num in range(1, Number+1):
    S *= num
print("Product of {} numbers {}".format(Number, S))

#1.5
print("###1.5")
Number = 4
str1 = ""
for num in range(1, Number+1):
    str1 +="*"
    print(str1)
print("---")
for num in range(1, Number+1):
    print("*" * num)

print("----")
places = [
    'Red Square',
    'Swallow Nest',
    'Niagara Falls',
    'Grand Canyon',
    'Louvre',
    'Hermitage'
]

#словарь соответствия мест и стран
location = {
    'Red Square': 'Russia',
    'Swallow Nest': 'Russia',
    'Niagara Falls': 'USA',
    'Grand Canyon': 'USA',
    'Louvre': 'France',
    'Hermitage': 'Russia'
}

#создаём цикл по списку мест, которые хотим посетить
count = 0
for place in places: #place — текущее название места
    country = location[place] #получаем страну из словаря location по ключу
    if country != 'Russia': #сравниваем название стран
        places[count] = 'Unavailable' #помечаем место как недоступное
    count += 1
print(places) #выводим результирующий список

print("----")
places = [
    'Red Square',
    'Swallow Nest',
    'Niagara Falls',
    'Grand Canyon',
    'Louvre',
    'Hermitage'
]

#словарь соответствия мест и стран
location = {
    'Red Square': 'Russia',
    'Swallow Nest': 'Russia',
    'Niagara Falls': 'USA',
    'Grand Canyon': 'USA',
    'Louvre': 'France',
    'Hermitage': 'Russia'
}
for count in range(len(places)):
    country = location[places[count]]  # получаем страну из словаря location по ключу
    if country != 'Russia':  # сравниваем название стран
        places[count] = 'Unavailable'  # помечаем место как недоступное

print(places)  # выводим результирующий список

#1.6
print("###1.6")
my_list = []
for number in range(0,10):
    my_list.append(number**2)
print(my_list)

#1.8
print("###1.8")
my_list=[1]
for i in range(10):
    my_list.append(my_list[i] * 2)
print(my_list, len(my_list))


#1.9
print("###1.9")
word_list = "My name is Kons".split()
print(word_list)
str1 = ""
for s in word_list:
    str1 += s + " "
print(str1)

#1.10
print("###1.10")
num_list = [1, 10, 3, -5]
num_list.sort()
for item in num_list:
    print(item)

#1.11
print("###1.11")
my_list = list(range(0, 100, 3))
count_odd = 0
for item in my_list:
    if item % 2 == 0:
        count_odd += 1
print("Number of odd", count_odd)

#1.12
print("###1.12")
my_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']
count = 0
for item in my_list:
    if type(item) is str:
        count += 1
print(count)


#2
lst=['a', 'b', 'c', 'd', 'e']
while len(lst) > 2:
    #Начало блока кода с телом цикла
    lst.pop(0) # Обновляем список, удаляя первый элемент в нём
    print(lst) # Выводим промежуточный результат
    #Конец блока кода с телом цикла
#Выводим на экран результирующий список
print('Result', lst)

print("----")

weight = 67 #заданный вес входящего в лифт человека
max_weight = 400 #задаём грузоподъёмность
S = 0 #задаём суммарный вес людей в лифте
#создаём цикл, который будет работать, пока S не превысит max_weight
while S < max_weight: #делай, пока...
    S += weight #увеличиваем суммарный вес, равносильно S = S + weight
    print('Current sum weight', S) #выводим значение суммарного веса после обновления
print() #отделяем промежуточный вывод от результата пустой строкой
print('Overweight {} kg'.format(S-max_weight)) #выводим итоговое значение перевеса

#2.2
print("###2.2")
max_vol = float(10)
val1 = 3.3
S = 0
while S < max_vol:
    S += val1
    print(S)
print("overflow is {:.2} l".format(S - max_vol))

print("----")
S = 0  # создаём накопительную переменную, в которой будем считать сумму
n = 1  # задаём текущее натуральное число

# создаём цикл, который будет работать, пока сумма не превысит 500
while S < 50:  # делай, пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # увеличиваем значение натурального числа
    print("Still counting ...")  # выводим строку ожидания
print()  # отделяем промежуточный вывод от результата пустой строкой
print("Sum is: ", S)  # выводим результирующую сумму
print("Numbers total: ", n - 1)  # выводим результирующее количество чисел

#2.3
print("###2.3")
max_sq = 1000
n = 1
while n**2 <  max_sq:
    n += 1
    print(n, n**2)
print("Max number with SQ > 1000 is ", n-1)

print("---")
n = 1
while True:
    if n > 10:
        break
    print(n)
    n += 1

secret_passwords = {
    'Enot': 'ulybaka',
    'Agent12': '1password1',
    'MouseLulu': 'myshkanaruhka'
} #база позывных и паролей
#создаём бесконечный цикл
#while True:
#    name = input("enter name:")
#    if name in secret_passwords:
#        password = input("enter password:")
#        if password == secret_passwords[name]:
#            print("Weclome, ", name)
#            break
#        else:
#            print("wrong password")
#    else:
#        print("wrong name")

#2.4
print("###2.4")

max_sq = 1000
n = 1
while True:
    if n**2 >  max_sq:
        print("Max number with SQ > 1000 is ", n - 1)
        break
    n += 1

#2.8
print("###2.8")
n = 10
i = 1
while i ** 2 < n:
    i += 1
print(i)

#2.9
print("###2.9")
n = 10
i = 0
while i < n:
    print('Hello')
    i += 1

#2.10
print("###2.10")
max_pr = 1000
n = 1
pr = 1
while pr < max_pr:
    pr *= n
    n += 1
    print(pr, n)
print(pr, n - 1)


#2.11
print("###2.11")
max_pr = 1000
n = 0
pr = 3
while pr**n < max_pr:
    n += 1
print(pr**n, n - 1)

#2.12
print("###2.12")
max_pr = 3000
n = 1.08
y = 0
pr = 1000
while pr < max_pr:
    pr *= n
    y += 1
    print(pr, y)
print(pr, y)

#2.13
print("###2.13")
max_people = 5
i = 0
while i < max_people:
    print('There are', i, 'people in the room') # В помещении i человек
    i += 1


####3
temperature = [
    [13, 15, 10],
    [14, 13, 9],
    [8, 9, 6]
]
print(temperature[0][2])
print(temperature[1][1])
print(temperature[2][0])


matrix = [
    [1, 2],
    [3, 4, 5],
    [5, 6]
]

for row in matrix:
    print(row)
    for elm in row:
        print(elm)
    print()

N = len(matrix)
for i in range(N):
    print(i, matrix[i])
    M = len(matrix[i])
    for j in range(M):
        print(i,j,matrix[i][j])
    print()

#3.2
print("###3.2")
hours = list(range(9, 24, 2)) #создаём список часов
minutes = list(range(0, 60, 15)) #создаём список минут
for h in hours:
    for m in minutes:
        print("Alarm set {} {}".format(h,m) )

str_list = ['text', 'morning', 'notepad', 'television', 'ornament'] #заданный список строк
count = 0 #задаём начальное количество символов 'e'
#создаём цикл по элементам списка str_list
for text in str_list:
    #увеличиваем количество символов 'e'
    count += text.count('e') #.count() считает, сколько раз символ встречается в строке text
print("Count symbol 'e':", count) #выводим результат

#3.3
print("###3.3")
text_list = [
    'afbaad',
    'faaf',
    'afaga',
    'agag'
]
count = 0
for text in text_list:
    count += text.count("a")
print("a - ", count)

count = 0
for text in text_list:
    for sym in text:
        if sym == "a":
            count += 1
print("a - ", count)

#3.4
print("###3.4")

random_matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]
max_val_row = []
for row in random_matrix:
    max_val = row[0]
    for elm in row:
        if elm > max_val:
            max_val = elm
    max_val_row.append(max_val)
print(max_val_row)

#3.5
print("###3.5")
student_scores = [
    [56, 90, 80],
    [80, 86, 92],
    [91, 76, 89],
    [91, 42, 60],
    [65, 30, 90]
]

summa = 0
math_sum = 0
info_sum = 0
rus_sum = 0
N = len(student_scores) # number of students
for i in range(N):
    M = len(student_scores[i])
    math_sum += student_scores[i][0]
    info_sum += student_scores[i][1]
    rus_sum += student_scores[i][2]
    for j in range(M):
        summa += student_scores[i][j]
print('Average math score', math_sum/N) #выводим средний балл по математике
print('Average info score', info_sum/N) #выводим средний балл по информатике
print('Average rus score', rus_sum/N) #выводим средний балл по русскому языку
print('Average score', N,M,summa/(N*M)) #выводим общий средний балл


#3.6
print("###3.6")
count = 0
for i in range(5):
    for j in range(4):
        count += 1
print(count)

#3.7
print("###3.7")
scores = [
    [0.5, 0.6, 0.6, 0.65, 0.3],
    [0.55, 0.7, 0.9, 0.5, 0.5]
]
scores_lst = []
for row in scores:
    for score in row:
        scores_lst.append(score)
print(scores_lst)

#3.8
print("###3.8")
test_matrix1 = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1]
]
test_matrix2 = [
    [1, 2, 3],
    [7, -1, 2],
    [123, 2, -1],
    [123, 5, 1]
]

row_count = len(test_matrix1)
elm_count = 0

