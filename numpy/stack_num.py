import numpy as np 
a=np.array([[1,2,3],[2,4,6]])
b=np.array([[5,7,3],[9,8,1]])
print(np.vstack((a,b)))           #to stack the elements vertically 
print(np.hstack((a,b)))           #to stack the elements horizontally
#splitting in array numpy
# Splitting:For splitting, we have these functions:
# np.hsplit: Split array along horizontal axis.
# np.vsplit: Split array along vertical axis.
# np.array_split: Split array along specified axis
print(np.hsplit(a,1))
print(np.vsplit(b,1))