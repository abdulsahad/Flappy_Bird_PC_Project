import pygame
import random
from contants import WINDOW_WIDTH, WINDOW_HEIGHT, GAP_BETWEEN_PIPES
from screen import game_screen

pygame.init()
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# The Pipe's class

class Pipe:
    def __init__(self):
        self.x = WINDOW_WIDTH
        self.height = random.randint(100, WINDOW_HEIGHT - GAP_BETWEEN_PIPES - 100) #restricting the pipe heights  
        self.top = self.height
        self.bottom = self.height + GAP_BETWEEN_PIPES
        self.velocity = 5
        self.color = (0, 255, 0)
        self.scored = False

    def drawing(self):
        pygame.draw.rect(game_screen, self.color, (self.x, 0, 50, self.top))  # Upper pipe
        pygame.draw.rect(game_screen, self.color, (self.x, self.bottom, 50, WINDOW_HEIGHT - self.bottom))  # Bottom pipe

    def update(self):
        self.x -= self.velocity