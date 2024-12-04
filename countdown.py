import pygame
from screen import game_screen
from contants import WINDOW_WIDTH, WINDOW_HEIGHT, BG_COLOR

pygame.init()
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def countdown_screen():
    font = pygame.font.Font(None, 72)
    for i in range(1, 4, 1): # countdown starts from 1 and game starts befor hitting to 4
        game_screen.fill(BG_COLOR)
        countdown_surface = font.render(str(i), True, (255, 0, 0))
        game_screen.blit(countdown_surface, (WINDOW_WIDTH // 2 - countdown_surface.get_width() // 2, WINDOW_HEIGHT // 2 - countdown_surface.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(1000)  # Delay for 1 second
