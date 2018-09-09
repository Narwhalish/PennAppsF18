class Player:
    hand = []

    def __init__(self, player_number):
        self.player_number = player_number

    def update_player_number(self, player_number):
        self.player_number = player_number

    def find_power_cards(self, trump_val):
        power_card_indices = [i for i, card in enumerate(self.hand) if card.rank == trump_val]
        self.power_cards = dict(zip(power_card_indices, [self.hand[i].rank + self.hand[i].suit for i in power_card_indices]))

    def add_to_hand(self, card):
        self.hand.append(card)

    def configure_bottom(self, bottom):
        #bottom is a list of cards
        #and then return the new list I guess
        pass
