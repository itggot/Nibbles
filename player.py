import pygame
from pygame.locals import *
import os
import collections

Point = collections.namedtuple('Point', 'x y')
Direction = collections.namedtuple('Direction', 'vel_x vel_y')

class Player(object):

    def __init__(self, x, y, width, height):
        self.segments = [Point(x, y), Point(x - 10, y), Point(x - 20, y)]
        self.window_width = width
        self.window_height = height
        self.velocity = 10
        self.image = pygame.image.load(os.path.join('media', 'player.png'))
        self.directions = collections.deque([Direction(1, 0), Direction(0, 1), Direction(-1, 0), Direction(0, -1)])
        self.points = 3
        self.font = pygame.font.SysFont('Comic Sans', 24)
        self.score_label = self.font.render("Player 1: {0}".format(self.points - 1), 1, (255, 255, 255))

    @property
    def head(self):
        return self.segments[0]

    @property
    def x(self):
        return self.head.x

    @property
    def y(self):
        return self.head.y

    @property
    def vel_x(self):
        return self.directions[0].vel_x * self.velocity

    @property
    def vel_y(self):
        return self.directions[0].vel_y * self.velocity

    def reset(self):
        self.points = 1
        self.segments = [Point(200, 200)]

    def grow(self):
        self.points += 1

    def turn_left(self):
        self.directions.rotate(1)

    def turn_right(self):
        self.directions.rotate(-1)

    def is_colliding_with_wall(self):
        return self.x > self.window_width - 10 or\
           self.x < 0 or\
           self.y > self.window_height - 10 or\
           self.y < 0

    def is_colliding_with_self(self):
        if len(self.segments) > 4:
            tail = self.segments[1:]
            return self.head in tail
        return False

    def is_colliding_with_plupp(self, plupp):
        return self.x == plupp.x and self.y == plupp.y

    def update(self):
        self.segments.insert(0, Point(self.x + self.vel_x, self.y + self.vel_y))
        if len(self.segments) > self.points:
           self.segments.pop()

        self.score_label = self.font.render("Player 1: {0}".format(self.points - 1), 1, (255, 255, 0))

    def draw(self, window):
        for segment in self.segments:
            window.blit(self.image, segment)
        window.blit(self.score_label, (10, 10))
