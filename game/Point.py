import pygame
import random
import os

import Constants


# Import necessary modules and constants for the Food class
SCREEN_WIDTH = Constants.SCREEN_WIDTH
SCREEN_HEIGHT = Constants.SCREEN_HEIGHT

POINT_SIZE = Constants.POINT_SIZE
POINT_COLOR = Constants.POINT_COLOR




'''
The Point class inherits from pygame.sprite.Sprite, 
which allows it to be used in conjunction with Pygame's sprite groups and collision detection features.

Main methods of the Point class include:
    - __init__: Initializes the point with a random position and creates a rectangle for collision detection.
    - draw: Draws the point on the screen as a rectangle filled with the specified color.
    - move_to_random_position: Moves the point to a new random position on the screen.


The class also includes methods:
    - getting the point's rect for collision detection 
    - getting the point's size 
    - getting the point's position as a tuple (x, y)

'''



class Point(pygame.sprite.Sprite):
    def __init__(self):

        '''Initializes the Point object by setting its position to a random location on the screen and creating a rectangle for collision detection.'''

        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, SCREEN_WIDTH - POINT_SIZE[0])
        self.y = random.randint(0, SCREEN_HEIGHT - POINT_SIZE[1])
        self.point_rect = pygame.Rect(self.x, self.y, *POINT_SIZE)



    def draw(self, screen):

        '''Draws the point on the screen as a rectangle filled with the specified color.'''

        point_image = pygame.Surface(POINT_SIZE)
        point_image.fill(POINT_COLOR)
        screen.blit(point_image, (self.x, self.y))



    def move_to_random_position(self):

        '''Moves the point to a new random position on the screen.'''

        self.x = random.randint(0, SCREEN_WIDTH - POINT_SIZE[0])
        self.y = random.randint(0, SCREEN_HEIGHT - POINT_SIZE[1])
        self.point_rect.topleft = (self.x, self.y)



    def get_rect(self):

        '''Returns the rectangle representing the point's position and size for collision detection.'''

        return self.point_rect



    def get_size(self):

        '''Returns the size of the point.'''

        return POINT_SIZE



    def get_position(self):

        '''Returns the current position of the point as a tuple (x, y).'''

        return (self.x, self.y)    