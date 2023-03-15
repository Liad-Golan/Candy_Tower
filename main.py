import pygame
from Constans import *
from player import *
from my_buttons import *
from Button import *


def main():
    pygame.init()


    pygame.display.set_caption("Candy Tower")

    background = pygame.image.load("image/background.jpeg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH_X, SCREEN_LENGTH_Y))

    start_game = pygame.image.load("image/start_game.png")
    start_game = pygame.transform.scale(start_game, (START_GAME_WIDTH, START_GAME_HEIGHT))

    background1 = pygame.image.load("image/background1.jpeg")
    background1 = pygame.transform.scale(background1, (SCREEN_WIDTH_X, SCREEN_LENGTH_Y))

    icy = Player(PLAYER1_IMAGES)

    j = 1
    running = True
    while running:
        keys = pygame.key.get_pressed()
        if j == 1:
            SCREEN.blit(background1, (0, 0))
            SCREEN.blit(start_game, (START_GAME_X, START_GAME_Y))

            # square = pygame.Rect(0, 0,
            #                      20, 20)
            # pygame.draw.rect(screen, (0, 0, 0), square)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_on_start_game = start_game_button.mouse_in_button(mouse_pos)
                if mouse_on_start_game:
                    print(mouse_pos)
                    j += 1
                    SCREEN.blit(background, (0, 0))
                    icy.icy_display('stand')
        pygame.display.flip()
        #if keys[pygame.K_UP]:
        #    icy.icy_jump()
    pygame.quit()


main()

