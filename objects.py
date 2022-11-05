import os
import pygame
from parameters import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.active = False
        self.moving = False
        image_path = os.path.join('Images', 'angry-bird-icon_32.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, BIRD_SIZE)
        self.rect = self.image.get_rect(left=x, top=y)
        #pygame.Rect()

    def collide(self, group_name):
        self.soundfx.play()
        pygame.sprite.spritecollide(Bird, group_name, True)

    def update(self, pressed_keys, fire):
        if self.active:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
            if fire:
                self.rect.move_ip(5, 5)
                self.kill()
            #move_down_sound.play()
        elif self.moving:
            self.move()

    def move(self):
        pass

class Piggy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image_path = os.path.join('Images', 'Pig-icon_48.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, PIG_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pass

    def collide(self, group_name):
        self.soundfx.play()
        pygame.sprite.spritecollide(Piggy, group_name, True)


class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("calibri", 30)

    def update(self, screen, hit):
        if hit: self.score += 10
        text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(text, (850, 30))

