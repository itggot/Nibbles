import pygame
from pygame.locals import *
import sys
from player import Player
from plupp import Plupp
from map import Map
from eventhandler import EventHandler
from collisionhandler import CollisionHandler

class Game(object):

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.player = Player(x=100, y=100, width=640, height=480)
        self.plupp = Plupp(window_width=640, window_height=480)
        self.clock = pygame.time.Clock()
        self.map = Map()

        while True:
            CollisionHandler.handle_plupp_collisions(player=self.player, plupp=self.plupp)
            CollisionHandler.handle_player_collisions(player=self.player, map=self.map)

            EventHandler.handle_events(player=self.player, plupp=self.plupp)
            self.clock.tick(15)
            self.update()
            self.draw()

    def update(self):
        self.player.update()

    def draw(self):
        self.window.fill((0, 0, 255))
        self.player.draw(self.window)
        self.plupp.draw(self.window)
        self.map.draw(self.window)
        pygame.display.flip()

nibbles = Game()