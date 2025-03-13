import pygame
import random
import os

import Constants


# Import necessary modules and constants for the Food class
SCREEN_WIDTH = Constants.SCREEN_WIDTH
SCREEN_HEIGHT = Constants.SCREEN_HEIGHT

FOOD_SIZE = Constants.FOOD_SIZE
FOOD_COLOR = Constants.FOOD_COLOR




'''
The Food class inherits from pygame.sprite.Sprite, 
which allows it to be used in conjunction with Pygame's sprite groups and collision detection features.

Main methods of the Food class include:
    - __init__: Initializes the food with a random position and creates a rectangle for collision detection.
    - draw: Draws the food on the screen as a rectangle filled with the specified color.
    - move_to_random_position: Moves the food to a new random position on the screen.


The class also includes methods:
    - getting the food's rect for collision detection 
    - getting the food's size 
    - getting the food's position as a tuple (x, y)

'''



class Food(pygame.sprite.Sprite):
    def __init__(self):

        '''Initializes the Food object by setting its position to a random location on the screen and creating a rectangle for collision detection.'''

        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, SCREEN_WIDTH - FOOD_SIZE[0])
        self.y = random.randint(0, SCREEN_HEIGHT - FOOD_SIZE[1])
        self.food_rect = pygame.Rect(self.x, self.y, *FOOD_SIZE)



    def draw(self, screen):

        '''Draws the food item on the screen as a rectangle filled with the specified color.'''

        food_image = pygame.Surface(FOOD_SIZE)
        food_image.fill(FOOD_COLOR)
        screen.blit(food_image, (self.x, self.y))



    def move_to_random_position(self):

        '''Moves the food to a new random position on the screen.'''

        self.x = random.randint(0, SCREEN_WIDTH - FOOD_SIZE[0])
        self.y = random.randint(0, SCREEN_HEIGHT - FOOD_SIZE[1])
        self.food_rect.topleft = (self.x, self.y)



    def get_rect(self):

        '''Returns the rectangle representing the food's position and size for collision detection.'''

        return self.food_rect



    def get_size(self):

        '''Returns the size of the food item.'''

        return FOOD_SIZE



    def get_position(self):

        '''Returns the current position of the food item as a tuple (x, y).'''

        return (self.x, self.y)    