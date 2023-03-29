import pygame
from Constans import *
clock = pygame.time.Clock
from player import *
import random

class Screen_stones():
    def __init__(self, stair_y):
        self.min_length = 200
        self.max_length = 700
        self.stair = pygame.image.load("image/stair.png")

        self.stair_y = stair_y #זמנית

    def display_stair(self, stair_info):
        if stair_info[0] == 0:
            self.stair_x = random.randint(0, SCREEN_WIDTH_X - self.min_length)
            self.stair_length = random.randint(self.min_length, self.max_length) #length_random_generate
        else:
            self.stair_length = stair_info[0]
            self.stair_x = stair_info[1]
        #print(self.rect_stair)
        stair_scale = pygame.transform.scale(self.stair, (self.stair_length, STAIR_WIDTH))
        SCREEN.blit(stair_scale, (self.stair_x, self.stair_y))

        self.rect_stair = stair_scale.get_rect()
        self.rect_stair[0] = self.stair_x
        self.rect_stair[1] = self.stair_y#self.stair_y
        pygame.draw.rect(SCREEN, (0, 0, 0), self.rect_stair, 3)

        return [self.stair_length, self.stair_x]


    def stair_movment(self):
        if self.stair_y < SCREEN_LENGTH_Y:
            self.stair_y += 0.1
        else:
            self.stair_y = -140
            return True

    def get_stair(selfself):
        return self.stair