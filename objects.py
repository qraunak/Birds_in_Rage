import os
import pygame
from parameters import *

class Bird(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        image_path = os.path.join('Images', 'angry-bird-icon_48.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, BIRD_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def locate(self):
        return self.rect.center

    def collide(self, group_name):
        self.soundfx.play()
        pygame.sprite.spritecollide(Bird, group_name, True)


class Piggy(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        image_path = os.path.join('Images', 'Pig-icon_48.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, PIG_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def locate(self):
        return self.rect.center

    def collide(self, group_name):
        self.soundfx.play()
        pygame.sprite.spritecollide(Piggy, group_name, True)
