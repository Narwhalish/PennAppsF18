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

    def __init__(self, number_of_players):
        self.players = [Player(player_number) for player_number in range(1, number_of_players + 1)]
        self.decks = [Deck() for _ in range(number_of_players / 2)]

    def deal_hands(self):
        for p in self.players:
            if self.decks[0].cards_left:
                p.add_to_hand(self.decks[0].deal_card())
            else self.decks[1].cards_left:
                p.add_to_hand(self.decks[1].deal_card())

    def determine_starter(self):
        

    def end_turn(self):
        self.turn += 1

if __name__ == '__main__':
    d1 = Deck()
    d1.shuffle_deck()
    d1.print_deck()
