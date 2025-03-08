import pygame
import random
import os

from Constants import *

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, SCREEN_WIDTH - FOOD_SIZE[0])
        self.y = random.randint(0, SCREEN_HEIGHT - FOOD_SIZE[1])
        self.food_rect = pygame.Rect(self.x, self.y, *FOOD_SIZE) # Create a rect for the food to handle collisions

    def draw(self, screen):
        pass

    def move(self):
        pass

    def get_rect(self):
        pass
    
    def get_size(self):
        pass
    
    def get_position(self):
        pass
    

    