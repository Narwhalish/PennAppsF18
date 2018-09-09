#* /usr/bin/python3
# -*- encoding: utf-8 -*-

from Player import Player
from Deck import Deck
from Card import Card

class Game:
    bottom = []
    advantage = "" #could be odd team or even team

    def __init__(self, number_of_players):
        self.number_of_players  = number_of_players
        self.players = [Player(player_number) for player_number in range(1, number_of_players + 1)]
        self.decks = [Deck() for _ in range(number_of_players // 2)]

    def deal_hands(self):
        cards_per_player = {4: 25, 6: 26, 8: 26, 10: 26}
        pile = []

        for d in self.decks:
            d.shuffle_deck()
            pile += d.get_deck()

        while True:
            for p in self.players:
                if len(p.hand) < cards_per_player[self.number_of_players]:
                    # p.add_to_hand(pile.pop(0))
                    card = pile.pop(0)
                    p.add_to_hand(card)
                    print('player ' + str(p.player_number) + ' has '+ card.rank + card.suit + ' as card # ' + str(len(p.hand)))
                    # print(str(p.hand) + '\n')
                else:
                    break

    def determine_starter_two(self):
        index = 0   #index of hand that we're checking
        place = 0   #the place in the list where Player One is found
        for person in players:
            if person.hand[index].get_rank() == '2':
                place = players.index(person)
                break
            index += 1

        player_numbers = 1    #to newly set for players
        for x in range(0,4):
            if place < 4:
                players[place].update_player_number(player_numbers)
                place, player_numbers += 1
            else:
                place = place - 4
                players[place].update_player_number(player_numbers)
                place, player_numbers += 1

    def determine_starter_normal(self):
        
        #deal cards visually and slowly
        #allow players to select a card to flip
        #should be a thing to highlight the ones that are the correct number
        pass

if __name__ == '__main__':
    root = Game(4)
    root.deal_hands()
