def print_root(value, n=2):
    # Зададим внутреннюю функцию
    # Она будет являться вспомогательной
    def root(value, n=2):
        result = value ** (1/n)
        return result
    # Получим результат из внутренней функции
    res = root(value, n)
    # Печатаем результат и не возвращаем его
    print('Root of power', n, 'from', value, 'equals', res)

print_root(81, 4)
#print(root(81, 4))


def register_employee(name, surname):
    def create_full_name():
        sep = ' '
        result = name + sep + surname
        return result
    full_name = create_full_name()
    print('Employee {} is registered with the company {}'.format(full_name, company_name))

company_name = 'TheBlindMice'  # название компании
register_employee('John', 'Doe')  # вызов функци

#################################################
# Создадим глобальную переменную
# и приравняем её нулю
global_counter = 0

# Создадим функцию, которая прибавляет 1
# к переменной global_counter
def add_one():
    global global_counter
    print(global_counter)
    global_counter += 1

# Запустим функцию add_one
add_one()
# Напечатаем значение переменной global_counter
print(global_counter)

##################################
def outer_function():
    # Создадим переменную, относящуюся к внешней функции
    enclosing_counter = 0

    # Внутренняя функция
    def inner_function():
        # Прибавим 1 к enclosing_counter
        nonlocal enclosing_counter
        enclosing_counter += 1
        # Напечатаем значение enclosing_counter
        print(enclosing_counter)

    # Запустим внутреннюю функцию из внешней
    inner_function()
# Запустим внешнюю функцию
outer_function()

###############
# Повтор предыдущего кода:
my_list = [1, 4, 5, 7]
# Запишем в переменную с названием
# len длину списка my_list,
# полученную с помощью встроенной функции len
#len = len(my_list)
#print(len)
# Будет напечатано:
# 4

# Попробуем снова воспользоваться функцией len:
# Создадим ещё один список
new_list = ['Ivan', 'Sergej', 'Maria']
# Также узнаем его длину с помощью функции len
length = len(new_list)
print(length)
# Возникнет ошибка:
# TypeError: 'int' object is not callable

#########################
def outer():
    x = 1
    def inner():
        print('x in outer function: ', x)
    return inner

out = outer()
#print(out)
#out()
outer()()

###############
def counter():
    # Начальное значение счётчика — 0
    number = 0
    print("ID-counter ", id(number))

    # Функция add будет каждый раз прибавлять
    # к счётчику 1 при запуске
    def add():
        # Сообщаем, что number берём из
        # внешней функции
        nonlocal number
        print("ID-add ", id(number))
        number += 1
        return number
    # Возвращаем не результат вычислений,
    # а непосредственно саму функцию add
    # без круглых скобок!
    return add

print(counter())
counter1 = counter()
# Проверим, что counter1 действительно является вызываемым объектом,
# то есть функцией. Для этого воспользуемся встроенной функцией
# callable:
print(callable(counter1))


# Создадим два различных счётчика
print("counter 1 and counter 2")
counter1 = counter()
counter2 = counter()

# Будем запускать вразнобой разные счётчики

print("Counter1:", counter1())
print("Counter1:", counter1())
print("Counter2:", counter2())
print("Counter2:", counter2())
print("Counter1:", counter1())
print("Counter2:", counter2())
print("Counter2:", counter2())



#2.5
print('##2.5')
def saver():
    total = 0
    def add_saver(money):
        nonlocal total
        total += money
        return total
    return add_saver

pig1 = saver()
pig2 = saver()
print(pig1(25))
print(pig1(100))
print(pig1(19))
print(pig2(100))
print(pig2(100))
print(pig2(200))


y = 10
x = y
print(id(x), id(y))
print(id(x), id(10))
x += 1
print(id(x), id(y))
print(id(x), id(10))
print(id(x), id(11))
print(id(x), id(12))


s = ""
for i in range(1, 10):
    s += str(i) + ','
    print(s)
    print(id(s))
#    s += ","
#    print(s)
#    print(id(s))
print(s)


stack = "Overflow"
print(stack)
print(id(stack))
stack += "T" + " ,"
print(stack)
print(id(stack))

y = 3.4
x = y
print(id(x), id(y))
print(id(x), id(3.4))
x += 1
print(x)
print(id(x), id(y))
print(id(x), id(3.4))
print(id(x), id(4.4))


#######################
#3
def sum_lst(lst):
    print(lst)
    if len(lst) == 0 : return 0
    return lst[0] + sum_lst(lst[1:])


