# Blackjack Card Game
#Alfie Froude 05/11/20

import random
from os import sys

global decksCreated
decksCreated = 0
global deck_amount
deck_amount = 53
global dealer_bust
dealer_bust = False
global dealersTurn
dealersTurn = False
global dealers_hand_value
dealers_hand_value = 0
global dealerScore
dealerScore = 0
global playerScore
playerScore = 0
global card_limit
card_limit = 0
"""Preset variables, used to keep track of score, turns, deck value and detects gameplay events."""

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
"""start is the main menu. Loops if null."""

def play():
    global turn
    turn = True
    global players_hand
    players_hand = []
    global hand_value
    hand_value = 0
    if decksCreated == 0:
        newDeck()
    print("You have been dealt 2 cards:\n")
    deal_hand()
    #The player is dealt their first 2 cards
    #print(hand_value)
    print("\nYour current hand is:\n")
    for i in players_hand:
        print(i, end=" ")
    #Prints players hand out
    gameplay()
"""
play is the code that starts the game off, a new deck is created, the players initial hand at the 
beginning of a round is dealt and their hand is presented to them via the for loop.
"""
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
"""gameplay is the event of the player choosing to deal or fold, OR bust if their hand exceeds 21.
"""

def deal_hand():
    i = 0
    initial_deal_amount = 2
    #the perameter inputted is the number of cards dealt initially in blackjack
    while(i != initial_deal_amount):
        card_dealt = deckEvents()
        print(card_dealt)
        players_hand.append(card_dealt)
        i = i + 1
"""
deal_hand gets the specified amount of cards(initial_deal_amount) from deckEvents, prints the card to the player
and the adds it to their hand, this is repeated until the initial_deal_amount parameter is met.
"""

def deal():
    print("You have been dealt a card:\n")
    card_dealt = deckEvents()
    print(card_dealt)
    players_hand.append(card_dealt)
    #print(hand_value)
    print("\nYour current hand is:\n")
    for i in players_hand:
        print(i, end=" ")
    if (i == 5)and(hand_value <= 21):
        cardTrick()
    else:
        gameplay()
"""
deal gets a card from deckEvents and adds it to the players hand, it them prints the players hand in full to
show them what cards they currently have, it also checks to see if they have a 5 card trick.
"""

def fold():
    print("\nYou have folded...")
    print("\nYour current hand is:\n")
    for i in players_hand:
        print(i, end=" ")
    print("\n\nThe total of your hand is: " + str(hand_value))
    global dealersTurn
    dealersTurn = True
    the_dealer()
"""
If the player chooses fold, they are presented with some text and their hand value is calculated and presented to them,
it is then the dealers go.
"""

def bust():
    if (hand_value > 21):
        lose_bust()
"""If players hand value exceeds 21, they go bust."""
        
class deckConstructor:
    def __init__(self, deckNum):
        self.deckNum = deckNum

    def buildDeck(self):
        suits = ['Hearts ♥', 'Spades ♠', 'Diamonds ♦', 'Clubs ♣']
        royals = ["J", "Q", "K", "A"]
        numbered_cards = []
        global deck
        deck = []

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

        global decksCreated
        decksCreated += 1
        return deck
"""
This is the deckConstructor, it's purpose is to generate a new deck of cards instance when called, inside deckConstructor is buildDeck.
buildDeck uses 4 for loops to construct a deck, the first for loop appends the values 2 - 10 to the numbered_cards array as strings, 
the second for loop appends the royals to numbered_cards, and finally the third for loop runs, once for each suit, another for loop which
runs 13 times, creating each unique card in the deck and appending it to an empty array called deck. And last of all, the deck is shuffled.
"""

def newDeck():
    d = deckConstructor(decksCreated + 1)
    global deckInPlay
    deckInPlay = d.buildDeck()
"""newDeck creates a new instance of a deck using deckConstructor if the first deck in play is used up during gameplay."""

def deckEvents():
    global deckInPlay
    global deck_amount
    global card_limit
    #preset values called from outside the function
    deck_amount = card_limit
    #sets the card limit to the current amount of cardsin the deck in play
    h = random.randint(0, card_limit)
    deck_amount-=1
    #randomly picks a card from the current deck and then updates the deck amount
    card_picked = deckInPlay.pop(h)
    card_value = card_picked[0]
    card_value_if10 = card_picked[1]
    #removes the card picked from the deck array and then assigns specific characters from the string of the card picked to 2 new variables
    if (card_value == "J" or card_value == "Q" or card_value == "K"):
        card_value = 10
    #if the character of the string of the card picked is equal to J or Q or K the the value of the card is set to 10
    elif (card_value == "A"):
        global dealersTurn
        global dealers_hand_value
        #preset values called from outside the function
        if (dealersTurn == True):
            if (dealers_hand_value > 10):
                card_value = 1
            else:
                card_value = 11
        #if its the dealers turn and their hand is greater than 10 then the ace is set to 1 else it is set to 11.
        else:
            aceValue = input("You have drawn an Ace!\nWould you like it to be valued as 1 (a) or 11 (b):")
            if (aceValue == "a"):
                card_value = 1
            elif (aceValue == "b"):
                card_value = 11
            #Ace set by player after it has been drawn from the deck
    elif (card_value_if10 == "0"):
        card_value = 10
    #This is the other variable created during the removing of the card picked from the deck, if the second character in the string of the card picked is equal to 0 then it is a 10.
    else:
        card_value = int(card_value)
    #if none of the if/elif statements are met then the card value is set to the interger of the character in the string of the card picked.
    if (turn == True):
        global hand_value
        hand_value = hand_value + card_value
    elif (turn == False):
        dealers_hand_value += int(card_value)
    return card_picked

