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

result = (diagnosis_1 == 'yes') or (diagnosis_2 == 'yes') or (diagnosis_3 == 'yes')
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
if "3" in str(number) and  "7" in str(number):
    print("3 and 7 are in")
else:
    print("3 and 7 are not")

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
if int(strN[0])%2 == 0:
    print("2.2: beging with odd")

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


#4.6
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
#input1 = input("Enter number")
input1 = "SSS"
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

#6.0
x = 1
y = -4
if x > 0 and y > 0:
    print("1st quarter")
if x < 0 and y > 0:
    print("2nd quarter")
if x < 0 and y < 0:
    print("3d quarter")
if x > 0 and y < 0:
    print("4th quarter")

#month_num = int(input("month number (1,2,3,4...12)"))
month_num = 3
if month_num in [3, 4, 5]:
    print("Spring")
elif month_num in [6, 7, 8]:
    print("Summer")
elif month_num in [9, 10, 11]:
    print("Autumn")
else:
    print("Winter")

def get_wind_class(speed):  # Объявление функции
    if 1 <= speed <= 4:
        return("weak [1]")
    elif 5 <= speed <= 10:
        return ("moderate [2]")
    elif 11 <= speed <= 18:
        return ("strong [3]")
    elif speed >= 19:
        return ("hurricane [4]")
    else:
         return("Wrong number")

print(get_wind_class(6))  # Печатаем результат выполнения


user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    #if username in user_database.keys():
    if username in user_database:
        print("name is found")
        if user_database[username] == password:
            return True
        else:
            return False
    else:
        return False

print(check_user("password", "test"))
print(check_user("hesoyam", "test"))
print(check_user("hesoyam", "tgm"))

a = 42
b = 41
#BAD!
if a > b:
    result = a
else:
    result = b

#GOOD!
result = a if a > b else b
#ИЛИ
result = (b, a)[a > b]

#5.5
A = 55
B = 45
C = 7

if (A < 45 and B >= 45 and C >= 45)  or \
        (A >= 45 and B < 45 and C >= 45)  or \
        (A >= 45 and B >= 45 and C < 45):
    print("5.5", True)
else:
    print("5.5", False)

#5.6
#if  not (A > -10 and A < -1) and  not (A > 2 and A < 15):
if not (-10 <= A <= -1 or 2 <= A <= 15):
    print("5.6 not belong ", True)
else:
    print("5.6 belong", False)

#5.7
number = 66
str1 = str(number)
list1 = list(str1)
print(list1)
if "5" in list1:
    print("5 is in")
else:
    print("5 is not")

map1 = list(map(int,list1))
print(map1)
if 5 in map1:
    print("5 is in")
else:
    print("5 is not")

if number // 10 == 5 or number % 10 == 5:
    print("5 is in")
else:
    print("5 is not")

#5.8
list1 = [1, 2, 5, 3, 9]
set1 = set(list1)
if  len(list1) == len(set1):
    print("all unique")
else:
    print("not unique")

print(len(list1) == len(set(list1)))

#5.9
num = 12344321
#list1 = list(str(num))
#list_reverse = list1[::-1]
#print(list1)
#print(list_reverse)
#if list_reverse == list1:
if str(num) == str(num)[::-1]:
    print("Polindrom!")
else:
    print("Not polindrom")

A = -1
res = 45 if A > 0 else 50
print(res)

user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

print("user" in user_database)