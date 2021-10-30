import random
valid_input = False
a = 0
value = {"rock": ("scissors", "lizard"),
         "paper": ("rock", "spock"),
         "scissors": ("paper", "lizard"),
         "lizard": ("paper", "spock"),
         "spock": ("scissors", "rock")}
while valid_input == False:
    compin = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
#0=rock 1=paper 2=scissors
    w = "You win!"
    t = "You tied."
    L = "You lose."
    if a == 0:
        usein = input("Welcome to rock, paper, scissors, lizard, spock! Please type your choice:")
    elif a == 1:
        usein = input("If you would like to play again, please type your choice. If not, type stop.")
    elif a == 2:
        usein = input("Try again.")
    else:
        usein = input("I have no idea how you got this prompt, but if you want to input your choice I won't stop you.")
    if usein == "Rock" or usein == "rock":
        thing = "rock"
    elif usein == "Paper" or usein == "paper":
        thing = "paper"
    elif usein == "Scissors" or usein == "scissors":
        thing = "scissors"
    elif usein == "Lizard" or usein == "lizard":
        thing = "lizard"
    elif usein == "Spock" or usein == "spock":
        thing = "spock"
    elif usein == "Stop" or usein == "stop":
        thing = "stop"
    else:
        thing = 4
    try:
        if thing == compin:
            print(t)
            a = 1
        elif thing == "stop":
            break
        elif compin in value[thing]:
            print("The computer picked "+compin+". "+w)
            a = 1
        else:
            print("The computer picked "+compin+". "+L)
            a = 1
    except:
        print("Error: the tool you picked does not exist")
        a = 2
