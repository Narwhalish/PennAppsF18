import Card

class Deck:
    card_ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', 'B', 'S']
    card_suits = ['C', 'D', 'H', 'S', 'J']

    def __init__(self):
        self.deck = [Card(rank + suit) for rank in self.card_ranks for suit in self.card_suits]
        self.deck.append(Card('JB'), Card('JS'))
        self.cards_left = True

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) == 1:
            self.cards_left = False
        return self.deck.pop(0)
