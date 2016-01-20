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
        self.tail = []
        self.points = 1
        self.font = pygame.font.SysFont('Comic Sans', 24)
        self.score_label = self.font.render("Player 1: {0}".format(self.points - 1), 1, (255, 255, 255))

    def reset(self):
        self.score = 1
        self.tail = []
        self.x = 100
        self.y = 100

    def grow(self):
        self.points += 1
        self.tail.append((self.x, self.y))

    def turn_left(self):
        self.directions.rotate(1)

    def turn_right(self):
        self.directions.rotate(-1)

    def update(self):
        self.x += self.directions[0][0] * self.velocity
        self.y += self.directions[0][1] * self.velocity

        self.tail.append((self.x, self.y))
        if len(self.tail) > self.points:
            self.tail.pop(0)

        if self.x > self.window_width or self.x < 0:
            self.x = self.window_width / 2
        if self.y > self.window_height or self.y < 0:
            self.y = self.window_height / 2

        self.score_label = self.font.render("Player 1: {0}".format(self.points - 1), 1, (255, 255, 0))

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        for segment in self.tail:
            window.blit(self.image, (segment[0], segment[1]))
        window.blit(self.score_label, (10, 10))
