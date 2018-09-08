#! /usr/bin/python3
# -*- encoding: utf-8 -*-

import sys
import os
import pygame
import card

pygame.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)

card_back_img = pygame.image.load(os.path.join('images', 'card_back.png'), namehint='card_back')
card_back_rect = card_back_img.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill([0, 0, 0])
    screen.blit(card_back_img, card_back_rect)
    pygame.display.flip()
