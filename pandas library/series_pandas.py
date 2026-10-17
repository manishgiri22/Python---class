import pandas as pd
a=[2,4,5,66,7]
myvar=pd.Series(a)
print(myvar)
print(myvar[4])

#indexing the labels  change the index as your need or requirement . 
mylavel=pd.Series(a, index= ['a','b','c','d','e'])
print(mylavel)


