import sys
import os
import random
import pygame

import Constants



'''Draws a grid on the given surface using the specified box size from Constants.
This function is used to visually divide the game screen into a grid, which can help with movement and collision detection.'''

def draw_grid(surface, 
              box_size=Constants.BOX_SIZE, 
              color=Constants.GRAY, 
              width= Constants.SCREEN_WIDTH, 
              height=Constants.SCREEN_HEIGHT
              ):
    
    for x in range(0, width, box_size):
        pygame.draw.line(surface, color, (x, 0), (x, height))
    for y in range(0, height, box_size):
        pygame.draw.line(surface, color, (0, y), (width, y))



'''Renders the given text using the specified font and color. This function is a simple wrapper around Pygame's font rendering capabilities.'''

def render_text(text, font, color):
    return font.render(text, True, color)

