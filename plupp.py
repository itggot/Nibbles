import pygame
from pygame.locals import *
import os
import random

class Plupp(object):

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.x = random.randint(0, (self.window_width - 10) / 10) * 10
        self.y = random.randint(0, (self.window_height - 10) / 10) * 10
        self.image = pygame.image.load(os.path.join('media', 'plupp.png'))

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
