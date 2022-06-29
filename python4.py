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
    print(n, n**2)


