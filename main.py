import sys
import pygame
from parameters import *
from gameWindow import GameWindow
from objects import Bird, Piggy


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():

    screen = GameWindow().surface
    bird_group = pygame.sprite.Group()
    pig_group = pygame.sprite.Group()
    clock = pygame.time.Clock()

    bird_1 = Bird(20, OBJ_BOTTOM)
    bird_2 = Bird(60, OBJ_BOTTOM)
    bird_3 = Bird(100, OBJ_BOTTOM)

    pig_1 = Piggy((610, WIN_HEIGHT-100))
    pig_2 = Piggy((760, WIN_HEIGHT-185))
    pig_3 = Piggy((900, WIN_HEIGHT-255))

    bird_group.add(bird_1)
    bird_group.add(bird_2)
    bird_group.add(bird_3)
    pig_group.add(pig_1)
    pig_group.add(pig_2)
    pig_group.add(pig_3)

    while True:
        event_handler()
        pygame.display.update()
        bird_group.draw(screen)
        pig_group.draw(screen)
        bird_group.update()
        pig_group.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
