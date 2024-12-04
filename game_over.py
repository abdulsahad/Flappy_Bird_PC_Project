import pygame
import sys
from contants import WINDOW_HEIGHT, WINDOW_WIDTH, BG_COLOR
from screen import game_screen

pygame.init()
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def game_over_screen(score):
    font = pygame.font.Font(None, 72)
    game_over_surface = font.render("Game Over!", True, (255, 0, 0))
    score_surface = font.render(f"Your Score: {score}", True, (0, 0, 0))
    restart_surface = font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
    while True:    
        game_screen.fill(BG_COLOR)
        game_screen.blit(game_over_surface, (WINDOW_WIDTH // 2 - game_over_surface.get_width() // 2, 200))
        game_screen.blit(score_surface, (WINDOW_WIDTH // 2 - score_surface.get_width() // 2, 300))
        game_screen.blit(restart_surface, (WINDOW_WIDTH // 2 - restart_surface.get_width() // 2, 400))
        for event in pygame.event.get(): #This for loop helps to restart the game when the game over 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #Asking for input from Keyboard
                if event.key == pygame.K_r: #check what key is pressed
                    return  # Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()