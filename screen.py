import pygame

def game_screen(SCREEN_WIDTH, SCCREEN_HEIGHT):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    return screen
