import pygame
SCREEN_WIDTH_X = 1000
SCREEN_LENGTH_Y = 750

START_GAME_X = 600
START_GAME_Y = 450
START_GAME_WIDTH = 250
START_GAME_HEIGHT = 250

SCREEN = pygame.display.set_mode((SCREEN_WIDTH_X, SCREEN_LENGTH_Y))

#בכל דמות יש קישור לשלוש תמונות כאשר הסדר שלהן הוא עומד הולך קופץ
PLAYER1_IMAGES = ['C:\Hackathon_nitzanim\Candy_Tower\image\icy_tower_stand.png', 'C:\Hackathon_nitzanim\Candy_Tower\image\icy_tower_walk.png', 'C:\Hackathon_nitzanim\Candy_Tower\image\icy_tower_jump.png']

ICY_WIDTH = 64.5
ICY_LENGTH = 96.5

icy_x = 500
icy_y = 600

WALK_SPEED = 1.3