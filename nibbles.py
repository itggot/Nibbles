import pygame
from pygame.locals import *
import sys
from player import Player
from plupp import Plupp


class Game(object):

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.player = Player(x=100, y=100, width=640, height=480)
        self.plupp =  Plupp(window_width=640, window_height=480)
        self.clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(20)
            self.update()
            self.draw()

    def update(self):
        self.player.update()

    def draw(self):
        self.window.fill((0, 0, 255))
        self.player.draw(self.window)
        self.plupp.draw(self.window)
        pygame.display.flip()

nibbles = Game()