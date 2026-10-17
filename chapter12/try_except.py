print("this is try and except code")
try:
   
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    if(b!=0):
        print(a/b)
    else:
        raise ZeroDivisionError
except Exception as e:
    print(e)
    print("divide by zero")

