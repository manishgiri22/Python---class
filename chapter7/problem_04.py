#write a python program to calulate a factorial of the given number 
num = int(input("enter any number to find a factorial:"))
i=1, fact=1
for i in range(i,num+1):
    fact=fact*i
    i+=1
print(fact,"factorial is this :")