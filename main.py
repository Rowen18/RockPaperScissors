import random
valid_input = False
a = 0
while valid_input == False:
    compin = (random.randrange(0, 3))
#0=rock 1=paper 2=scissors
    x = "The computer picked "
    r = "rock. "
    p = "paper. "
    s = "scissors. "
    w = "You win!"
    t = "You tied."
    L = "You lose."
    if a == 0:
        usein = input("Welcome to rock, paper, scissors! Please type your choice:")
    if a == 1:
        usein = input("If you would like to play again, pick rock, paper, or scissors. If not, type stop.")
    if a == 2:
        usein = input("Try again.")
    if usein == "Rock" or usein == "rock":
        thing = 0
    elif usein == "Paper" or usein == "paper":
        thing = 1
    elif usein == "Scissors" or usein == "scissors":
        thing = 2
    elif usein == "Stop" or usein == "stop":
        thing = 3
    else:
        thing = 4
    if thing == compin:
        print(t)
        a = 1
    elif thing == 0 and compin == 1:
        print(x+p+L)
        a = 1
    elif thing == 0 and compin == 2:
        print(x+s+w)
        a = 1
    elif thing == 1 and compin == 0:
        print(x+r+w)
        a = 1
    elif thing == 1 and compin == 2:
        print(x+s+L)
        a = 1
    elif thing == 2 and compin == 0:
        print(x+r+L)
        a = 1
    elif thing == 2 and compin == 1:
        print(x+p+w)
        a = 1
    elif thing == 3:
        break
    else:
        print("Sorry, you can't use that in this game")
        a = 2