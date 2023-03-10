import pygame
from Constans import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((Screen_Width_X, Screen_Length_Y))
    pygame.display.set_caption("Candy Tower")

    background = pygame.image.load("image/background.jpeg")
    background = pygame.transform.scale(background, (width_background, height_background))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background, (0, 0))
        pygame.display.flip()
    pygame.quit()


main()
