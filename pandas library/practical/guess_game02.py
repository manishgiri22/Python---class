import random;
guess=random.randint(1,100);
count=0;
input_num=-1;
while(guess==input_num):
    input_num=int(input("guess the number"));
    if(guess>=input_num):
        print("you're guessing to much high ");
        count+=1;
    elif(input_num>guess):
        print("you're guessing to low please go high");
        count+=1;
print(f"you guess the correct answer in {count} times");