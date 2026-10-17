a=int(input("enter first the numbers:"))
b=int(input("enter the numbers:"))
c=int(input("enter third numbers:"))
d=int(input("enter fourth numver:"))
if(a>b and a>c and a>d):
    print("a is the largest number")
elif(b>a and b>c and b>d):
    print("b is the largest number")
elif(c>a and c>b and c>d):
    print(f"c is the largerst number{c}")
else:
    print("d is the largest number")
print("it is the end of the code")