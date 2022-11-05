import os
import pygame
from parameters import *

class GameWindow:
    def __init__(self):
        self.surface = pygame.display.set_mode(WIN_SIZE)
        self.set_caption_icon()

    def set_caption_icon(self):
        image_path = os.path.join('Images', 'angry-bird-icon_32.png')
        image = pygame.image.load(image_path).convert_alpha()
        pygame.display.set_icon(image)
        pygame.display.set_caption(CAPTION)

    def paint_background(self):
        self.add_image('background.jpg', WIN_SIZE, ORIGIN)
        self.add_image('hook.png', (30, 100), (150, WIN_HEIGHT-150))
        self.add_image('wooden_block_4.png', (50, 40), (140, WIN_HEIGHT-50))
        self.add_image('wooden_block_2.png', (20, 60), (600, WIN_HEIGHT-70))
        self.add_image('wooden_block_2.png', (20, 60), (680, WIN_HEIGHT-70))
        self.add_image('wooden_block_5.png', (30, 30), (690, WIN_HEIGHT-100), 90)
        self.add_image('wooden_block_3.png', (15, 150), (580, WIN_HEIGHT-80), 90)
        self.add_image('wooden_block_3.png', (15, 150), (720, WIN_HEIGHT-155))
        self.add_image('wooden_block_3.png', (15, 150), (820, WIN_HEIGHT-155))
        self.add_image('wooden_block_3.png', (15, 150), (700, WIN_HEIGHT-165), 90)
        self.add_image('wooden_block_3.png', (20, 150), (860, WIN_HEIGHT-155))
        self.add_image('wooden_block_3.png', (20, 150), (970, WIN_HEIGHT-155))
        self.add_image('wooden_block_1.png', (15, 150), (850, WIN_HEIGHT-165), 90)
        self.add_image('wooden_block_2.png', (20, 60), (860, WIN_HEIGHT-225))
        self.add_image('wooden_block_2.png', (20, 60), (940, WIN_HEIGHT-225))
        self.add_image('wooden_block_3.png', (15, 150), (830, WIN_HEIGHT-235), 90)
        self.add_image('wooden_block_5.png', (30, 30), (930, WIN_HEIGHT-263))

    def add_image(self, image_path, scale, position, rotate=None):
        image_path = os.path.join('Images', image_path)
        image = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, scale)
        if rotate:
            image = pygame.transform.rotate(image, rotate)
        self.surface.blit(image, position)
