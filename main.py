import random
import win_loss_tracker
valid_input = False
a = 0
value = {"rock": ("scissors", "lizard"),
         "paper": ("rock", "spock"),
         "scissors": ("paper", "lizard"),
         "lizard": ("paper", "spock"),
         "spock": ("scissors", "rock")}

s1 = win_loss_tracker.stats(0, 0, 0)
while valid_input == False:
    compin = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
#0=rock 1=paper 2=scissors
    w = ". You win!"
    t = ". You tied."
    L = ". You lose."
    if a == 0:
        usein = input("Welcome to rock, paper, scissors, lizard, spock! Please type your choice:").lower()
    elif a == 1:
        usein = input("If you would like to play again, please type your choice. If not, type stop.").lower()
    elif a == 2:
        usein = input("Try again.").lower()
    else:
        usein = input("I have no idea how you got this prompt, but if you want to input your choice I won't stop you.").lower()
    try:
        if usein == compin:
            print("The computer picked "+compin+t)
            s1.incrementties()
            a = 1
        elif usein == "stop":
            break
        elif compin in value[usein]:
            print("The computer picked "+compin+w)
            s1.incrementwins()
            a = 1
        else:
            print("The computer picked "+compin+L)
            s1.incrementlosses()
            a = 1
    except:
        print("Error: the tool you picked does not exist")
        a = 2
