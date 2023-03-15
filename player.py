import pygame
from Constans import *


class Player():
    def __init__(self, player_photos):
        self.icy_stand = pygame.image.load(player_photos[0])
        self.icy_stand_scale = pygame.transform.scale(self.icy_stand, (64.5, 96.5))

        self.icy_walk = pygame.image.load(player_photos[1])
        self.icy_walk_scale = pygame.transform.scale(self.icy_walk, (64.5, 96.5))

        self.icy_jump = pygame.image.load(player_photos[2])
        self.icy_jump_scale = pygame.transform.scale(self.icy_jump, (64.5, 96.5))

        self.icy_x = 500
        self.icy_y = 600

    def icy_display(self, status):
        if status == 'stand':
            SCREEN.blit(self.icy_stand_scale, (self.icy_x, self.icy_y))
        elif status == 'jump':
            SCREEN.blit(self.icy_jump_scale, (self.icy_x, self.icy_y))
        else:
            SCREEN.blit(self.icy_walk_scale, (self.icy_x, self.icy_y))


    def icy_jump(self):
        SCREEN.blit(self.icy_jump_scale(500, 50))
