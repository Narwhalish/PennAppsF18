#* /usr/bin/python3
# -*- encoding: utf-8 -*-

class Card:
    def __init__(self, card_rank, card_suit):
        self.rank = card_rank
        self.suit = card_suit

    #possibly don't need?
    def get_value(self):
        value_cards = {'5': 5, '10': 10, 'K': 10}
        return value_cards[self.rank]