#3.4
print("###3.4")
def mul_lst(lst):
    print(lst)
    if len(lst) == 0 : return 1
    return lst[0] * mul_lst(lst[1:])
my_lst = [10, 21, 24, 12]
print(sum_lst(my_lst))
print(mul_lst(my_lst))



#3.5
print("###3.5")
def factorial(num):
    if num == 0: return 1
    if num == 1: return 1
    return num * factorial(num-1)

print(factorial(5))

#3.7
print("###3.7")
def fib(num):
    if num == 0: return 0
    if num == 1: return 1
    return fib(num - 1) + fib(num - 2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(6))

#4.4
print("###4.4")
def check_string(s):
    print(s)
    if len(s) < 1:
        return True
    if s[0] == s[-1]:
        return check_string(s[1:-1])
    else:
        return False
print(check_string('ABCCBA'))


#4.5
print("###4.5")
def power(val, n):
    #print(val)
    if n == 0: return 1
    if n == 1: return val
    return val * power(val, n-1)

print(power(25,0))
print(power(-5,4))


#4.6
print("###4.6")
def is_leap(x):
    return (int(x)%400 == 0) or (int(x)%4 == 0) and not (int(x)%100 == 0)
print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2020))


#4.7
print("###4.7")
def check_date(day, month, year):
    def is_leap(year):
        return (int(year) % 400 == 0) or (int(year) % 4 == 0) and not (int(year) % 100 == 0)

    #if not ((type(day) is int) and (type(month) is int) and (type(year) is int)): return False
#    print(list(map(lambda x: type(x) == int, [day, month, year])))
    if not all(list(map(lambda x: type(x) == int, [day, month, year]))) : return False
#    print("DEBUG 1")
    if not (1900 < year < 2022) : return False
#    print("DEBUG 2")
    if not (1 <= month <= 12): return False
#    print("DEBUG 3")
    if not (1 <= day <= 31): return False
#    print("DEBUG 4")
    if month in [4,6,9,11] and day > 30 : return False
#    print("DEBUG 5")
    if not is_leap(year) and month == 2 and day > 28  : return False
#    print("DEBUG 6")
    if is_leap(year) and month == 2 and day > 29: return False
    return True

print(check_date(13.5,12,2017))
print(check_date(5,12,1890))
print(check_date(5,13,1980))
print(check_date(54,5,1980))
print(check_date(31,4,1980))
print(check_date(29,2,2001))

print(check_date(18,9,1999))
print(check_date(29,2,2000))
print(check_date(29,2,2021))
print(check_date(13,13,2021))
print(check_date(13.5,12,2021))

#4.8
print("###4.8")

def check_date(day, month, year):
    def is_leap(year):
        return (int(year) % 400 == 0) or (int(year) % 4 == 0) and not (int(year) % 100 == 0)

    #if not ((type(day) is int) and (type(month) is int) and (type(year) is int)): return False
    if not all(list(map(lambda x: type(x) == int, [day, month, year]))) : return False
    if not (1900 < year < 2022): return False
    if not (1 <= month <= 12): return False
    if not (1 <= day <= 31): return False
    if month in [4, 6, 9, 11] and day > 30: return False
    if not is_leap(year) and month == 2 and day > 28: return False
    if is_leap(year) and month == 2 and day > 29: return False
    return True

def register(surname, name, date, middle_name=None, registry=None):
    if registry is None: registry = []
    if not check_date(*date): raise ValueError("Invalid Date!")
    registry.append((surname,name,middle_name, date[0], date[1], date[2]))
    return registry


reg = register('Petrova', 'Maria', (13, 3, 2003), 'Ivanovna')
reg = register('Ivanov', 'Sergej', (24, 9, 1995), registry=reg)
reg = register('Smith', 'John', (13, 2, 2003), registry=reg)
print(reg)
reg = register('Ivanov', 'Sergej', (29, 3, 2021))
print(reg)

#5
print("###5")
new_list = [12, 14, 16]
iter_list = iter(new_list)
print(iter_list)
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

new_list = ['admin', 'guest', 'root', 'anonymous']
iter_list = iter(new_list)
while True:
    try:
        print(next(iter_list))
    except StopIteration:
        print("Empty list")
        break

iter_list = iter(new_list)
for user in iter_list:
    print(user)

