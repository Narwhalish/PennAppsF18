#* /usr/bin/python3
# -*- encoding: utf-8 -*-

import pygame
import os
import sys
import random
import Player, Deck, Card

class Game:
    bottom = []
    advantage = "" #could be odd team or even team

    def __init__(self, number_of_players):
        self.number_of_players  = number_of_players
        self.players = [Player(player_number) for player_number in range(1, number_of_players + 1)]
        self.decks = [Deck() for _ in range(number_of_players / 2)]

    def deal_hands(self):
        cards_per_player = {4: 25, 6: 26, 8: 26, 10: 26}
        pile = []

        for d in self.decks:
            pile += d.get_deck()

        while True:
            for p in self.players:
                if len(p.hand) < cards_per_player[self.number_of_players]:
                    p.add_to_hand(pile.pop(0))
                else:
                    break

    def determine_starter_two(self):
        

    def determine_starter_normal(self):
        #deal cards visually and slowly
        #allow players to select a card to flip
        #should be a thing to highlight the ones that are the correct number
        pass

    def deal_hands(self):
        #deal to players!

if __name__ == '__main__':
    root = Game(2)
    root.
