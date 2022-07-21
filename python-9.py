# Импортируем объект Counter из модуля collections
from calendar import day_abbr
from collections import Counter
from operator import le
from pydoc import ModuleScanner
# Создаём пустой объект Counter
c = Counter()
c['red'] += 1
print(c)
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter(cars)
print(c)
print(c['red'])
print(c['purple'])
print(sum(c.values()))

cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print('elements in moscow:', counter_moscow)
print('elements in spb:', counter_spb)

print (counter_moscow + counter_spb)
print(counter_moscow - counter_spb)
# Counter({'black': 2, 'yellow': 1})

#counter_moscow.subtract(counter_spb)
#print(counter_moscow)
#Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})

print(*counter_moscow.elements())
print(list(counter_moscow))
print(dict(counter_moscow))
print(counter_moscow.most_common())
print(counter_moscow.most_common(2))

counter_moscow.clear()
print(counter_moscow)

###9
print()
print('#9')
print()

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
groups = dict()
 
for student, group in students:
    # Проверяем, есть ли уже эта группа в словаре
    if group not in groups:
        # Если группы ещё нет в словаре, создаём для неё пустой список
        groups[group] = list()
    groups[group].append(student)
 
print(groups)

from collections import defaultdict
groups = defaultdict(list)
for st, gr in students:
    groups[gr].append(st)

print(groups)
print(groups[2021])
print(groups)

dict_object = dict()
defaultdict_object = defaultdict()
 
print(type(dict_object))
# <class 'dict'>
print(type(defaultdict_object))
# <class 'collections.defaultdict'>
print(dict_object)
# {}
print(defaultdict_object)
# defaultdict(None, {})


#9.2
print()
print('###9.2')
print()
import sys
print(sys.version)

from collections import OrderedDict
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client = OrderedDict(data)
print(ordered_client)

ordered_client_ages = OrderedDict(sorted(data, key = lambda k: k[1]))
print(ordered_client_ages)
ordered_client_ages['Nikita'] = 18
print(ordered_client_ages)

print('###deque')

from collections import deque
dq = deque()
print(dq)

clients = deque()
clients.append('Ivanov')
clients.append('Petrov')
clients.append('Smirnov')
clients.append('Tikhonova')

print(clients)
print(clients[2])

first_client = clients.popleft()
second_client = clients.popleft()
 
print("First client:", first_client)
print("Second client:", second_client)
print(clients)

clients.appendleft('Vip-client')
 
print(clients)
tired_client = clients.pop()
print(tired_client, "left the queue")
print(clients)

clients = deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
del clients[2]
print(clients)


shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extend([11, 12, 13, 14, 15, 16, 17])
print(shop)

shop = deque([1, 2, 3, 4, 5])
print(shop)
# deque([1, 2, 3, 4, 5])
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)

print()
limited = deque(maxlen=3) 
print(limited)
# deque([], maxlen=3)
limited_from_list = deque([1,3,4,5,6,7], maxlen=3)
print(limited_from_list)
limited_from_list.append(8)
print(limited_from_list)

print()
temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]
days = deque(maxlen=7)
for temp in temps:
    days.append(temp)
    if len(days) == days.maxlen:
        print(round(sum(days)/len(days),2), end=';')
        print(days)

print()
dq = deque([1,2,3,4,5])
print(dq)
dq.reverse()
print(dq)

dq = deque([1,2,3,4,5])
dq.rotate(2)
print(dq)

dq = deque([1,2,3,4,5])
dq.rotate(-2)
print(dq)

dq = [1,2,4,2,3,1,5,4,4,4,4,4,3]
print(dq.index(4))
print(dq.count(4))

#print(dq.index(25))
# ValueError: 25 is not in deque
#print(dq.count(25))
# 0
dq.clear()
print(dq)


#9.3.2
print()
print('###9.3.2')
print()

temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5),
        ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4),
        ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8),
        ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7),
        ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5),
        ('2020', 1.5)]
temp_dict = OrderedDict(sorted(temps, key = lambda x: x[1], reverse=True))
print(temp_dict)

#9.3.5
print()
print('###9.3.5')
print()
users = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]
dq_users=deque(users)

print(dq_users)
print(dq_users.popleft())
print(dq_users)

dq_users.rotate(-5)
print(dq_users)
print(dq_users.pop())

print(dq_users.count(8))


#9.4.3
print()
print('###9.4.3')
print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False

