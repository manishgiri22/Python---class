'''
1=snake
0=water
-1=gun

'''
import random
computer= random.choice([-1,0,1])
you= int(input("enter your choice (-1,0,1):"))
playerDict={
    -1:"gun",
    0:"water",
    1:"snake"
}
reverseDict={
    "gun":-1,
    "water":0,
    "snake":1
}
choice=playerDict[you]
comp=playerDict[computer]
print(f"your choice is {reverseDict[choice]} and computer choice is {reverseDict[comp]}")
if(computer==you):
    print("its draw ")
else:
    if(computer==-1 and you==0):
        print("player wins")
    elif(computer==-1 and you==1):
        print("you lose")
    elif(computer==0 and you==-1):
        print("you lose")
    elif(computer==0 and you==1):
        print("player wins")
    elif(computer==1 and you==-1):
        print("player wins")
    elif(computer==1 and you==0):
        print("you lose")
    else:
        print("something getting wrong here")