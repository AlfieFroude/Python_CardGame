# Blackjack Card Game
#Alfie Froude 05/11/20
import random
import sys

def start():
    print("\n~~~Welcome to Blackjack!~~~\n")
    begin = input("Start 's'\n\nHow To Play 'r'\n\nQuit 'q'\n\n\nINPUT:")
    if (begin == "r"):
        rules()
    elif (begin == "s"):
        play()
    elif (begin == "q"):
        end()
    else:
        start()

def play():
    print("***Insert Gameplay Here***")

def rules():
    print("Aim:\n Get your hand's total as close to 21 as possible.\n If you exceed 21 you are bust.\n If you get 21 you have blackjack.\n  - In this case, you can only be beat if the dealer gets blackjack aswell. (This results in a DRAW).\n If you get anything below blackjack you just need to get higher than the dealer to WIN.\n")
    print("How To Play: ")
    print("1) You will be delt 2 cards\n2) You have 2 options, FOLD or DRAW\n  FOLD: Stop your play\n  DRAW: Draw another card\n3) Get your hand value to 21 or higher than the dealers hand\n4) Don't get BUST! ")
    
    input("\nPress Any Key To Continue...")
    start()

def end():
    sys.exit()

if __name__ == "__main__":
    start()