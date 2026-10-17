n=int(input("enter a number /(1 to add  , 2 to sub, 3 to mul , 4 to div /)"))
num1=int(input("enter first number"))
num2=int(input("enter second number"))
match n:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)