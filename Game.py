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
    
    def __init__(self, num_players):
        self.players = [Player(x) for x in range(1, num_players + 1)]
        self.decks = [Deck() for _ in range(num_players / 2)]

    def determine_starter_2():
        #randomly pick a player to get the bottom so that player would be number 1

    def end_turn(self):
        self.turn += 1

    def deal_hands(self):

if __name__ == '__main__':
    d1 = Deck()
    d1.shuffle_deck()
    d1.print_deck()
