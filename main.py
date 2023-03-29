import pygame
from Constans import *
from player import *
from my_buttons import *
from Button import *
from screen_stairs import *


def main():
    pygame.init()

    pygame.display.set_caption("Candy Tower")

    game_background = pygame.image.load("image/game_background.jpeg")
    game_background = pygame.transform.scale(game_background, (SCREEN_WIDTH_X, SCREEN_LENGTH_Y))

    start_game = pygame.image.load("image/start_game.png")
    start_game = pygame.transform.scale(start_game, (START_GAME_WIDTH, START_GAME_HEIGHT))

    start_background = pygame.image.load("image/start_background.jpeg")
    start_background = pygame.transform.scale(start_background, (SCREEN_WIDTH_X, SCREEN_LENGTH_Y))

    icy = Player(PLAYER1_IMAGES)

    screenNumber = 1
    running = True
    right = True
    up_key_pressed = False
    need_random1 = [0, 0]
    need_random2 = [0, 0]
    need_random3 = [0, 0]
    need_random4 = [0, 0]

    stair1 = Screen_stones(1, 600)
    stair2 = Screen_stones(2, 450)  # גבהים 200 ו500 לא עבודים
    stair3 = Screen_stones(3, 300)  # אההההההה....!!!!!
    stair4 = Screen_stones(4, 150)
    status = 'stand'

    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_on_start_game = start_game_button.mouse_in_button(mouse_pos)
                if mouse_on_start_game:  # loop
                    screenNumber = 2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                up_key_pressed = True

        if screenNumber == 1:  # main screen
            SCREEN.blit(start_background, (0, 0))
            SCREEN.blit(start_game, (START_GAME_X, START_GAME_Y))
            # square = pygame.Rect(0, 0,
            #                      20, 20)
            # pygame.draw.rect(screen, (0, 0, 0), square)

        elif screenNumber == 2:  # game screen
            SCREEN.blit(game_background, (0, 0))
            need_random1 = stair1.display_stair(need_random1)
            need_random2 = stair2.display_stair(need_random2)
            need_random3 = stair3.display_stair(need_random3)
            need_random4 = stair4.display_stair(need_random4)
            icy.icy_move(keys)  # support move functionality
            icy.icy_display()  # figure on screen
            icy.icy_jumping(up_key_pressed)  # support jump functionality
            up_key_pressed = False
            icy.check_screen_stones(stair1)
            icy.check_screen_stones(stair2)
            icy.check_screen_stones(stair3)
            icy.check_screen_stones(stair4)

            if stair1.stair_movment():
                 need_random1 = [0, 0]
            elif stair2.stair_movment():
                need_random2 = [0, 0]
            elif stair3.stair_movment():
                need_random3 = [0, 0]
            elif stair4.stair_movment():
                need_random4 = [0, 0]

        pygame.display.flip()
        # if keys[pygame.K_UP]:
        #    icy.icy_jump()
    pygame.quit()


main()

"""
stair = screen_stones()
stair.display_stair(True)
"""
