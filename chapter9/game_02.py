import random
def game():
    print("you are playing a game")
    score=random.randint(1,400)
    with open("high_score.txt","r") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=(int(highscore))
        else:
            highscore=0
    print(f"your score is {score}")
    if(score>highscore):
        with open("high_score.txt","w") as f:
            f.write(str(highscore))
    return score
game()
    

