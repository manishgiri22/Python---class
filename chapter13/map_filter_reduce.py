from functools import reduce
l=[2,3,4,5,6,7]
square=lambda x:x*x  #take 1 item at a time and calculate square
sqlist=map(square,l)    #map or listing the square in the new list 
print(list(sqlist))     #type casting of the map in the list 


#filter example
def even(n):
    if(n%2==0):
        return True
    return False
onlyeven=filter(even,l)
print(list(onlyeven))

#reduce example
#first import reduce from functools
def sum(a,b):
    return a+b          #return reduce function  
def mul(a,b):
    return a*b
print(reduce(sum,l))        # reduce (function, arguments)
print(reduce(mul,l))