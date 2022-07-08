def multiply_lst(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * multiply_lst(lst[1:])

my_lst = [10, 21, 24, 12]

print(multiply_lst(my_lst))


def print_hours(minutes):
    # // — это оператор целочисленного деления
    hours = minutes // 60
    # % — это оператор получения остатка от деления
    left_minutes = minutes % 60
    print("Hours:{} Minutes:{}".format(hours,left_minutes))

print_hours(94)

def get_time(distance, speed):
    # В переменную result сохраним результат
    # деления расстояния на скорость.
    result = round(distance / speed,2)
    # Чтобы вернуть результат вычислений,
    # пишем оператор return и название переменной,
    # значение которой будет передано.
    return result
print("time spent hours:", get_time(56, 6))

def get_time_tuple(distance, speed):
    # В переменную result сохраним результат
    # деления расстояния на скорость.
    hours = distance // speed
    distance_left = distance % speed
    kms_per_min = speed / 60
    left_minutes = round(distance_left / kms_per_min)
    print(hours, distance_left, kms_per_min, left_minutes)

    return hours, left_minutes

h,m = get_time_tuple(56, 6)
print("time spent hours:mins:", h,m)

def in_list(list_in, obj):
    for elm in list_in:
        if elm == obj:
            print("Found")
            return True
    print("not found")
    return False

my_list = [1,2,5,7,10]
result = in_list(my_list, 3)
# Element is NOT found!
print(result)
result = in_list(my_list, 7)
# Element is found!
print(result)

# Функция открытия дверей
def open_doors():
    pass

# Функция закрытия дверей
def close_doors():
    pass

# Функция перемещения на этаж с номером number
def move_to_floor(number):
    pass

def get_time(distance, speed):
    if  speed == 0:
        raise ValueError("Speed cannot be equal to 0!")
    # Если расстояние или скорость отрицательные, то возвращаем ошибку
    if distance < 0 or speed < 0:
        # Оператор raise возвращает (raise — досл. англ. "поднимать")
        # объект-исключение. В данном случае ValueError (некорректное значение).
        # Дополнительно в скобках после слова ValueError пишем текст сообщения
        # об ошибке, чтобы сразу было понятно, чем вызвана ошибка.
        raise ValueError("Distance or speed cannot be below 0!")
    result = distance / speed
    return result

print(get_time(100, 11))

def get_cola(ice=True):
    if ice == True:
        print("Cola with ice is ready!")
    else:
        print("Cola without ice is ready!")

get_cola()

print(16 ** (1/4))
def root(value, n=2):
    # Как мы уже выяснили, чтобы посчитать
    # корень степени n из числа, можно возвести это число
    # в степень 1/n
    result = value ** (1/n)
    return result

# Посчитаем корень 3-ей степени (кубический корень) из 27
print(root(25))

#def wrong_root(n=2, value):
#    result = value ** (1/n)
#    return result
#print(wrong_root(25))


def add_mark(name, mark, journal={}):
    # Присваиваем имени в журнале переданную оценку
    journal[name] = mark
    return journal
group1 = {}
group1 = add_mark('Ivanov', 5, group1)
group1 = add_mark('Tihonova', 4, group1)
print(group1)

group2 = add_mark('Smirnov', 3)
print(group2)
group3 = add_mark('Kuznetsova', 5)
print(group3)

def add_mark_correct(name, mark, journal=None):
    # Присваиваем имени в журнале переданную оценку
    if journal is None:
        journal = {}
    journal[name] = mark
    return journal
group1 = {}
group1 = add_mark_correct('Ivanov', 5, group1)
group1 = add_mark_correct('Tihonova', 4, group1)
print(group1)

group2 = add_mark_correct('Smirnov', 3)
print(group2)
group3 = add_mark_correct('Kuznetsova', 5)
print(group3)


def add_mark(name, mark, journal=None):
    # Добавьте здесь проверку аргумента mark
    if  mark not in [2,3,4,5]:
        raise ValueError("Invalid Mark!")
    if journal is None:
        journal = {}

    journal[name] = mark
    return journal

# попытка вызвать функцию с некорректными аргументами
try:
    print(add_mark('Ivanov', 6))
# должна завершиться с ошибкой ValueError, которую мы выведем в блоке except
except ValueError as e:
    print(e)