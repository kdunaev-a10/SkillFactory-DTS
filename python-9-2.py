# Импортируем объект Counter из модуля collections
from calendar import day_abbr
from collections import Counter
from operator import le
from pydoc import ModuleScanner
from collections import defaultdict
from collections import deque
from collections import OrderedDict
from matplotlib.cbook import print_cycles
import numpy as np
import numpy as np

a = np.int8(25)
print(a)
print(type(a))
print()
print(np.iinfo(a))
print(np.iinfo(np.int64))

b = np.uint8(124)
print(type(b))
print(np.iinfo(b))
print(np.iinfo(np.uint32))
print(np.iinfo(np.uint64))
print(2**64-1, 2**128-1)

###
print('###')
a = np.int32(1000)
print(a)
# 1000
print(type(a))
# <class 'numpy.int32'>
a = np.int32(2056)
print(a)
# 2056
print(type(a))
# <class 'numpy.int32'>

a = np.int32(1000)
b = a + 25
print(b)
# 1025
print(type(b))
# <class 'numpy.int64'>

##
print('###')
a = np.int32(1000)
b = np.int8(25)
c = a + b
print(c)
# 1025
print(type(c))
# <class 'numpy.int32'>

a = np.int8(127)
print(a)
a = np.int8(128)
print(a)
a = np.int8(256)
print(a)
a = np.int8(260)
print(a)


###
print('###')
a = np.int32(2147483610)
b = np.int32(2147483605)
print(a, b)
# 2147483610 2147483605
#print(a + b)
print(np.int64(a) + np.int64(b))
# 4294967215

###Float
print('####')
print(np.finfo(np.float16))
# finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16)
print(np.finfo(np.float32))
# finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)
print(np.finfo(np.float64))
# finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)

print(np.float16(4.12))
# 4.12
print(np.float16(4.13))
# 4.13
print(np.float16(4.123))
# 4.12
print(np.float16(4.124))
# 4.125
print(np.float16(4.125))
# 4.125


###
print('###List')
print(np.sctypeDict )
print(len(np.sctypeDict))
print(*sorted(map(str, set(np.sctypeDict.values()))))


a = "Hello world!"
print(type(a))
# <class 'str'>
#a = np.str(a)
#print(type(a))
# <class 'str'>
a = np.str_(a)
print(type(a))
# <class 'numpy.str_'>

##5.5
print(np.int8(-456))


####
print('##ARRAYS')
arr = np.array([1,5,2,9,10])
print(arr)
print(type(arr))

nd_arr = np.array([
    [12, 45, 78],
    [34, 56, 13],
    [12, 98, 76]
])
print(nd_arr)
print(nd_arr.dtype)

arr = np.array([1,5,2,9,10], dtype=np.int8)
print(arr)
print(type(arr))
print(arr.dtype)

arr[2] = 2000
print(arr)
arr[2] = 125.5
print(arr)

arr = np.float32(arr)
print(arr)
print(arr.dtype)

arr = np.array([12321, -1234, 3435, -214, 100], dtype=np.int32)
print(arr)
print(arr.dtype)
arr = np.int8(arr)
print(arr)
print(arr.dtype)

###
print('####')

arr = np.array([1,5,2,9,10], dtype=np.int8)
nd_arr = np.array([
    [12, 45, 78],
    [34, 56, 13],
    [12, 98, 76]
], dtype=np.int16)
print(arr.ndim, arr.size, arr.shape, arr.itemsize)
print(nd_arr.ndim, nd_arr.size, nd_arr.shape, nd_arr.itemsize)

zeros_3d = np.zeros([3,4,3], np.int8)
print(zeros_3d, zeros_3d.shape)


print(np.arange(5))
print(np.arange(1,4))
print(np.arange(1,4,0.5))

print(np.arange(1,2,0.1, dtype=np.float16))


arr, step = np.linspace(1, 2, 10, retstep=True)
print(step)
arr, step = np.linspace(1, 2, 10, endpoint=False, retstep=True)
print(step)

##6.6
print('##6.6')
arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
print(step)

##6.7
print('##6.7')
arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
print(step)


###7
arr = np.arange(8)
print(arr)
arr.shape = (2,4)
print(arr)

arr_new = arr.reshape((4,2), order='F')
print('old',arr)
print('new',arr_new)

print(arr_new.shape)
arr_tr = arr_new.transpose()
print('transpose')
print(arr_tr.shape)
print(arr_tr)


###slices
arr = np.linspace(1, 2, 6)
print(arr)
print(arr[2])
print(arr[2:4])
print(arr[::-1])
print(arr[-1])


print("2d array")
nd_array =  np.linspace(0, 6, 12, endpoint=False).reshape(3,4)
print(nd_array)
print(nd_array[1][2])
print(nd_array[1,2])
print(nd_array[1,:2])
print(nd_array[:2,2])
print(nd_array[:,2])
print(nd_array[:2])

