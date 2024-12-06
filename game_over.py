import pygame
import sys
from contants import WINDOW_HEIGHT, WINDOW_WIDTH, BG_COLOR
from screen import game_screen

# Importing pygame lib
pygame.init()
# Seting up the game screen with the specified width and height
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def game_over_screen(score):
    font = pygame.font.Font(None, 72) # Making a font for rendering text
    game_over_surface = font.render("Game Over!", True, (255, 0, 0)) # Game over text is in red
    score_surface = font.render(f"Your Score: {score}", True, (0, 0, 0)) # Score text is in black
    restart_surface = font.render("Press R to Restart or Q to Quit", True, (0, 0, 0)) # instruction for restarting or quiting the game
    # infinite loop to display the game over screen
    while True:
        # Fill the screen of the game with the background color
        game_screen.fill(BG_COLOR) 
        # the Game Over text is in the center of the screen
        game_screen.blit(game_over_surface, (WINDOW_WIDTH // 2 - game_over_surface.get_width() // 2, 200))
        # Place the score text below the game over text
        game_screen.blit(score_surface, (WINDOW_WIDTH // 2 - score_surface.get_width() // 2, 300))
        # Place the restart and quit instructions below the score
        game_screen.blit(restart_surface, (WINDOW_WIDTH // 2 - restart_surface.get_width() // 2, 400))
        for event in pygame.event.get(): #This for loop helps to restart the game when the game is over 
            if event.type == pygame.QUIT: # If the user has closed the window
                pygame.quit() # Quit pygame
                sys.exit() # Exit the program
            if event.type == pygame.KEYDOWN: #Asking for input from Keyboard
                if event.key == pygame.K_r: #check what key is pressed
                    return  # Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit() # Quit pygame
                    sys.exit() # Exit the program
        
        pygame.display.update()# Update the display to show the changes made