new_list = ['admin', 'guest', 'root', 'anonymous']
for i, user in enumerate(new_list):
    # Выводим индекс и элемент на экран через двоеточие
    print(i, user, sep=': ')

new_list = ['admin', 'guest', 'root', 'anonymous']
enum_users = enumerate(new_list)
enum_list = list(enum_users)
print(enum_list)

# Создаём цикл по элементам итератора
for i, user in enum_users:
    print("iter: ", i, user, sep=': ')
#Ничего не будет напечатано

#print(next(enum_users))
# Возникнет ошибка:
# StopIteration:

print()

# Объявляем функцию для расчёта суммы вклада
def deposit(money, interest):
    # Процент по вкладу преобразуем во множитель:
    # делим процент на 100 и прибавляем 1
    interest = interest/100 + 1
    # Создаем бесконечный цикл
    while True:
        # Сумма вклада через год — это
        # текущая сумма, умноженная на коэффициент и
        # округлённая до двух знаков после запятой
        money = round(interest * money, 2)
        # Выдаём полученную сумму вклада
        yield money
        #return money
print(deposit(1000, 5))
bank = deposit(1000,5)
print(next(bank))
print(next(bank))
print(next(bank))

print()
# Объявляем функцию для расчёта суммы вклада
# Аргумент years принимает число лет, на которое рассчитан вклад
def deposit_years(money, interest, years):
    interest = interest/100 + 1
    # Вместо while используем цикл for с range
    for year in range (years):
        money = round(interest * money, 2)
        yield money

bank2 = deposit_years(1500, 3, 2)
print(next(bank2))
print(next(bank2))
#print(next(bank2))

print()
bank3 = deposit_years(10000, 10, 3)
for money in bank3:
    print(money)
#print(next(bank3))

print()
bank3 = deposit_years(10000, 10, 3)
sums = list(bank3)
print(sums)


#5.5
print("###5.5")
def mygen():
    i=7
    print('hello')
    while i>0:
        i-=1
        yield i
gen = mygen()
print(gen)
print(next(gen))

#5.6
print("###5.6")
gen = mygen()
for i in gen:
    print(i, end=' ')
print()

#5.7
print("###5.7")
def inf_iter(l_in):
    while True:
        for char in l_in:
            yield char

l = [101, 102, 103]
gen = inf_iter(l)
for _ in range(5):
    print(next(gen))

#5.8
print("###5.8")
def group_gen(n):
    while True:
        for i in range(1,n+1):
            yield i

groups = group_gen(3)
for _ in range(10):
    print(next(groups))

#5.8.1
print("###5.8.1")
# Объявляем генератор square_gen
def square_gen():
    # Создаём цикл для последовательности от 1 до 10
    for x in range(1, 11):
        # Выдаём квадрат числа
        yield x ** 2
gen = square_gen()
print(type(gen))
square_list = list(gen)
print(square_list)

squares_generator = (x**2 for x in range(1,11))
print(type(squares_generator))
print(squares_generator)
print(next(squares_generator))
print(next(squares_generator))
print("for loop")
for n in squares_generator:
    print(n)

squares_generator = (x**2 for x in range(1,11))
print(list(squares_generator))
squares_generator = (x**2 for x in range(1,11))
print(tuple(squares_generator))
squares_generator = (x**2 for x in range(1,11))
print(set(squares_generator))

#5.8.1
print("###5.8.1")
kube_generator = (x**3 for x in range(1,16) if x % 3 == 0)
print("for loop")
for n in kube_generator:
    print(n)

triple_cubes_list = [x**3 for x in range(1,16) if x % 3 == 0]
print(type(triple_cubes_list))
print(triple_cubes_list)

triple_cubes_set = {x**3 for x in range(1,16) if x % 3 == 0}
print(type(triple_cubes_set))
print(triple_cubes_set)

triple_cubes_tuple = tuple((x**3 for x in range(1,16) if x % 3 == 0))
print(type(triple_cubes_tuple))
print(triple_cubes_tuple)

def root_generator(values):
    for val in values:
        if val >= 0:
            result = val ** 0.5
            yield result

#5.9
print("###5.9")
def root_generator(values):
    for val in values:
        if val >= 0:
            result = val ** 0.5
            yield result
new_root_generator = root_generator([-5, 25, 36, -25, 0])
for n in new_root_generator:
    print(n)

new_root_generator = (x ** 0.5 for x in [-5, 25, 36, -25, 0] if x >= 0)
for n in new_root_generator:
    print(n)

