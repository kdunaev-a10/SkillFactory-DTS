#1.4
def is_leap_year(x):
    return (int(x)%400 == 0) or (int(x)%4 == 0) and not (int(x)%100 == 0)

#y = input("Year ")
y = 1800
print(int(y)%400)
print(int(y)%4)
print(int(y)%100)
print(is_leap_year(y))


#1.8
diagnosis_1 = 'yes'
diagnosis_2 = 'no'
diagnosis_3 = 'no'

result = (diagnosis_1 == 'yes') or (diagnosis_2 == 'no') or (diagnosis_3 == 'no')
print(result)

number = 1234567
str1 = str(number)
list1 = list(str1)
print(list1)
map1 = list(map(int,list1))
print(map1)
print(10 in map1)

print("3" in str(number))
print("7" in str(number))

a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

#2.2
print(a is None) #RIGHT USE OF None
print(a == None) #BAD USE OF None!

N = 27395
strN = str(N)
print(int(strN[0])%2 is 0)

#2.3
list_1 = [1, 2]

list_2 = [1, 2, 3]
val = list_2.pop()

print(list_1 == list_2)

#3.1
a = 7
b = 9+a
print("a=F(",b,")")

#3.2
s = 5
a = 10
if a > 0:
    s = s + a
else:
    s = s - a
print(s)


print(bool(0))  # False
print(bool(1))  # True
print(bool("")) # False
print(bool("1"))  # True
print(bool([])) # False
print(bool([1]))  # True

zero = 50%3
if zero :
    print("divide by", zero)
else:
    print("cant divide by", zero)

pass1 = ""
if not pass1:
    print("forgot to enter pass")