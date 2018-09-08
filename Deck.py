import Card

class Deck:
    card_ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'B', 'S']
    card_suits = ['C', 'D', 'H', 'S', 'J']

    def __init__(self):
        self.deck = [Card(rank + suit) for rank in self.card_ranks for suit in self.card_suits]
        self.deck.append(Card('JB'), Card('JS'))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    #temp method
    def print_deck(self):
        print(self.deck)