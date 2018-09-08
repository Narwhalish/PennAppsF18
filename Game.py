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

    def __init__(self, num_players):
        self.players = [Player(x) for x in range(1, num_players + 1)]
        self.decks = [Deck() for _ in range(num_players / 2)]

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


    def determine_starter_normal():
        #deal cards visually and slowly
        #allow players to select a card to flip
        #should be a thing to highlight the ones that are the correct number

    def deal_hands(self):
        #deal to players!

if __name__ == '__main__':
    d1 = Deck()
    d1.shuffle_deck()
    d1.print_deck()
