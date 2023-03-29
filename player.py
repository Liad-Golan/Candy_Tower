import pygame
from Constans import *
clock = pygame.time.Clock


class Player():
    def __init__(self, player_photos):
        self.icy_stand = pygame.image.load(player_photos[0])
        self.icy_stand_scale = pygame.transform.scale(self.icy_stand, (64.5, 96.5))

        self.icy_walk = pygame.image.load(player_photos[1])
        self.icy_walk_scale = pygame.transform.scale(self.icy_walk, (64.5, 96.5))

        self.icy_jump = pygame.image.load(player_photos[2])
        self.icy_jump_scale = pygame.transform.scale(self.icy_jump, (64.5, 96.5))

        self.icy_x = icy_x
        self.icy_y = icy_y - ICY_LENGTH

        self.status = 'stand'
        self.is_jumping = False
        self.y_start = self.icy_y

        self.rect_icy = self.icy_stand_scale.get_rect()
        self.collision = False

        self.icy_on_stair = False


    def check_screen_stones(self, screen_stones):
        screen_stones_rect = screen_stones.rect_stair
        if self.is_jumping == False: # max height, going down
            if self.rect_icy.colliderect(screen_stones_rect):
                if self.rect_icy.bottom <= screen_stones_rect.top+5:
                    self.collision = True
                    self.stair_top = screen_stones_rect.top
                    self.icy_on_stair = True
                    # TODO: to remove
                    pygame.draw.rect(SCREEN, (255, 0, 0), self.rect_icy, 3)
                    pygame.draw.rect(SCREEN, (255, 0, 0), screen_stones_rect, 3)
                    print("icy", self.rect_icy.bottom)
                    print("stairs", screen_stones_rect.top)
                    print('collision', self.collision)
                    #self.icy_y = screen_stones_rect.top
                    #self.icy_x = 50
                else:
                    self.collision = False
            else:
                pass
                #self.collision = False
        else: #on jumping up
            #print("im up")
            pass
        """
                    self.is_jumping = False
                    Player.icy_jumping(False)
                    """


        

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

        self.rect_icy[0] = self.icy_x
        self.rect_icy[1] = self.icy_y
        pygame.draw.rect(SCREEN, (0, 0, 0), self.rect_icy, 3)


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

    def icy_jumping(self, up_key_pressed):
        if up_key_pressed:
            self.status = 'jump'
            self.is_jumping = True
            self.y_start = self.icy_y

        if self.is_jumping:
            if self.y_start-300 < self.icy_y:
                self.icy_y -= 3
                pygame.time.delay(2)
            else:
                self.is_jumping = False
                print("im down")
                print("is collision:", self.collision)
        elif self.collision == True:
            print("stand")
            self.status = 'stand'
            print("icy stairs", self.icy_y, self.stair_top)
            self.collision = False
            on_stair = True
        elif not self.is_jumping:
            if self.icy_y + ICY_LENGTH < SCREEN_LENGTH_Y and not self.icy_on_stair:
                self.icy_y += 3
                pygame.time.delay(2)
                print("is collision2:", self.collision)
            if  self.icy_on_stair:
                self.icy_y += 0.1
                print("on stair", self.icy_y)
                if self.icy_y + ICY_LENGTH == SCREEN_LENGTH_Y:
                    self.failed = True
                    self.icy_on_stair = False
            else:
                self.status = 'stand'
        #if self.icy_on_stair:
         #   self.icy_y = self.stair_top


#(self.icy_y + ICY_LENGTH < 650) and (screen_stones.stair_x< self.icy_x < screen_stones.stair_x+screen_stones.stair_length)
#self.icy_y + ICY_LENGTH < SCREEN_LENGTH_Y or self.icy_y + ICY_LENGTH < 650