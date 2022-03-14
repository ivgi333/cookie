import pygame
from settings import *
from tiles import Tile
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('celeste clone')
runs = True
while runs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False

    screen.fill('black')
    pygame.display.flip()
    clock.tick(60)
