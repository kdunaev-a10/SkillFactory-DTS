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
