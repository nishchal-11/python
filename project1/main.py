import random
computer =random.choice([-1,0,1])
youstr=input("enter your choice")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
reverseDict={1:"Snake",-1:"water",0:"Gun"}

print(f" you choose {reverseDict[you]}  computer choose {reverseDict[computer]}")
if(computer== you):
    print("draw")
else:
    if(computer==-1 and you ==1):
        print("you win")
    elif(computer==-1 and you ==0):
        print("you lose")

    elif(computer==1 and you ==-1):
        print("you lose")
    elif(computer==1 and you ==0):
        print("you lose")

    elif(computer==0 and you ==-1):
        print("you lose")
    elif(computer==0 and you ==1):
        print("you win")
    else:
        print("something wnet wrong")
