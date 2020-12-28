import random

decksCreated = 0

class deck:
    def __init__(self, deckNum):
        self.deckNum = deckNum

    def buildDeck(self):
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

        global decksCreated
        decksCreated += 1
        return deck

d = deck(decksCreated + 1)
deckInPlay = d.buildDeck()

print(deckInPlay)
print(decksCreated)
deckInPlay = d.buildDeck()
print(deckInPlay)
print(decksCreated)