print("triple dict")
triple_cubes_dict = {x:x**3 for x in range(1,16) if x % 3 == 0}
print(type(triple_cubes_dict))
print(triple_cubes_dict)

st = "asdfghasdf"
st_dict = {x:0 for x in st}
print(st_dict)

st = "asdfghasdf"
st_dict1 = {x:st.count(x) for x in st_dict.keys()}
print(st_dict1)

#6
print('##6')
def get_length(word):
    return len(word)
names = ['Ivan', 'Nikita', 'Simon', 'Margarita', 'Vasilisa', 'Kim']
lens = map(get_length, names)
print(next(lens))
print(next(lens))

lst = list(map(get_length, names))
print(lst)

lens = list(map(lambda x: len(x), names))
print(lens)

#6.1
print('##6.1')
docs = [
    '//doc/5041434?query=data%20science',
    '//doc/5041567?query=data%20science',
    '//doc/4283670?query=data%20science',
    '//doc/3712659?query=data%20science',
    '//doc/4997267?query=data%20science',
    '//doc/4372673?query=data%20science',
    '//doc/3779060?query=data%20science',
    '//doc/3495410?query=data%20science',
    '//doc/4308832?query=data%20science',
    '//doc/4079881?query=data%20science'
]
url = 'https://www.kommersant.ru'

links = map(lambda s: url+s,docs)
for i in docs:
    print(next(links))

even_list = list(filter(lambda x: x % 2 == 0,lens))
print(even_list)

#6.2
print('##6.2')
family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
    ]

def family(*arg):
    family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
    ]
    print(arg)
    lst = list(filter(lambda s: s in family_list, arg))
    return lst
    #ваш код здесь. используйте функцию filter()


#вызов функции
print(family(
    'newborn registration',
    'parking permit',
    'maternity capital',
    'tax benefit',
    'medical policy'
    )
)

#6.3
print('##6.3')

names = ['Ivan', 'Nikita', 'Simon', 'Margarita', 'Vasilisa', 'Kim']
long_names = filter(lambda s: len(s) >= 5, names)
#print(next(long_names))
count_a = map(lambda x: (x, x.upper().count('A')), long_names)
print(list(count_a))


reg = [('Ivanov', 'Sergej', 24, 9, 1995),
      ('Smith', 'John', 13, 2, 2003),
      ('Petrova', 'Maria', 13, 3, 2003)]

#year_2000 = filter(lambda y: y[4] > 2000, reg)
year_2000 = filter(lambda y: y[-1] > 2000, reg)

new_reg = map(lambda tuple: (tuple[0]+' '+tuple[1][:1]+'.', tuple[2], tuple[3], tuple[4]), year_2000)
print(list(new_reg))


def update_tuple(arg):
    # Выделяем фамилию из кортежа
    surname = arg[0]
    # Выделяем имя из кортежа
    name = arg[1]
    # Создаём новую запись: фамилия + пробел + первая буква имени + точка
    new_surname = surname + ' ' + name[0] + '.'
    # Возвращаем обновлённый кортеж
    return (new_surname, arg[2], arg[3], arg[4])

# Фильтруем записи по условию, что последний элемент кортежа > 2000
filter_reg = filter(lambda x: x[-1] > 2000, reg)
# Применяем функцию-преобразование к каждому кортежу из списка и создаём новый список
new_reg = list(map(update_tuple, filter_reg))




#6.4
print('##6.4')
surnames = ['Ivanov', 'Smirnov', 'Kuznetsova', 'Nikitina']
ames = ['Sergej', 'Ivan', 'Maria', 'Elena']
names = ['Sergej', 'Ivan']
# Создаём цикл по элементам итератора zip — кортежам из фамилий и имён
for surname, name in zip(surnames, names):
    print(surname, name)

def group_gen(n=3):
    while True:
        for i in range(1, n+1):
            yield i

g = group_gen()
for i in range(11):
    print(next(g))

def print_groups(users):
    group_n = group_gen()
    group_list = zip(users, group_gen())
    for s,g in group_list:
        print("{} in group {}".format(s,g))


users = ['Smith J.', 'Petrova M.', 'Lubimov M.', 'Holov J.']
print_groups(users)

from functools import reduce
iterable = list(range(1, 7))
# Применяем lambda-функцию для вычисления к произведения к списку
reduced = reduce(lambda x,y: x*y , iterable)
print(reduced)

print(reduce(lambda x,y: x+y, range(6)))