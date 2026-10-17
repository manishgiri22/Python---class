import random 
n= random.randint(1,100)
a=-1
guesses=0
while (a!=n):
    a=int(input("guess the number from 1 to 100:"))
    if(a>n):
        print("guess lower")
    elif(a<n):
        print("guess higher")
    guesses+=1
print(f"you guess the number {n} in {guesses} times! ")
