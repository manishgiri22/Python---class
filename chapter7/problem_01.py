# write a program to print multiplication table of given number  
n= int(input("enter a number to find multiplication:"))
i=0
while(i<=10):
    print(n,"*",i,"=",n*i)
    i+=1
else:
    print("successfull")