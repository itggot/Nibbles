import pygame
import csv
import os


class Map(object):

    def __init__(self, map_id=0):
        self.image = pygame.image.load(os.path.join('media', 'player.png'))
        with open(os.path.join('maps', '{0}.csv'.format(map_id))) as map_file:
            map_reader = csv.reader(map_file, delimiter=';')
            self.map = []
            for row in map_reader:
                grillkorv = []
                for cell in row:
                    grillkorv.append(cell)
                self.map.append(grillkorv)
        print(self.map)

    def is_wall_at(self, point):
        return self.map[point[1] / 10][point[0] / 10] == "#"

    def draw(self, window):
        x = 0
        y = 0
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell == '#':
                    window.blit(self.image, (x * 10, y * 10))
