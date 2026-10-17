
try:
    a=int(input("enter any number :"))
    b=int(input("enter the divisor:"))
    # res=a/b
    res=a/c
    # raise ZeroDivisionError
except ZeroDivisionError as e:
    print("error: zero division error ")
    print(e)
except ValueError as e:
    print(e)
    print("error: cannot divisible by string")
except NameError as e:
    print(e)
    print("please declare variable properly ")
finally:
    print(res)
print("rest of the program here ")