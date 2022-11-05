import os
import pygame
from objects import Block, BlockCollection
from parameters import *

class GameWindow:
    def __init__(self):
        self.surface = pygame.display.set_mode(WIN_SIZE)
        self.set_caption_icon()
        self.blocks = BlockCollection()

    def set_caption_icon(self):
        image_path = os.path.join('Images', 'angry-bird-icon_32.png')
        image = pygame.image.load(image_path).convert_alpha()
        pygame.display.set_icon(image)
        pygame.display.set_caption(CAPTION)

    def paint_background(self):
        background = Block('background.jpg', WIN_SIZE, ORIGIN)
        hook = Block('hook.png', (30, 100), (150, WIN_HEIGHT-150))
        block = Block('wooden_block_4.png', (50, 40), (140, WIN_HEIGHT-50))
        self.surface.blit(background.image, background.rect)
        self.surface.blit(hook.image, hook.rect)
        self.surface.blit(block.image, block.rect)
        self.blocks.update(self.surface)
