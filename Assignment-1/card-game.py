# Card Game Program
# Alfie Froude 5/11/20

import array
import random

#Start Up - set up variables

while True:
    # Play the game
    play()

def play():
    while player_not_bust():
        deal()

def deal():
    player_hand = deck()

#Create a Card Deck
class card_deck():
    deck = {}

    suit = ['hearts', 'spades', 'diamond', 'clubs']

    ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace']

    values = ['two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
             'eight':8,'nine':9, 'ten':10, 'jack':11,
             'queen':12, 'king':13, 'ace':1,]