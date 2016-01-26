import pygame
from pygame.locals import *
import events

class CollisionHandler(object):

    @classmethod
    def handle_plupp_collisions(self, player, plupp):
        if player.is_colliding_with_plupp(plupp):
            event = pygame.event.Event(events.PLUPPEATEN)
            pygame.event.post(event)

    @classmethod
    def handle_player_collisions(self, player):
        if player.is_colliding_with_self() or player.is_colliding_with_wall():
            event = pygame.event.Event(events.PLAYERDIED)
            pygame.event.post(event)
