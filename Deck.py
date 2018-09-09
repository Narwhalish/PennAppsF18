from Card import Card
import random

class Deck:
    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = ['C', 'D', 'H', 'S']

    def __init__(self):
        self.deck = [Card(rank, suit) for rank in self.card_ranks for suit in self.card_suits]
        self.deck.append(Card('J', 'B'))
        self.deck.append(Card('J', 'S'))
        
        self.cards_left = True

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def get_deck(self):
        return self.deck

    def get_cards_left(self):
        return len(self.deck)
