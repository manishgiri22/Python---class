from random import randint
computer_number=random.randint(1,100)
print("guess the number that you gonna find out:")
guess_number=int(input("enter your guess:"))
count=0
while guess_number!=computer_number: 
    if guess_number==computer_number:
        print("you guess the correct number.")
        count+=1
        print(f"you guess the correct number in {count} times:")
    elif computer_number>guess_number:
        print("your guess is too low")
        count+=1
        print(f"you guess the correct number in {count} times:")
    elif guess_number>computer_number:
        print("your guess is to high")
        count+=1
        print(f"you guess the correct number in {count} times:")