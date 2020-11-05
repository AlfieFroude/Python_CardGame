# Card Game Program
# Alfie Froude 5/11/20

import array
import random

#Start Up - set up variables
"""
while True:
    # Play the game
    play()

def play():
    while player_not_bust():
        deal()

#def deal():
"""

#Create a Card Deck
def card_deck():

    suits = ['Hearts ♥', 'Spades ♠', 'Diamonds ♦', 'Clubs ♣']
    royals = ["J", "Q", "K", "A"]
    numbered_cards = []
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

    random.shuffle(deck)

if __name__ == "__main__":
    card_deck()