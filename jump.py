from main import WINDOW_HEIGHT

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