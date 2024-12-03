import pygame

WINDOW_HEIGHT = 600
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
        self.velocity = 0  # The current vertical velocity
        self.gravity = 0.5  # Pulling the bird down due to gravity force
        self.jumping_strength = -7  # The force applied when the bird jumps

    def drawing(self, screen):
        pygame.draw.rect(screen, self.c, (self.x, self.y, self.width, self.height))

    def jumping(self):
        # Trigger the bird to jump by applying an upward velocity
        self.velocity = self.jumping_strength

    def update(self):
        self.velocity += self.gravity  # Apply gravity
        self.y += self.velocity  # Update the bird's vertical position

        # Prevent the bird from moving out of boundries
        if self.y <= 0:  
            self.y = 0
            self.velocity = 0
        elif self.y >= WINDOW_HEIGHT - self.height:  # Keep the bird within the screen
            self.y = WINDOW_HEIGHT - self.height
            self.velocity = 0
