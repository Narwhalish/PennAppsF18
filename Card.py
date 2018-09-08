class Card:
    def __init__(self, card_code):
        self.rank = card_code[0]
        self.suit = card_code[1]

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    #possibly don't need?
    def get_value(self):
        value_cards = {'5': 5, '10': 10, 'K': 10}
        return value_cards[self.rank]
