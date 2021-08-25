import pygame
import os  # Operating System needed to define file paths
import constants

# These images in pygame are technically known as 'surfaces'
white_figther_right_image = pygame.image.load(
    os.path.join('Assets/Sprites', 'RWhiteFighter.png'))
white_fighter_right = pygame.transform.scale(
    white_figther_right_image, (constants.FIGHTER_WIDTH, constants.FIGHTER_HEIGHT))  # Resize images
red_fighter_left_image = pygame.image.load(
    os.path.join('Assets/Sprites', 'LRedFighter.png'))
red_fighter_left = pygame.transform.scale(
    red_fighter_left_image, (constants.FIGHTER_WIDTH, constants.FIGHTER_HEIGHT))

white_fighter = pygame.Rect(
    250, 200, constants.FIGHTER_WIDTH, constants.FIGHTER_HEIGHT)
red_fighter = pygame.Rect(
    550, 200, constants.FIGHTER_WIDTH, constants.FIGHTER_HEIGHT)


def handle_white_movement(keys_pressed, white_fighter):
    # Movement for White Fighter
    if keys_pressed[pygame.K_a]:  # LEFT
        white_fighter.x -= constants.VEL
    if keys_pressed[pygame.K_d]:  # RIGHT
        white_fighter.x += constants.VEL


def handle_red_movement(keys_pressed, red_fighter):
    # Movement for Red Fighter
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        red_fighter.x -= constants.VEL
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        red_fighter.x += constants.VEL
