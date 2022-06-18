empty_list = list()
print(empty_list)
another_empty_list = []
print(another_empty_list)

a = range(1,10)
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

print(a[0:4:2] )
print(a[::-1])

a = list(range(-3,7))
print(a)
a_slice = a[::-1]
print(a_slice[:2])

a = list(range(-3,7))
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
a="order1"
b="order2"
c="order3"
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