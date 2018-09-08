#* /usr/bin/python3
# -*- encoding: utf-8 -*-

import pygame
import os
import sys
import random
import Player, Deck, Card

class Game:
    bottom = []
    turn = 0
    score = [0, 0]
    advantage = "" #could be odd team or even team

    def __init__(self, number_of_players):
        self.number_of_players  = number_of_players
        self.players = [Player(player_number) for player_number in range(1, number_of_players + 1)]
        self.decks = [Deck() for _ in range(number_of_players / 2)]

    def deal_hands(self):
        cards_per_player = {4: 25, 6: 26, 8: 26, 10: 26}
        for d in self.decks:
            while d.get_cards_left() != 0:
                for p in self.players:
                    if len(p.hand) < self.cards_per_player[self.number_of_players]:
                        p.add_to_hand(d.deal_card())

    def determine_starter_two(self):
        pass

    def determine_starter_normal(self):
        #deal cards visually and slowly
        #allow players to select a card to flip
        #should be a thing to highlight the ones that are the correct number
        pass

if __name__ == '__main__':
    root = Game(2)
    root.
