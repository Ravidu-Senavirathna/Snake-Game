import pygame
import random
import os

import Constants


''' 
Initialize the player's starting position to the center of the screen. 
The player will be represented as a rectangle with a specific size defined in Constants.py. 
The starting position is calculated to ensure that the player is centered on the screen when the game starts.
'''

STARTING_POSITION_X = (Constants.SCREEN_WIDTH // 2) - (Constants.PLAYER_SIZE[0] // 2)
STARTING_POSITION_Y = (Constants.SCREEN_HEIGHT // 2) - (Constants.PLAYER_SIZE[1] // 2)

PLAYER_COLOR = Constants.PLAYER_COLOR
PLAYER_SIZE = Constants.PLAYER_SIZE





'''
The Player class represents the player character in the game. 
It is responsible for handling the player's position, movement, and drawing the player on the screen. 
The player is represented as a simple rectangle for now, but this can be replaced with an image or sprite later on. 

The class also includes methods: 
    - getting the player's rect for collision detection and boundary checking 
    - getting and setting the player's position.  

    
    The Player class inherits from pygame.sprite.Sprite, 
    which allows it to be used in conjunction with Pygame's sprite groups and collision detection features.

'''


class Player(pygame.sprite.Sprite):
    def __init__(self):

        ''' Initialize the player with a starting position and create a rect for collision detection '''

        pygame.sprite.Sprite.__init__(self)
        self.x = STARTING_POSITION_X
        self.y = STARTING_POSITION_Y
        self.player_rect = pygame.Rect(self.x, self.y, *PLAYER_SIZE)



    def draw(self, screen):

        ''' Draw the player on the screen. The player is represented as a simple rectangle for now, 
        but this can be replaced with an image or sprite later on '''

        player_image = pygame.Surface(PLAYER_SIZE)
        player_image.fill(PLAYER_COLOR)
        screen.blit(player_image, (self.x, self.y))
 


    def move(self, dx, dy):

        ''' Move the player by a certain amount in the x and y directions 
            and update the player's rect position accordingly '''

        self.x += dx
        self.y += dy
        self.player_rect.topleft = (self.x, self.y)



    def get_rect(self):

        ''' Get the player's rect for collision detection and boundary checking '''

        return self.player_rect



    def get_position(self):

        ''' Get the player's current position as a tuple (x, y) '''

        return self.x, self.y



    def set_position(self, x, y):

        ''' Set the player's position to a specific (x, y) coordinate 
        and update the player's rect position accordingly '''

        self.x = x
        self.y = y
        self.player_rect.topleft = (self.x, self.y)