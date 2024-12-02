import pygame
from screen import game_screen
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BG_COLOR = (135, 206, 235)  # Sky blue background color
# Initialization
screen = game_screen(WINDOW_WIDTH, WINDOW_HEIGHT)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((BG_COLOR))  # Sky blue background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
