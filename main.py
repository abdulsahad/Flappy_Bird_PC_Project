import pygame
from screen import game_screen
from bird import Bird

BIRD_WIDTH = 25
BIRD_HEIGHT = 30
BIRD_POSITION_X = 50
BIRD_POSITION_Y = 50
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BG_COLOR = (250, 250, 250)  


# Initialization
screen = game_screen(WINDOW_WIDTH, WINDOW_HEIGHT)
clock = pygame.time.Clock()

bird = Bird(BIRD_POSITION_X, BIRD_POSITION_Y, BIRD_WIDTH, BIRD_HEIGHT)
running = True
while running:
    screen.fill((BG_COLOR))  # Sky blue background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bird.drawing(screen)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
