a = "3.14"
print(type(a))

a = 5
print(id(a), a)
b=10
print(id(b), b)
a = a + b
print(id(a), a)

print(5/2)
print(5//2)
print(5%2)

print(-5/2)
print(-5//2)
print(-5%2)

print("test")
print (13 % -3 * 3)
print (3**2)

f = 653457
g = 123493
#print(len(str(f**g)))

a = 5.4321**100
print(a*1000)

print(1.3+2.3)

print("decimal")
from decimal import *
getcontext().prec = 6
print(Decimal(1) / Decimal(2))
print(Decimal(1.3)+Decimal(2.3))

print(round(11*2.5/3,2))
print(round(3.14159**2/2))

print(3 > 10)
print(3 == 10)
print(3 < 10)

print(1.57*3/1.5 == 3.14)
print(3**3 - 3* (6*3 - 4.5*2))

s1 = "Per"
s2 = "fec"
s3 = "fe"
s4 = "ct"
new_string = "Perfect"
print(new_string.find('P'))
print(new_string[::-1])

colors = 'red blue green'
print(colors.split())

animal = 'bear,1,0,0,1,0,0,1,1,1,1,0,0,4,0,0,1,1'
print(animal.split(','))

colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности
colors_joined = " . ".join(colors_split) # объединение строк
print('Color joined')
print(colors_joined)

#str = input("enter numbers separated with space")
str = "1 2 3 4"
str_split = str.split()
print(str_split)
str_join = "\n".join(str_split)
print(str_join)

cur_date = "10.10.2000"
currency = 'EUR'
rate = 86.93

print('the currency {2} on date {1} had value {2:.3f}'.format(currency,cur_date,rate) )
print(f'the currency {currency} on date {cur_date} had value {rate:.3f}' )

name = 'John'
dayofweek = 'Friday'
print('Hello, {}! Today is {}. Have a nice day!'.format(name,dayofweek) )

a = 5.4321
print(a+10)

empty_list = list()
print(empty_list)
another_empty_list = []
print(another_empty_list)