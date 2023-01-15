from random import random

import pygame
import os
import sys

# brd = board
brd = [['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
       ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
       ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
       ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
       ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___']]
history = [0, 0, 0]
who_moves = 'WHITE'

pygame.init()
pygame.font.init()
size = 648, 748
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()


def start_new_game():
    global brd
    brd = [['w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__'],
           ['bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___'],
           ['w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__', 'w___', 'bb__'],
           ['b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___'],
           ['w___', 'b___', 'w___', 'b___', 'w___', 'b___', 'w___', 'b___'],
           ['bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___'],
           ['w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__'],
           ['bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___', 'bw__', 'w___']]


start_new_game()