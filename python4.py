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
for number in range(0,9):
    my_list.append(number**2)
print(my_list)