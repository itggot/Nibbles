import pygame
from pygame.locals import *
import os
import collections

class Player(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 10
        self.image = pygame.image.load(os.path.join('media', 'player.png'))
        self.directions = collections.deque([(1, 0), (0, 1), (-1, 0), (0, -1)])


    def update(self):
        key_events = filter((lambda x: x.type == KEYDOWN), pygame.event.get())
        for event in key_events:
            if event.key == K_RIGHT:
                self.directions.rotate(-1)
            elif event.key == K_LEFT:
                self.directions.rotate(1)
        self.x += self.directions[0][0] * self.velocity
        self.y += self.directions[0][1] * self.velocity


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
