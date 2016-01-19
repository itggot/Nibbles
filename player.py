import pygame
from pygame.locals import *
import os
import collections

class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.window_width = width
        self.window_height = height
        self.velocity = 10
        self.image = pygame.image.load(os.path.join('media', 'player.png'))
        self.directions = collections.deque([(1, 0), (0, 1), (-1, 0), (0, -1)])

    def update(self):
        key_events = pygame.event.get(KEYDOWN)
        for event in key_events:
            if event.key == K_RIGHT:
                self.directions.rotate(-1)
            elif event.key == K_LEFT:
                self.directions.rotate(1)
        self.x += self.directions[0][0] * self.velocity
        self.y += self.directions[0][1] * self.velocity
        if self.x > self.window_width or self.x < 0:
            self.x = self.window_width / 2
        if self.y > self.window_height or self.y < 0:
            self.y = self.window_height / 2



    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
