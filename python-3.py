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
print(int(strN[0])%2 == 0)

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

#4-0
try:
    print("before exception")
#    a = int(input("enter a "))
#    b = int(input("enter b "))
    a = 10
    b = 0
    c = a / b
#    print("c ", c)
except ZeroDivisionError as e:
    print("Error ", e)
else:
    print("Fine, c ", c)
finally:
    print("Finished!")

print("After exception ")

##Raise
try:
#    age = int(input("you age: "))
    age = -1
    if age > 100 or age <= 0:
        raise ValueError("you're too old or don'T exist")
except ValueError as age_error:
    print("age is wrong!")
    print("error ", age_error)
else:
    print("you are {} years old!".format(age))


#Check
#input1 = input("Enter number ")
input1 = 111
try:
    int1 = int(input1)
except ValueError as type_error:
    print("cauldn'T convert into number")
    print("Error: ", type_error)
else:
    print("You entered a right number ", int1, type(int1))
finally:
    print("Exit ")


#5.0
input1 = input("Enter number")
try:
    int1 = int(input1)
except ValueError as type_error:
    print("cauldn'T convert into number")
    print("Error: ", type_error)
else:
    print("You entered a right number ", int1, type(int1))
    if int1 % 2 == 0 or int1 % 3 == 0:
        print("number {} is divided by 2 or 3".format(int1))
    else:
        print("number {} is NOT divided by 2 or 3".format(int1))
finally:
    print("Exit ")

