empty_list = list()
print(empty_list)
another_empty_list = []
print(another_empty_list)

a = range(1, 10)
print(a)
a = range(10)
print(a)
a = range(10, 1, -1)
print(a)
a = range(0, 10, 2)
print(a)
a = list(range(0, 10, 2))
print(a)


a = ["a", "b", "c", "d", "e"]
print(a[-1])

print(a[0:4:2])
print(a[::-1])

a = list(range(-3, 7))
print(a)
a_slice = a[::-1]
print(a_slice[:2])

a = list(range(-3, 7))
print(a)
a_slice = a[-4:-2]
print(a_slice)

#2.10
s = 'hello kitty'.split()
print(s)
s_slice = s[::-1]
print(s_slice[:2])

my_str = 'hello kitty'
my_list = my_str.split()
print(my_list[-2:])

####
#Lists
#####
#2.12
orders_daily = []
a = "order1"
b = "order2"
c = "order3"
orders_daily.append(a)
orders_daily.append(b)
orders_daily.append(c)
print(orders_daily)

# 2.13

book1 = "my book"
book2 = "your book"
books = ["all_books"]
books.append(book1)
books.append(book2)
print(books)
# 2.14
books.clear()
print(books)

#2.15
numbers = [1,5,3,1,4,5,6,7,5,8]
print(numbers.count(5))

#2.16
my_books = ["book1", "book2", "book3", "book4", "book5"]
tom_books = my_books.copy()
print(tom_books, my_books)

#2.17
my_books = ["order1", "order2", "order3", "order4", "order5"]
tom_books = my_books[:]
print(tom_books, my_books)

#2.18
my_orders = ["order1", "order2", "order3"]
my_books = ["book1", "book2"]
my_orders.extend(my_books)
print(my_orders)

#2.19
nums = list(range(1,11))
nums.reverse()
print(nums)

#2.20
random_values = [3, 5, 0, -1, 2, 10, 15, -5]
random_values.sort()
print(random_values)

#2.21
list1=[5]
list1.append(0.2)
list1.append("hello there")
list1.append([1,2,3,4])
list1.append("bye")
print(list1)


a = (1,2,3,4,5,6)
# создадим кортеж
b = [1,2,3,4,5,6]
# создадим список с теми же элементами, что в кортеже выше
print(a.__sizeof__())
print(b.__sizeof__())

#2.24
tpl2 = tuple()
tpl3 = ("s")
print(tpl3)
tpl4 = ("s", )
print(tpl4)
#2.25
tpl5 = (255,)
print(tpl5)
#2.26
tpl5 = (15,22,0)
print(tpl5)

#Dict
my_dict = dict()
my_dict1 = {}
print(my_dict, my_dict1)

#3.6
alphabet_dict = {"a":1,"b":2,"c":3,"d":4,"e":5}
print(alphabet_dict["d"])

#3.7
alphabet_dict = {1:100,2:50,3:10}
print(alphabet_dict[2])
#3.8
alphabet_dict[4] = 5
print(alphabet_dict)
#3.9
alphabet_dict[3] = 25
print(alphabet_dict)
#3.10
alphabet_dict.clear()
print(alphabet_dict)

#3.11
place_and_money = {1: 100, 2: 50, 3: 10}
print(place_and_money.keys())

#3.12
name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
print(name_to_age.keys())

#3.13
name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
print(name_to_age.values())

#3.14
place_and_money = {1: 100, 2: 50, 3: 10}
print(place_and_money.values())

#3.15
place_and_money = {1: 100, 2: 50, 3: 10}
print(place_and_money.get(20,0))

#3.16
name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
print(name_to_age.get("Danny", -1))

#3.17
place_and_money = {1: 100, 2: 50, 3: 10}
place_and_money.update({4:5,5:1})
print(place_and_money)

#3.18
name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
name_to_age.update({'Anne': 23, 'Phillip': 29})
print(name_to_age)

#3.19
place_and_money = {1: 100, 2: 50, 3: 10}
result = place_and_money.pop(3)
print(place_and_money, result)

#3.20
name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
result = name_to_age.pop("Anton")
print(name_to_age, result)

#3.21
place_and_money = {1: 100, 2: 50, 3: 10}
place_and_money.setdefault(10,1)
print(place_and_money)

#3.22
name_to_age = {'Anne': 22, 'Anton': 27, 'Phillip': 30}
name_to_age.setdefault('Anne',32)
print(name_to_age)

#3.23
d = {}
d[5] = [3,4,5]
d.update({(3,4,5):"strong man"})
print(d)

#3.24
d = {}
d["name"] = "Sancho"
d["surname"] = "Panso"
d.update({'info':{'age': 35, 'country': 'Mexico'}})
print(d)

#3.25
d = {}
d["info"] = [10, 15, 27]
d["about"] = {'game': 'football', 'period': 5}
print(d)
d["about"] = "dont know"
print(d)

#4.1
s = set()
print(s)

#4.2
s = {5,10,3,2,11}
print(s)

#4.3
s3 = set('wow thats cool')
print(s3)