#1.4
def is_leap_year(x):
    return ((x%400 == 0) or (x%4 == 0) and not (x%100 == 0))

y = input("Year")
print(is_leap_year(y))