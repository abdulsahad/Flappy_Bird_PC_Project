import pygame
import sys
from screen import game_screen
from bird import Bird
from contants import BIRD_HEIGHT, BIRD_WIDTH, BG_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH


# Initialization
screen = game_screen(WINDOW_WIDTH, WINDOW_HEIGHT)
clock = pygame.time.Clock()

def main():
    bird = Bird(200, WINDOW_HEIGHT // 2, BIRD_WIDTH, BIRD_HEIGHT) #First two is dimension on sscreen x and y components and other two are the size of bird

    while True:
        screen.fill(BG_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jumping()

        # Update bird
        bird.update() 
        bird.drawing(screen)


        # Update display
        pygame.display.update()
        clock.tick(60)

# Run the game loop
while True:
    main()
