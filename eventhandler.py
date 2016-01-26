import pygame
from pygame.locals import *
import sys
import events

class EventHandler(object):

    @classmethod
    def handle_events(self, player, plupp):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.turn_left()
                elif event.key == K_RIGHT:
                    player.turn_right()
                elif event.key == K_ESCAPE:
                    quit()
                    sys.exit()
            elif event.type == events.PLUPPEATEN:
                plupp.respawn()
                player.grow()
            elif event.type == events.PLAYERDIED:
                player.reset()
