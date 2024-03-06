import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    return [Card(suit, value) for suit in suits for value in values]

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal(deck, num_hands=4):
    return [deck[i::num_hands] for i in range(num_hands)]
