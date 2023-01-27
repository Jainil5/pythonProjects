import random


def game(a,b):
    if a==0 and b==0:
        print("Draw")
    if a==2 and b==2:
        print("Draw")
    if a==5 and b==5:
        print("Draw")
    if a==0 and b==2:
        print("You win")
    if a==0 and b==5:
        print("Bot win")
    if a==2 and b==0:
        print("Bot win")
    if a==2 and b==5:
        print("You win")
    if a==5 and b==2:
        print("bot win")
    if a==5 and b==0:
        print("You win")



for i in range(10):
    x=random.choice([0,2,5])
    y=random.choice([0,2,5])
    print(x,y)
    print(game(x,y))