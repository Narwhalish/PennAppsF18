class Player:
    contribution = 0
    hand = []

    def __init__(self, name, player_number):
        self.name = name
        self.player_number = player_number

    def add_to_hand(self, card):
        self.hand.append(card)

    def configure_bottom(self, bottom):
        #bottom is a list of cards
        #and then return the new list I guess
