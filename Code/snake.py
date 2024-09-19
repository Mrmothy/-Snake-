import pygame, random
from os.path import join

#Initialize Pygame
pygame.init()

#Initialize Game Window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
pygame.display.set_caption("~~Snake~~")

#Set FPS and clock 
FPS = 20
clock = pygame.time.Clock()

#Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH / 2
head_y = WINDOW_HEIGHT / 2 + 100

snake_dx = 0
snake_dy = 0

score = 0

#Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

#Set Fonts
font = pygame.font.SysFont("gabriola", 48)

#Set Text 
title_text = font.render("~~Snake~~", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH /2, WINDOW_HEIGHT / 2)

score_text = font.render(f"Score: {score}", True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

gameover_text = font.render("GAMEOVER", True, RED, DARKGREEN)
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

continue_text = font.render("Press continue to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH / 2 , WINDOW_HEIGHT / 2 + 64)

#Set Sound and Music
pick_up_sound = pygame.mixer.Sound(join("Assets", "pick_up_sound.wav"))
pick_up_sound.set_volume(.25)


#Set Images (use simple rects. just create the coordinates.)
#For a Rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord =  (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []



#Start Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Fill surface
    display_surface.fill(WHITE)

    #Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    #Display Assets
    pygame.draw.rect(display_surface, GREEN, head_coord)
    pygame.draw.rect(display_surface, RED, apple_coord)

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End Game
pygame.quit()