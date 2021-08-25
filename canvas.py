import pygame
import constants
import character

# Names the game
pygame.display.set_caption('First game!')

# Fills the window and updates it


def draw_window(white_fighter, red_fighter):
    constants.WIN.fill(constants.BGCOLOR)
    # Use blit() when you want to draw a surface onto the screen
    # Takes in surface, and position
    constants.WIN.blit(character.white_fighter_right,
                       (white_fighter.x, white_fighter.y))
    constants.WIN.blit(character.red_fighter_left,
                       (red_fighter.x, red_fighter.y))
    pygame.display.update()
