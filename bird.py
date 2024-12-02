import pygame

BIRD_COLOR = (250, 0, 0)
BIRD_HEIGHT = 40
BIRD_WIDTH = 40

class Bird:
    def __init__(self, a, b, width, height):
        # Bird's position and size
        self.x = a  # Horizontal Position
        self.y = b  # Vertical Position
        self.width = width  # Width of the bird
        self.height = height  # Height of the bird
        self.c = BIRD_COLOR  # Color of the bird

    def drawing(self, screen):
        pygame.draw.rect(screen, self.c, (self.x, self.y, self.width, self.height))
