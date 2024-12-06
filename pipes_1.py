import pygame
import random
from contants import WINDOW_WIDTH, WINDOW_HEIGHT, GAP_BETWEEN_PIPES
from screen import game_screen

# Importing pygame
pygame.init()
# Seting up the game screen with the specified width and height
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# The Pipe's class
# Create the pipe class to manage all the pipe objects in the game
class Pipe:
    def __init__(self):
        self.x = WINDOW_WIDTH # Set pipe start position at edge of screen to the right
        self.height = random.randint(100, WINDOW_HEIGHT - GAP_BETWEEN_PIPES - 100) # Randomising and restricting the pipe's heights 
        self.top = self.height # Define the top and bottom positions of the pipe
        self.bottom = self.height + GAP_BETWEEN_PIPES 
        self.velocity = 5 # Set the velocity at which the pipe moves left across the screen
        self.color = (0, 255, 0) # Color of the pipe (green)
        self.scored = False # To indicate if the pipe has been scored
    
    # Method to draw the pipe on the game screen
    def drawing(self):
        pygame.draw.rect(game_screen, self.color, (self.x, 0, 50, self.top))  # Upper pipe
        pygame.draw.rect(game_screen, self.color, (self.x, self.bottom, 50, WINDOW_HEIGHT - self.bottom))  # Bottom pipe

    def update(self): # update the pipe's position
        
        self.x -= self.velocity # Move the pipe to the left by its velocity
