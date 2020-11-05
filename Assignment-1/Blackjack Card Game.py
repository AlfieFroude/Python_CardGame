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
    global players_hand
    players_hand = []
    print("You have been dealt 2 cards:")
    deal_hand()

def deal_hand():
    initial_deal_amount = 2
    for i in range(initial_deal_amount):
        card_dealt = one_shuffled_deck(1)
        print(card_dealt)
        players_hand.append(card_dealt)
        #the peramiter inputted is the number of cards dealt initially in blackjack

#def deal():

#def fold():

def one_shuffled_deck(x):

    suits = ['Hearts ♥', 'Spades ♠', 'Diamonds ♦', 'Clubs ♣']
    royals = ["J", "Q", "K", "A"]
    numbered_cards = []
    global deck
    deck = []

    #card_values = {'A':11,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}]
    #Ace set high, changes to low if need be during gameplay

    # loops a set amount appending a new interger each time starting from 2
    for i in range(2,11):
        numbered_cards.append(str(i))
        # numbers 2-10 added to numbered_cards and converted to strings
    
    for o in range(4):
        numbered_cards.append(royals[o])
        # royal cards added to numbered_cards to complete basic card order

    for p in range(4):
        for r in range(13):
            card = (numbered_cards[r] + " of " + suits[p])
            deck.append(card)
        # creates 4 sets of 13 cards with different suits and appends them into deck

    random.shuffle(deck)
    # shuffles deck

    h = random.randint(0, 53)
    card_picked = deck.pop(h)
    return card_picked

        #when function is called a random card to drawn from the deck


    
def rules():
    print("Aim:\n Get your hand's total as close to 21 as possible.\n If you exceed 21 you are bust.\n If you get 21 you have blackjack.\n  - In this case, you can only be beat if the dealer gets blackjack aswell. (This results in a DRAW).\n If you get anything below blackjack you just need to get higher than the dealer to WIN.\n")
    print("How To Play: ")
    print("1) You will be dealt 2 cards\n2) You have 2 options, FOLD or DRAW\n  FOLD: Stop your play\n  DRAW: Draw another card\n3) Get your hand value to 21 or higher than the dealers hand\n4) Don't get BUST! ")
    
    input("\nPress Any Key To Continue...")
    start()

def end():
    sys.exit()

if __name__ == "__main__":
    start()