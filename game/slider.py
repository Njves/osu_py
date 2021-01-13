import cfg
import pygame
import random

from game.CountLoader import CountLoader
from game.circle import Circle



class Slider(pygame.sprite.Sprite):

    circle_x = 20
    circle_y = 40
    def __init__(self, name,  *groups):
        super().__init__(*groups)
        self.name = "slider"

        x = random.randint(300, 1000)
        y = random.randint(1, 500)
        self.image = pygame.surface.Surface((300, 80))
        self.image.fill((255, 255, 255))
        self.image.set_alpha(100)
        self.rect = self.image.get_rect(center=(x, y))
        self.circle = pygame.draw.circle(self.image, "black", (self.circle_x, self.circle_y), 30, 3)



    def get_inner_circle(self):
        return self.circle

    def move_circle(self):

        self.image.fill((255, 255, 255))
        if self.circle_x < self.rect.width - 30:
            self.circle_x += 8
            self.circle_y += 0
            self.circle = pygame.draw.circle(self.image, "black", (self.circle_x, self.circle_y), 30, 1)

    def update(self, *args, **kwargs) -> None:
        if self.circle.collidepoint(args[0]):
            CountLoader.count += 1

