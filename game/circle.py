import pygame
import random


from pygame.font import Font

from game.CountLoader import CountLoader


class Circle(pygame.sprite.Sprite):

    is_clicked = False
    def __init__(self, id, clap, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("images/circle.bmp").convert()
        self.image.set_colorkey((255, 255, 255))
        self.is_clicked = False
        font = Font(None, 70)
        text = font.render(f"{id}", 1, (0, 0, 0))
        self.name = "circle"
        x = random.randint(1, 1000)
        y = random.randint(1, 500)
        self.rect = self.image.get_rect(center=(x, y))
        self.sound = pygame.mixer.Sound(clap)
        self.sound.set_volume(50)


        self.image.blit(text, (80 // 2 - text.get_width() // 2, 80 // 2 - text.get_height() // 2))
        self.id = id




    def update(self, *args, **kwargs) -> None:
        if self.rect.collidepoint(args[0]):
            if not self.is_clicked:
                self.sound.play()
                self.is_clicked = True
                CountLoader.count += 1
                self.kill()
    def kill(self) -> None:
        if not self.is_clicked:
            CountLoader.count = 0
        super().kill()

