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

        self.icy_x = icy_x
        self.icy_y = 600

        self.status = 'stand'
        self.is_jumping = False
        self.y_start = self.icy_y



    def icy_display(self):
        if self.status == 'stand':
            SCREEN.blit(self.icy_stand_scale, (self.icy_x, self.icy_y))
        elif self.status == 'jump':
            SCREEN.blit(self.icy_jump_scale, (self.icy_x, self.icy_y))
        elif self.status == 'right':
            SCREEN.blit(self.icy_walk_scale, (self.icy_x, self.icy_y+4))
        elif self.status == 'left':
            walk_left = pygame.transform.flip(self.icy_walk_scale, True, False)
            SCREEN.blit(walk_left, (self.icy_x, self.icy_y+4))

    def icy_move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.status = 'right'
            self.icy_x += WALK_SPEED
        elif keys[pygame.K_LEFT]:
            self.status = 'left'
            self.icy_x -= WALK_SPEED

        if self.icy_x > SCREEN_WIDTH_X-ICY_WIDTH:
            self.icy_x = (SCREEN_WIDTH_X - ICY_WIDTH)
        elif self.icy_x < 0:
            self.icy_x = 0

    def icy_jumping(self, jump):
        if jump:
            self.status = 'jump'
            self.is_jumping = True
            self.y_start = self.icy_y

        if self.is_jumping:
            if self.y_start-100 < self.icy_y:
                self.icy_y -= 3
            else:
                self.is_jumping = False
        elif not self.is_jumping:
            if self.icy_y + ICY_LENGTH < SCREEN_LENGTH_Y:
                self.icy_y += 3
            else:
                self.status = 'stand'
