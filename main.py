import sys
import pygame
from parameters import *
from gameWindow import GameWindow
from objects import (
    Bird, Piggy,
    ScoreBoard,
    BlockCollection)


def event_handler():
    space_pressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            space_pressed = space_pressed or True
    return space_pressed


def object_creator():
    x_pos = [20, 60, 100]
    bird_group = pygame.sprite.Group()
    for i in range(len(x_pos)):
        bird_group.add(Bird(x_pos[i], OBJ_BOTTOM))

    x_pos = [610, 760, 900]
    y_pos = [100, 185, 255]
    pig_group = pygame.sprite.Group()
    for i in range(len(x_pos)):
        pig_group.add(Piggy(x_pos[i], WIN_HEIGHT-y_pos[i]))

    return bird_group, pig_group


def main():

    screen = GameWindow()
    clock = pygame.time.Clock()
    birds, pigs = object_creator()
    scoreboard = ScoreBoard()
    bird_list = birds.sprites()
    while True:
        hit = False
        fire = event_handler()
        pressed_keys = pygame.key.get_pressed()
        screen.paint_background()
        if pygame.sprite.spritecollide(bird_list[0], pigs, True):
            hit = True
        bird_list[0].active = True
        birds.draw(screen.surface)
        birds.update(pressed_keys, fire)
        pigs.draw(screen.surface)
        pigs.update(hit)
        scoreboard.update(screen.surface, hit)
        pygame.display.update()
        clock.tick(FPS)
        bird_list = birds.sprites()
        if not bird_list or not pigs.sprites(): break


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
