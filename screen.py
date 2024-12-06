import pygame

def game_screen(SCREEN_WIDTH, SCCREEN_HEIGHT): # Seting up the game screen with the specified width and height
    pygame.init() # Import the Pygame lib
    # Display window with defined width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCCREEN_HEIGHT)) # The dimensions are passed in a tuple to the set_mode function
    pygame.display.set_caption("Flappy Bird") # Title of the window is set to "Flappy Bird"
    return screen # The created screen object will be used further on in the game
