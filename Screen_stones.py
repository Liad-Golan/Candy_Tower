import pygame
from Constans import *
clock = pygame.time.Clock
from player import *
import random

class screen_stones():
    def __init__(self):
        self.min_length = 60
        self.max_length = 700
        rec

        self.stair = pygame.image.load("image/stair.png")


    def display_stair(self, stair_len):
        if stair_len == 0:
            stair_length = random.randint(self.min_length, self.max_length) #length_random_generate
            need_random = False
        else:
            stair_length = stair_len
        stair = pygame.transform.scale(self.stair, (stair_length, STAIR_WIDTH))
        SCREEN.blit(stair, (50, 650))
        return stair_length

