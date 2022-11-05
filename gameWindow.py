import os
import pygame
from parameters import *

class GameWindow:
    def __init__(self):
        self.surface = pygame.display.set_mode(WIN_SIZE)
        image_path = os.path.join('Images', 'background.jpg')
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, WIN_SIZE)
        self.surface.blit(self.image, ORIGIN)
        pygame.display.set_caption(CAPTION)

