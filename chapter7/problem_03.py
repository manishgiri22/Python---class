num=int(input("enter a number to check is it prime:"))
count=0
i=1
for  i in range(1,num):
    if(num % i==0):
        count+=1
    i+=1
if(count==2):
    print(f"the given{num} is prime number")
