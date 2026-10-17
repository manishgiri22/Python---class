import numpy as np 
arr1=np.array([2,3,4,5,6,7])
# print(np.sort(arr1))
# print(np.array_split(arr1,3))
# print(np.join(arr1))


# filter arrary in python 
'''arr=np.array([12,42,4,12,34,28,69,87])
newarr=[]
for element in arr:
    if element>42:
        newarr.append(True)
    else:
        newarr.append(False)
filter_arr=newarr
print(filter_arr)
print(newarr)'
'''

# Create a filter array that will return only even elements from the original array:
'''
arr=np.array([12,42,4,12,34,28,69,87])
filter_arr=[]
for element in arr:
    if element % 2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(newarr)
print(filter_arr)
arr2=np.array([1,2,8,3,9,4,5])
join_arr=np.concatenate((arr,arr2))
print(join_arr)
'''

# transpose of an array
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.transpose(arr)
print(arr)
print(arr2)
 # add array 
print(np.add(arr,arr2))
print(np.subtract(arr2,arr))