import random
valid_input = False
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
    usein = input("Welcome to rock, paper, scissors! Please type your choice:")
    if usein == "rock" and compin == 0:
        print(x+r+t) and valid_input == True
    elif usein == "rock" and compin == 1:
        print(x+p+L) and valid_input == True
    elif usein == "rock" and compin == 2:
        print(x+s+w) and valid_input == True
    elif usein == "paper" and compin == 0:
        print(x+r+w) and valid_input == True
    elif usein == "paper" and compin == 1:
        print(x+p+t) and valid_input == True
    elif usein == "paper" and compin == 2:
        print(x+s+L) and valid_input == True
    elif usein == "scissors" and compin == 0:
        print(x+r+L) and valid_input == True
    elif usein == "scissors" and compin == 1:
        print(x+p+w) and valid_input == True
    elif usein == "scissors" and compin == 2:
        print(x+s+t) and valid_input == True
    elif usein == "stop":
        break
    elif usein != "rock" and usein != "paper" and usein != "scissors":
        print("Sorry, you can't use that in this game.")
