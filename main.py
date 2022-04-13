import pygame
from settings import *
from level import Level
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
pygame.display.set_caption('celeste clone')
runs = True
image = pygame.image.load('./graphics/869.jpg')
while runs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False

    screen.blit(image,(0,0))
    level.run()

    pygame.display.flip()
    clock.tick(60)