###7.2
print('###7.2')
nd_array = np.array([
    [-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
    [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
    [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
    [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
    [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
    [-16841, -25392, -17278,  11740,   5916,    -47, -32037]
])


print('')
print(nd_array[-1,-1])
print('')
print(nd_array[3])
print('')
print(nd_array[:,-2])
print('')
#arr_new = nd_array[1:4].reshape((4,2), order='F')
print(nd_array[1:4,2:5])
print('')
print(nd_array[::-1,-1])

####
print('####')

arr = np.array([23,12,45,12,23,4,15,3])
arr_new = np.sort(arr, )
print(arr)
# [23 12 45 12 23  4 15  3]
print(arr_new)
# [ 3  4 12 12 15 23 23 45]

arr = np.array([23,12,45,12,23,4,15,3])
print(arr.sort())
# None
print(arr)

print('####')
print('roots')
data = np.array([4, 9, -4, 3, -5])
roots = np.sqrt(data)
print(roots)

print(None is None)
# True
print(np.nan is np.nan)
# True
print(np.nan is None)
# False
print(sum(roots))
print(np.isnan(roots))
print(sum(np.isnan(roots)))

print(roots[np.isnan(roots)])
roots[np.isnan(roots)] = 0
print(roots)
print(sum(roots))


###7.5
print('###7.5')
mystery = np.array([ 12279, -26024,  28745,      0,  31244,  -2365,  -6974,  -9212,      0, -17722,
                     16132,  25933,      0, -16431,  29810])
nans_index = np.isnan(mystery)
# В переменную n_nan сохраните число пропущенных значений
n_nan = sum(nans_index)
# Заполните пропущенные значения в массиве mystery нулями
mystery[np.isnan(mystery)] = 0
print(mystery)
print(mystery.dtype)

# Поменяйте тип данных в массиве mystery на int32
mystery = np.int32(mystery)
print(mystery)


# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = np.sort(mystery)

# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
# по столбцам! Например, 1, 2, 3, 4 -> 1    3
#                                      2    4
table = array.reshape((5,3),order='F')
print(table)
#  Сохраните в переменную col средний столбец из table
col = table[:,1]
print(col)

#####
#vektors
print()
print()

vec1 = np.array([2, 4, 7, 2.5])
vec2 = np.array([12, 6, 3.6, 13])
print(vec1 + vec2)

list1 = [2, 4, 7, 2.5]
list2 = [12, 6, 3.6, 13]
print(list1 + list2)
print([x + y for x, y in zip(list1,list2)])

vec1 = np.array([2, 4, 7, 2.5])
vec2 = np.array([12, 6, 3.6])
#print(vec1 * vec2)
# ValueError: operands could not be broadcast together with shapes (4,) (3,)

vec = np.arange(5)
print(vec * 10)
# array([ 0, 10, 20, 30, 40])
print(vec ** 2)


vec1 = np.array([2, 4, 7, 2.5])
vec2 = np.array([12, 6, 3.6, 13])
arr = vec1 > vec2
print(type(arr))


####
vec = np.array([3, 4])
length = np.sqrt(np.sum(vec ** 2))
print(length)

length = np.linalg.norm(vec)
print(length)

vec1 = np.array([0, 3, 5])
vec2 = np.array([12, 4, 7])
dist = np.sqrt(np.sum((vec1 - vec2) ** 2))
print(dist)

dist = np.linalg.norm(vec1 - vec2)
print(dist)

vec1 = np.arange(1, 6)
vec2 = np.linspace(10, 20, 5)
dot = np.sum(vec1 * vec2)
print(dot)

dot = np.dot(vec1,vec2)
print(dot)

x = np.array([25, 0])
y = np.array([0, 10])
print("ortogonal: ", np.dot(x, y))


###8.4
print('##8.4')

a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

print(np.linalg.norm(a + b), np.linalg.norm(a) + np.linalg.norm(b))
print(np.linalg.norm(a + c), np.linalg.norm(a) + np.linalg.norm(c))
print(np.linalg.norm(c + b), np.linalg.norm(c) + np.linalg.norm(b))

###8.5
print('##8.5')
print(np.linalg.norm(a - b))
print(np.linalg.norm(a - c))
print(np.linalg.norm(c - b))



###8.6
print('##8.6')

print(np.dot(a,b))
print(np.dot(a,c))
print(np.dot(c,b))

###
print('##')
vec = np.array([2,7,18,28,18,1,8,4])
print(vec.min(), np.min(vec))
# 1
print(np.max(vec), vec.max())
# 28
print(vec.mean())

mystery = np.array([2,7,18,28,18,1,8,4])
print(np.min(mystery))
print(np.mean(mystery))
print(np.median(mystery))
print(np.std(mystery))


####9
print()
print()
print('###9')
print(np.random.rand())
print(np.random.rand() * 100)
print(np.random.rand(5))
print(np.random.rand(2,3))
#print(np.random.rand(2,3,2,4,5,6))

shape = (3, 4)
#print(np.random.rand(shape))
# TypeError: 'tuple' object cannot be interpreted as an integer
print(np.random.rand(*shape))

#Sample random
shape = (2, 3)
print(np.random.sample(shape))

#uniform
print()
print('##UNIFORM')
print(np.random.uniform(low=0.0, high=1.0, size=None))
print(np.random.uniform(10,50))
print(np.random.uniform(0.3,0.6, size = 5))

print(np.random.uniform(300,699, size = (2,3)))

#INT
print()
print('##INT')
print(np.random.randint(6,12, size = (2,3)))
print(np.random.randint(10, size = (2,3)))