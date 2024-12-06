import pygame
from screen import game_screen
from contants import WINDOW_WIDTH, WINDOW_HEIGHT, BG_COLOR

# importing Pygame library
pygame.init()
# Set up the game screen, width and height
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def countdown_screen():
    font = pygame.font.Font(None, 72) # Making a font with a size of 72 for the countdown numbers
    # loop until we get to three
    for i in range(1, 4, 1): # countdown starts from 1 and game starts befor hitting to 4
        game_screen.fill(BG_COLOR)# Fill the screen of the game with the background color
        countdown_surface = font.render(str(i), True, (255, 0, 0)) # Draw current countdown value as red
        # To center the countdown number on the screen, we calculate its position.
        game_screen.blit(countdown_surface, (WINDOW_WIDTH // 2 - countdown_surface.get_width() // 2, WINDOW_HEIGHT // 2 - countdown_surface.get_height() // 2))
        pygame.display.update() # Show rendered countdown number on display
        pygame.time.delay(1000)  # Delay for 1 second before showing the next countdown number
