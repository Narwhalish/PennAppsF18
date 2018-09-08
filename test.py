#* /usr/bin/python3
# -*- encoding: utf-8 -*-

import pygame
import os
import sys
import random

class Card:
    def __init__(self, card_code):
        self.rank = card_code[0]
        self.suit = card_code[1]

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def get_value(self):
        value_cards = {'5': 5, '10': 10, 'K': 10}
        return value_cards[self.rank]

class Deck:
    card_ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = ['C', 'D', 'H', 'S']

    def __init__(self):
        self.deck = [Card(rank + suit) for rank in self.card_ranks for suit in self.card_suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    #temp method
    def print_deck(self):
        print(self.deck)

class Player:
    contribution = 0
    def __init__(self, name)

class Team:
    score = 0

    def __init__(self):
        self.game_role =

class Game:
    teams

    def __init__(self):
        #anything?

    def start_game(self, number_of_decks):
        decks = [Deck() for _ in range(number_of_decks)]

    def get_scores

if __name__ == '__main__':
    d1 = Deck()
    d1.shuffle_deck()
    d1.print_deck()
