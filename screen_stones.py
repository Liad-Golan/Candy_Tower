import pygame
from Constans import *
clock = pygame.time.Clock
from player import *
import random

class Screen_stones():
    def __init__(self):
        self.min_length = 200
        self.max_length = 700
        self.stair = pygame.image.load("image/stair.png")
        #self.rect_stair = self.stair.get_rect()


    def display_stair(self, stair_info):
        if stair_info[0] == 0:
            self.stair_x = random.randint(0, SCREEN_WIDTH_X - self.min_length)
            self.stair_length = random.randint(self.min_length, self.max_length) #length_random_generate
            need_random = False
        else:
            self.stair_length = stair_info[0]
            self.stair_x = stair_info[1]
        #print(self.rect_stair)
        stair = pygame.transform.scale(self.stair, (self.stair_length, STAIR_WIDTH))
        SCREEN.blit(stair, (self.stair_x, 650))
        return [self.stair_length, self.stair_x]

