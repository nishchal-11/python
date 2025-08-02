import random
def game():
    print("ypu are playing the game")
    score=random.randint(1,99)
    print(f"your score:{score}")
    with open("highscore.txt")as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0
    if(score>highscore or highscore ==""):
         with open("highscore.txt","w")as f:
            f.write(str(score))
    return score
game()