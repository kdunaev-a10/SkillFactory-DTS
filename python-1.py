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
