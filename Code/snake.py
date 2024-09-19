import pygame, random
from os.path import join

#Initialize Pygame
pygame.init()

#Initialize Game Window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
pygame.display.set_caption("Snake")

#Start Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



#End Game
pygame.quit()