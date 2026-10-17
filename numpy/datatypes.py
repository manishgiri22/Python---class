'''
string , integer, float , boolean , complex

'''
import numpy as np    
arr=np.array([2,3,4,5,6,78])
print(arr.dtype)
arr_str=np.array(['manish','sohan','utsav','ram'])
print(arr_str.dtype)
arr_new=np.array(['manish','giri','rohan'],dtype='S')
print(arr_new)
print(arr_new.dtype)  #to print data type of the array 


# convert data type in the array using astype keyword by coping the existing array
arr_int=np.array([2,3,4,5,6,78])
new_arr=arr_int.astype('S')
print(new_arr)
print(new_arr.dtype)

#copy vs view (copy is copy of new array and view is just change in the view of the array )
arr=np.array([1,2,3,4,5,6])
x=arr.copy()
arr[0]=12           # change in orgianal array and check the result 
print(arr)
print(x)  # it will print the original array before change
print(x.base)
#view 
arr_view=np.array([2,4,5,6,7,7])
x=arr_view.view()
x[0]=20         #(change the view and both arrays )display  
print(x)
print(arr_view)
print(x.base)


#shape of array 
arr_view=np.array([2,4,5,6,7,7])   # how many elements in the array do have 
print(arr_view.shape) #it will print the shape of the array 
# result will be (0,6) because of this have 0 dimension array and the elemnts is 6
 

#to create the 5 dimensional array using ndmin 
dmin=np.array([1,2,3,4,5],ndmin=5)
print(dmin)
print("shape of the dmin array",dmin.shape)


