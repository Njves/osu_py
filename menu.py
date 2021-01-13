import pygame
from pygame.font import Font

import cfg
from game.MapStorage import MapStorage
from game.game import Game

pygame.init()


class Menu:

    def __init__(self):

        self.screen = pygame.display.set_mode(cfg.mode)

    song = None
    song1 = None
    song2 = None
    def get_song_elements(self, screen):
        width = 400
        height = 40
        divider = 50
        x = cfg.WIDTH // 2 - width // 2
        y = 50
        font = Font(None, 30)
        text_render = []

        text_render.append(font.render("yanaginagi - Haru Modoki", True, (255, 255, 255)))
        text_render.append(font.render("0", True, (255, 255, 255)))
        text_render.append(font.render("Giga-P - hibikase", True, (255, 255, 255)))
        self.song = pygame.draw.rect(screen, "red", (x, y, width, height))
        self.song1 = pygame.draw.rect(screen, "red", (x, y + divider, width, height))
        self.song2 = pygame.draw.rect(screen, "red", (x, y + divider * 2, width, height))

        x += 100
        y += 10
        for i in text_render:
            screen.blit(i, i.get_rect(topleft=(x, y)))
            y += divider

    def start_game(self, id):
        storage = MapStorage()
        Game(storage.get_map_by_id(id)).start_menu()

    def start_menu(self):
        is_running = True
        clock = pygame.time.Clock()
        font = Font(None, 30)
        image = pygame.image.load("images/menu_bck.png")
        back_rect = image.get_rect()


        while is_running:
            self.screen.fill((0, 0, 0))
            self.screen.blit(image, back_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_song = self.song.collidepoint(event.pos)
                    #is_song1 = self.song1.collidepoint(event.pos)
                    is_song2 = self.song2.collidepoint(event.pos)
                    if is_song:
                        self.start_game(cfg.sng_haru)

                    #if is_song1:
                    #    self.start_game(cfg.sng_dura)
                    if is_song2:
                        self.start_game(cfg.sng_hibikase)


            render = font.render("Выберите песню", True, (233, 103, 160))
            font_rect = render.get_rect(center=(1280 // 2, render.get_height()))
            self.screen.blit(render, font_rect)
            self.get_song_elements(self.screen)

            pygame.display.flip()
            clock.tick(cfg.FPS)

