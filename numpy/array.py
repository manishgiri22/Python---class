#to add or install numpy in your system in pip install numpy
import numpy 
# arr= numpy.array([2,1,4,5,6,7])
# print(arr)
# print(numpy.__version__)
# print(type(arr))
arr_0=numpy.array(43)       # 0 DIMENSIONAL ARRAY 
arr_1=numpy.array([2,1,2,3,4])  # 1 DIMENSIONAL ARRAY
arr_2=numpy.array([[11,3,4,5],[2,4,5,6]])      #2 DIMENSIONAL ARRAY 
arr_3=numpy.array([[[1,2,3],[1,2,3],[3,4,5]]])
print(arr_0)
print(arr_1)
print(arr_2)
print(arr_3)
#ndim is attribute is used to check how many dimenstion that having the array have 
print(arr_0.ndim)

import numpy as np 
arr=np.array([2,4,5,6,5])
print(arr, arr.ndim)
