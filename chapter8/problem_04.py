'''
to print following pattern using recursion
***
**
*
'''
def pattern(n):
    if(n==0):   #base condition for the recursion
        return
    else:
        print("*"*n)   #to print the pattern
        pattern(n-1)   #to call the function with decreasing the n by 1.
pattern(3)    #calling function  by its name 