#! /usr/bin/python3
# -*- encoding: utf-8 -*-

import pygame
pygame.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
