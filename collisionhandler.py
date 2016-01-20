import pygame
from pygame.locals import *

class CollisionHandler(object):

    @classmethod
    def handle_plupp_collisions(self, player, plupp):
        if player.x == plupp.x and player.y == plupp.y:
            event = pygame.event.Event(USEREVENT + 1) #PLUPPGET
            pygame.event.post(event)


    @classmethod
    def handle_player_collisions(self, player):
        for segment in player.tail:
            if player.x == segment[] and player.y == segment[1]:
                event = pygame.event.Event(USEREVENT + 2) #PLAYERDIE
                pygame.event.post(event)

