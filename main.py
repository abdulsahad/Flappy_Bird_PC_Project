import pygame
import sys
from screen import game_screen
from bird import Bird
from contants import BIRD_HEIGHT, BIRD_WIDTH, BG_COLOR, WINDOW_HEIGHT, WINDOW_WIDTH
from game_over import game_over_screen
from pipes_1 import Pipe
from countdown import countdown_screen


# Initialization
# Seting up the game screen with the specified width and height
screen = game_screen(WINDOW_WIDTH, WINDOW_HEIGHT)
# Set up a clock object for controlling the frame rate of the game
clock = pygame.time.Clock()

def main():
    countdown_screen()  # Show countdown before starting the game
    pipes = [Pipe()] # Make a list of pipes starting with one pipe
    # First two is dimension on sscreen x and y components and other two are the size of bird
    bird = Bird(200, WINDOW_HEIGHT // 2, BIRD_WIDTH, BIRD_HEIGHT)
    score = 0 # Initialize the score to 0
    font = pygame.font.Font(None, 36) # Creating a font object for displaying the score text

    while True:
        screen.fill(BG_COLOR) # Background Fill

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # True if user closed the window
                pygame.quit() # Quit Pygame
                sys.exit() # Program exit
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Check for key presses
                bird.jumping() # Bird jumos when space bar is pressed

        # Update bird
        bird.update() # Update the bird's position
        bird.drawing(screen) # draw the bird on the screen

        # Update and draw pipes
        for pipe in pipes:
            pipe.update() # Update the pipe's position
            pipe.drawing() # draw the pipe on the screen

            # Check for collisions between the bird and the pipe
            if (bird.x + bird.width > pipe.x and bird.x < pipe.x + 50) and \
               (bird.y < pipe.top or bird.y + bird.height > pipe.bottom):
                game_over_screen(score) # Display game over screen with score
                return  # Restart the game

            # Check if bird passes through pipe
            if not pipe.scored and bird.x > pipe.x + 50:
                score += 1 # Increment the score by 1
                pipe.scored = True # Pipe is recorded as scored

        # Add new pipes and remove off-screen pipes
        if pipes[-1].x < WINDOW_WIDTH - 300:
            pipes.append(Pipe()) # Add a new pipe
            # Remove pipes that have gone off the screen
        pipes = [pipe for pipe in pipes if pipe.x + 50 > 0]

        # Detect if the bird falls to the ground or flies above the window
        if bird.y >= WINDOW_HEIGHT - bird.height or bird.y <= 0:
            game_over_screen(score) # Display game over screen with score
            return  # Restart the game

        # Display score
        score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_surface, (10, 10)) # Draw the score in the top-left corner

        # Update display and Show all changes made
        pygame.display.update()
        clock.tick(60) # Cap the game to 60 frames per second

# Run the game loop
while True:
    main() # Call the main function
