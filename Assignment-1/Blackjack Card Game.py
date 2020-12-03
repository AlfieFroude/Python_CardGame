# Blackjack Card Game
#Alfie Froude 05/11/20
import random
from os import sys

deck_amount = 53
global dealer_bust
dealer_bust = False

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
#This is the main menu. Loops if null

def play():
    global turn
    turn = True
    global players_hand
    players_hand = []
    global hand_value
    hand_value = 0
    print("You have been dealt 2 cards:\n")
    deal_hand()
    #The player is delt their first 2 cards
    #print(hand_value)
    print("\nYour current hand is:\n")
    for i in players_hand:
        print(i, end=" ")
    #Prints players hand out
    gameplay()

def gameplay():
    while hand_value <= 21:
        nextmove = input("\n\nWould you like to DRAW (d) or FOLD (f):\n\n\nINPUT:")
        if (nextmove == "d"):
            deal()
        elif (nextmove == "f"):
            global turn
            turn = False
            fold()
            break
    else:
        bust()
#Gameplay is the event of the player choosing to deal orr fold, it is often repeated therefor is in a seperate def
    

def deal_hand():
    i = 0
    initial_deal_amount = 2
    #the perameter inputted is the number of cards dealt initially in blackjack
    while(i != initial_deal_amount):
        card_dealt = one_shuffled_deck()
        print(card_dealt)
        players_hand.append(card_dealt)
        i = i + 1


def deal():
    print("You have been dealt a card:\n")
    card_dealt = one_shuffled_deck()
    print(card_dealt)
    players_hand.append(card_dealt)
    print(hand_value)
    print("\nYour current hand is:\n")
    for i in players_hand:
        print(i, end=" ")
    gameplay()
#The player is delt a single card from the deck

def fold():
    print("\nYou have folded...")
    print("\nYour current hand is:\n")
    for i in players_hand:
        print(i, end=" ")
    print("\n\nThe total of your hand is: " + str(hand_value))
    the_dealer()
#If the player chooses fold, this code is run, the dealer then gets their go

def bust():
    if (hand_value > 21):
        lose_bust()
#If players hand value exceeds 21, they go bust
        

def one_shuffled_deck():

    suits = ['Hearts ♥', 'Spades ♠', 'Diamonds ♦', 'Clubs ♣']
    royals = ["J", "Q", "K", "A"]
    numbered_cards = []
    global deck
    deck = []

    #card_values = {'A':11,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}]

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
    global deck_amount
    card_limit = 0
    deck_amount = card_limit
    h = random.randint(0, card_limit)
    deck_amount-=1
    card_picked = deck.pop(h)
    card_value = card_picked[0]
    card_value_if10 = card_picked[1]
    if (card_value == "J" or card_value == "Q" or card_value == "K"):
        card_value = 10
    elif (card_value == "A"):
        aceValue = input("You have drawn an Ace!\nWould you like it to be valued as 1 (a) or 11 (b):")
        if (aceValue == "a"):
            card_value = 1
        elif (aceValue == "b"):
            card_value = 11
        #Ace set by player after it has been drawn from the deck
    elif (card_value_if10 == "0"):
        card_value = 10
    else:
        card_value = int(card_value)
    if (turn == True):
        global hand_value
        hand_value = hand_value + card_value
    elif (turn == False):
        global dealers_hand_value
        dealers_hand_value = dealers_hand_value + card_value
    return card_picked

        #when function is called a random card to drawn from the deck

def the_dealer():
    global dealers_hand
    dealers_hand = []
    global dealers_hand_value
    dealers_hand_value = 0
    dealer_deal_hand()
    dealers_gameplay_logic()

def dealers_gameplay_logic():
    while (dealers_hand_value < 21):
        if (dealers_hand_value <= 16):
            dealer_deal()
        else:
            dealer_fold()
            break
    else:
        global dealer_bust
        dealer_bust = True
        dealer_fold()


def dealer_deal_hand():
    i = 0
    initial_deal_amount = 2
    #the perameter inputted is the number of cards dealt initially in blackjack
    while(i != initial_deal_amount):
        card_dealt = one_shuffled_deck()
        dealers_hand.append(card_dealt)
        i = i + 1

def dealer_deal():
    card_dealt = one_shuffled_deck()
    dealers_hand.append(card_dealt)
    #print(hand_value)
    dealers_gameplay_logic()

def dealer_fold():
    global hand_value
    global dealers_hand_value
    global dealer_bust
    print("\nThe Dealer got: " + str(dealers_hand_value))
    if (dealer_bust == True) & (hand_value <= 21):
        win()
    else:
        if (hand_value == dealers_hand_value):
            draw()
        elif (hand_value > dealers_hand_value ):
            win()
        elif (hand_value < dealers_hand_value):
            lose()


def rules():
    print("Aim:\n Get your hand's total as close to 21 as possible.\n If you exceed 21 you are bust.\n If you get 21 you have blackjack.\n  - In this case, you can only be beat if the dealer gets blackjack aswell. (This results in a DRAW).\n If you get anything below blackjack you just need to get higher than the dealer to WIN.\n")
    print("How To Play: ")
    print("1) You will be dealt 2 cards\n2) You have 2 options, FOLD or DRAW\n  FOLD: Stop your play\n  DRAW: Draw another card\n3) Get your hand value to 21 or higher than the dealers hand\n4) Don't get BUST! ")
    input("\nPress Any Key To Continue...")
    start()

def win():
    print("\n\nYou beat the dealer!\n\n***YOU WIN***")
    input("\n\n Press Any Key To Exit...")
    end()

def draw():
    print("\n\nYou and the dealer both had the same value!\n\n***YOU DRAW***")
    input("\n\n Press Any Key To Exit...")
    end()

def lose_bust():
    print("\n\nYou got BUST!\n\n***YOU LOSE***")
    input("\n\n Press Any Key To Exit...")
    end()

def lose():
    print("\n\nThe dealer beat you!\n\n***YOU LOSE***")
    input("\n\n Press Any Key To Exit...")
    end()

def end():
    sys.exit()

if __name__ == "__main__":
    start()