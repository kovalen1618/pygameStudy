import pygame
import constants
import canvas
import character


# Main function to run game


def main():
    clock = pygame.time.Clock()
    # Infinite game loop that keeps game running when it starts
    run = True
    while run:
        # Ensures the while loop never runs faster than the FPS,
        # thus making a controllable and consistent game
        clock.tick(constants.FPS)
        # Setup for loop to check for events in game
        for event in pygame.event.get():
            # Check if user quits game (exits while loop)
            if event.type == pygame.QUIT:
                run = False

            # Character movement
            keys_pressed = pygame.key.get_pressed()
            character.handle_white_movement(
                keys_pressed, character.white_fighter)
            character.handle_red_movement(keys_pressed, character.red_fighter)

            canvas.draw_window(character.white_fighter, character.red_fighter)

    # If while loop is exited, game closes
    pygame.quit()


# Makes sure the main() function runs only
# if the main.py file is ran directly
if __name__ == "__main__":  # __name__ is name of the file (__main__)
    main()
