import numpy as np
arr=np.array([[1,2,3,4],[2,3,4,5]])
for x in arr:
    for y in x:
        print(y)
    print('\n')
crr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in crr:
    for y in x:
        for z in y:
            print (z)
        print('\n')
# loop might be written down as below using nditr 
for x in np.nditer(crr):
    print(x)