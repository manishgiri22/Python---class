# finally code is used for 
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
finally:
    print("it will run automatically by overriding the return in the function ")

def fun():
    try:
        print("this is try  block")
        return
        
    except Exception as e:
        print(e)
        return
    finally:                            #run in each condition after all  in return also 
        print("iam outside from the return rule in fuction:") #dominant and avoding the reuturn rule 
fun()