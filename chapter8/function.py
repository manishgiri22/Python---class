# def factorial(n):
#     if(n==0  or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# a=factorial(5)
# print("factorial is ",a)
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)
# res=factorial(5)
# print(f"{res} is the result of the factorial of the 5")

#lamda  arguments:expression 
res= lambda a , b: a+b
print(res(3,2))

# nested function while using of the lamda functionm 
def myfunc(n):
    return lambda a: a*n
mydoubler=myfunc(2)
print(mydoubler(10))

