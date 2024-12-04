import pygame
import sys
from screen import game_screen
from bird import Bird
from contants import BIRD_HEIGHT, BIRD_WIDTH, BG_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH
from game_over import game_over_screen
from pipes_1 import Pipe


# Initialization
screen = game_screen(WINDOW_WIDTH, WINDOW_HEIGHT)
clock = pygame.time.Clock()

def main():
    pipes = [Pipe()]
    bird = Bird(200, WINDOW_HEIGHT // 2, BIRD_WIDTH, BIRD_HEIGHT) #First two is dimension on sscreen x and y components and other two are the size of bird
    score = 0
    font = pygame.font.Font(None, 36)

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

        # Update and draw pipes
        for pipe in pipes:
            pipe.update()
            pipe.drawing()

            # Check for collisions
            if (bird.x + bird.width > pipe.x and bird.x < pipe.x + 50) and \
               (bird.y < pipe.top or bird.y + bird.height > pipe.bottom):
                game_over_screen(score)
                return  # Restart the game

            # Check if bird passes through pipe
            if not pipe.scored and bird.x > pipe.x + 50:
                score += 1
                pipe.scored = True

        # Add new pipes and remove off-screen pipes
        if pipes[-1].x < WINDOW_WIDTH - 300:
            pipes.append(Pipe())
        pipes = [pipe for pipe in pipes if pipe.x + 50 > 0]

        # Check if bird hits the ground
        if bird.y >= WINDOW_HEIGHT - bird.height or bird.y <= 0:
            game_over_screen(score)
            return  # Restart the game

        # Display score
        score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_surface, (10, 10))

        # Update display
        pygame.display.update()
        clock.tick(60)

# Run the game loop
while True:
    main()
