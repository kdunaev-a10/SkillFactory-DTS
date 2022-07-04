def multiply_lst(lst):
    if len(lst) == 0:
        return 0
    return lst[0] * multiply_lst(lst[1:])

my_lst = [10, 21, 24, 12]

print(multiply_lst(my_lst))