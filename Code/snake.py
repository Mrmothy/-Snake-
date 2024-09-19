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

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
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

    #Move the snake
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake_dx = -1 * SNAKE_SIZE
            snake_dy = 0
        if event.key == pygame.K_RIGHT:
            snake_dx = SNAKE_SIZE
            snake_dy = 0
        if event.key == pygame.K_UP:
            snake_dx = 0
            snake_dy = -1 * SNAKE_SIZE
        if event.key == pygame.K_DOWN:
            snake_dx = 0
            snake_dy = SNAKE_SIZE
# 

    #Add the head coordinate to the first index of the body coordinate list
    #This will essentially move all of the snakes body boy one position in the list.
    body_coords.insert(0, head_coord)
    body_coords.pop()
    
    #Update the x, y position of the snakes head and make a new coordinate
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    
    #Check for game over
    if head_rect.right <= 0 or head_rect.left >= WINDOW_WIDTH or head_rect.bottom <= 0 or head_rect.top >= WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(gameover_text, gameover_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Pause the game until player presses a key, then reset the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                #player wants to play again
                if event.type == pygame.KEYDOWN:
                    score = 0

                    head_x = WINDOW_WIDTH / 2
                    head_y = WINDOW_HEIGHT / 2
                    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

                    body_coords = []

                    snake_dx = 0
                    snake_dy = 0

                    is_paused = False
                #Player wants to quit.
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False


    #Check for Collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()
        
        apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)

        body_coords.append(head_coord)

    #Update HUD
    score_text =font.render(f"Score: {score}", True, GREEN, DARKRED)


    #Fill surface
    display_surface.fill(WHITE)

    #Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    #Display Assets
    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)


    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End Game
# pygame.quit()