import pygame
from Constans import *
from player import *
from my_buttons import *
from Button import *
from Screen_stones import *



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

    j = 1
    running = True
    right = True
    jump = False
    need_random = 0

    status = 'stand'
    while running:
        keys = pygame.key.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_on_start_game = start_game_button.mouse_in_button(mouse_pos)
                if mouse_on_start_game: #loop
                        j=2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                jump = True



        if j == 1:
            SCREEN.blit(start_background, (0, 0))
            SCREEN.blit(start_game, (START_GAME_X, START_GAME_Y))
            # square = pygame.Rect(0, 0,
            #                      20, 20)
            # pygame.draw.rect(screen, (0, 0, 0), square)

        elif j == 2:
            SCREEN.blit(game_background, (0, 0))
            stair = screen_stones()
            need_random = stair.display_stair(need_random)
            icy.icy_move(keys)
            icy.icy_display()
            icy.icy_jumping(jump)
            jump = False


        pygame.display.flip()
        #if keys[pygame.K_UP]:
        #    icy.icy_jump()
    pygame.quit()


main()


"""
stair = screen_stones()
stair.display_stair(True)
"""