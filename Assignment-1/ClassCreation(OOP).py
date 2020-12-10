# OOP
# Creating a Card
# Alfie Froude 26/11/20

suits = [
    "Hearts"
    "Clubs"
    "Spades"
    "Diamonds"
    ]

face_values = [
    "Ace"
    "Two"
    "Three"
    "Four"
    "Five"
    "Six"
    "Seven"
    "Eight"
    "Nine"
    "Ten"
    "Jack"
    "Queen"
    "King"
]

class Card:
    """
    Object Oriented class for a single playing card
    card.suit => the suit of the card
    card.face_vlaue => the number etc. on the card
    card.value() => the number of points the card is worth
    """
    def __init__(self, suit, face_value):
        if suit in suits:
            self.suit = suit
        if face_value in face_values:
            self.face_value = face_value

    def __str__(self):
        return("Instance of class Card, the " + self.face_value + " of " + self.suit)

    def value(self):
        valueof = {
            "Ace": 11,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ten": 10,
            "Jack": 10,
            "Queen": 10,
            "King": 10
        }
        return(valueof[self.face_value])

new_card = Card("Hearts", "Seven")

print(new_card)

print(new_card.value())