"""
deckEvents is for sure over complicated, however its purpose is to randomly pick a card from the available deck and then give the card a value depending on what the card is,
it does this for both the dealer and player turn and it also handles whether the player wants their Ace to be a 1 or 11 or if its the dealers turn, it gives the Ace a value 
depending on the dealers current hand to give the dealer the best chance of winning.
"""

def the_dealer():
    global dealers_hand
    dealers_hand = []
    global dealers_hand_value
    dealers_hand_value = 0
    dealer_deal_hand()
    dealers_gameplay_logic()
"""the_dealer is where the dealers hand is created/reset"""

def dealers_gameplay_logic():
    while (dealers_hand_value <= 21):
        if (dealers_hand_value > hand_value):
            dealer_fold()
        elif (dealers_hand_value == hand_value):
            dealer_fold()
        elif (dealers_hand_value <= 11):
            dealer_deal()
        elif (17< hand_value < 22) and (dealers_hand_value < hand_value):
            dealer_deal()
        elif (11 < dealers_hand_value < 15) and (hand_value >= dealers_hand_value):
            dealer_deal()
        elif (11 < dealers_hand_value < 16) and (14 < hand_value < 22):
            dealer_deal()
        elif (15 < dealers_hand_value < 22) and (hand_value <= 15):
            dealer_fold()
        else:
            dealer_fold()
            break
    else:
        global dealer_bust
        dealer_bust = True
        dealer_fold()
"""
dealers_gameplay_logic is where the dealer plays the game on their turn, it uses basic logic to determine if it should DRAW or FOLD depending
on their hand value and the players hand value. (In a real game of blackjack the players play face up and the dealer goes last, so they would
be able to see the players hand.)
"""

def dealer_deal_hand():
    i = 0
    initial_deal_amount = 2
    #the perameter inputted is the number of cards dealt initially in blackjack
    while(i != initial_deal_amount):
        card_dealt = deckEvents()
        dealers_hand.append(card_dealt)
        i = i + 1
"""
dealer_deal_hand is the code that deals the first 2 cards to the dealers hand from deckEvents.
"""

def dealer_deal():
    card_dealt = deckEvents()
    dealers_hand.append(card_dealt)
    #print(hand_value)
    dealers_gameplay_logic()
"""
dealer_deal is where a single card is dealt to the dealers hand from deckEvents.
"""

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
"""
dealer_fold is run once the dealer is finished with their turn, because they either went bust or folded, if the dealer went bust and the player didn't the player wins.
Else the values in both the players and dealers hands are compared and the outcome is determined.
"""


def rules():
    print("Aim:\n Get your hand's total as close to 21 as possible.\n If you exceed 21 you are bust.\n If you get 21 you have blackjack.\n  - In this case, you can only be beat if the dealer gets blackjack aswell. (This results in a DRAW).\n If you get anything below blackjack you just need to get higher than the dealer to WIN.\n")
    print("How To Play: ")
    print("1) You will be dealt 2 cards\n2) You have 2 options, FOLD or DRAW\n  FOLD: Stop your play\n  DRAW: Draw another card\n3) Get your hand value to 21 or higher than the dealers hand\n4) Don't get BUST! ")
    input("\nPress Any Key To Continue...")
    start()
"""
rules is a bunch of text that instructs the user how to play.
"""

def win():
    print("\nYou beat the dealer!\n\n***YOU WIN***")
    global playerScore
    playerScore += 1
    print("The Score:\n YOU: "+ str(playerScore) + " V DEALER: " + str(dealerScore))
    playAgain()
"""
If the player wins this code is run and the score is updated.
"""

def draw():
    print("\nYou and the dealer both had the same value!\n\n***YOU DRAW***")
    print("The Score:\n YOU: "+ str(playerScore) + " V DEALER: " + str(dealerScore))
    playAgain()
"""
If the player draws this code is run and the score is updated.
"""

def lose_bust():
    print("\nYou got BUST!\n\n***YOU LOSE***")
    global dealerScore
    dealerScore += 1
    print("The Score:\n YOU: "+ str(playerScore) + " V DEALER: " + str(dealerScore))
    playAgain()
"""
If the player loses because of bust this code is run and the score is updated.
"""

def lose():
    print("\nThe dealer beat you!\n\n***YOU LOSE***")
    global dealerScore
    dealerScore += 1
    print("The Score:\n YOU: "+ str(playerScore) + " V DEALER: " + str(dealerScore))
    playAgain()
"""
If the player loses this code is run and the score is updated.
"""

def cardTrick():
    print("\nYou have a 5 card trick!\n\n***YOU WIN***")
    global playerScore
    playerScore += 1
    print("The Score:\n YOU: "+ str(playerScore) + " V DEALER: " + str(dealerScore))
    playAgain()
"""
If the player wins because of a 5 card trick this code is run and the score is updated.
"""

def playAgain():
    replay = input("\n\nPlay Again? yes(y) or no(n)")
    if replay == "y":
        reset()
    elif replay == "n":
        end()
    else:
        playAgain()
"""
playAgain is a statement that determines if the player wishes to play again or not.
"""

def reset():
    global players_hand
    players_hand = []
    global hand_value
    hand_value = 0
    global dealers_hand
    dealers_hand = []
    global dealers_hand_value
    dealers_hand_value = 0
    global dealer_bust
    dealer_bust = False
    global dealersTurn
    dealersTurn = False

    if len(deckInPlay) <= 10:
        newDeck()
        print("new deck created")
    play()
"""
reset changes all specified value back to their original values, then creates a new deck if the current deck is low and calls play()
"""

def end():
    sys.exit()

if __name__ == "__main__":
    start()