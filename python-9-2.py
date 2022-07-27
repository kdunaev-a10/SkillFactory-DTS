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