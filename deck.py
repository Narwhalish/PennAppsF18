class Deck:
    def __init__(self):
        cards = []
        suits = ["spades, diamonds, clubs, hearts"]
        for x in range(1, 15):
            for each in suits:
                cards.append(each, x)
