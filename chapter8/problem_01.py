# finding the greatest of the three number using function;
def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(n1,"is greatest  number:")
    elif(n2>n1 and n2>n3):
        print(n2,"is  greatest number")
    else:
        print(n3,"is greatest number")
n1= int(input("enter the first number:"))
n2= int(input("enter the second number:"))
n3= int(input("enter third number:"))
greatest(n1,n2,n3)