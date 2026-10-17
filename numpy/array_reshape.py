import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3) #print 1-d to 2-d array
newar=arr.reshape(2,3,2)    #print 1-d array to 3-d array 
print(newarr)
print(newar)
print(newarr.ndim)
c= np.arange(1,12).shape(3,4)
print(c.ndim)