#* /usr/bin/python3
# -*- encoding: utf-8 -*-

import pygame
import os
import sys
import random
import Player, Deck, Card

class Game:

    decks = []
    bottom = []
    turn = 0
    score = [0, 0]
    def __init__(self, num_players):
        self.num_players = num_players
        self.num_decks = num_players/2

    def determine_starter_2():
        #randomly pick a player to get the bottom so that player would be number 1

    def __init__(self, number_of_decks):
        self.decks = [Deck() for _ in range(number_of_decks)]

    def end_turn(self):
        self.turn += 1

    def deal_hands(self):

if __name__ == '__main__':
    d1 = Deck()
    d1.shuffle_deck()
    d1.print_deck()
