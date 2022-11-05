import sys
import pygame
from parameters import *
from gameWindow import GameWindow
from objects import Bird, Piggy

def event_handler():
    for event in pygame.event.get ( ) :
        if event.type == pygame.QUIT :
            pygame.quit ( )
            sys.exit ( )

def main():

    screen = GameWindow().surface
    bird_group = pygame.sprite.Group()
    pig_group = pygame.sprite.Group()
    clock = pygame.time.Clock()

    bird_1 = Bird((0, 10))
    bird_2 = Bird((100, 10))
    bird_3 = Bird((200, 10))

    pig = Piggy((50, 50))

    bird_group.add(bird_1)
    bird_group.add(bird_2)
    bird_group.add(bird_3)
    pig_group.add(pig)

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