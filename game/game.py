import random

import pygame
from pygame.font import Font

from cfg import FPS
from cfg import mode
from game.CountLoader import CountLoader
from game.circle import Circle
from game.Map import Map
from game.slider import Slider
import time
pygame.init()



class Game:
    sound = pygame.mixer.Sound("songs/modoki/soft-hitwhistle.wav")

    def __init__(self, map: Map):
        self.screen = pygame.display.set_mode((1280, 720))
        self.map = map

        pygame.mixer.music.load(map.song)
        self.back_song_time = pygame.mixer.Sound(map.song).get_length()

        self.image = pygame.image.load(map.background)
        self.bpm = map.bpm
        self.pace = map.pace

    def show_circle(self, circle):
        for i in range(256 * 4):
            circle.image.set_alpha(i / 4)

    count = 0
    is_slider_move = False
    group = pygame.sprite.Group()
    interval = 4
    global_count = 0
    is_circle = True
    circle_time = 0
    def generate_object(self, is_not_active):
        self.count += 1

        circle = Circle(self.count, self.map.clap, self.group)
        #pygame.mouse.set_pos(circle.rect.x + 40, circle.rect.y + 40)
        circle.image.set_alpha(0)
        self.show_circle(circle)
        self.circle_time = time.time() * 1000
        self.interval = self.interval_listener()

    is_push = False
    def interval_listener(self):
        current_time = time.time() * 1000
        interval = 4

        for i in self.pace:
            current_time = current_time - self.circle_time
            print(f"current time {current_time}")
            if current_time - 1 < i[0] < current_time + 1:
                self.interval = i[1]
        return interval

    def show_mark(self, text):
        render = self.font.render(text, True, "red")

        self.screen.blit(render, render.get_rect(center=(mode[0] // 2, 40)))

    def start_menu(self):
        time_start = time.time()
        pygame.mixer.music.play()
        # 174
        pygame.time.set_timer(pygame.USEREVENT + 1, self.bpm )
        # Делаем бэк прозрачнее
        self.image.set_alpha(170)
        self.font = Font(None, 40)
        is_running = True

        clock = pygame.time.Clock()
        pygame.time.wait(15)

        while is_running:
            self.screen.fill((0, 0, 0))
            alpha = 255
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    is_running = False
                    exit()
                if event.type == pygame.USEREVENT + 1:
                    cur_time = (time.time() - time_start)
                    #self.interval_listener()
                    if int(cur_time) >= self.back_song_time:
                        exit()
                    if self.interval > 0:
                        self.interval -= 1
                    if self.interval == self.interval // 2:
                        pass
                    if self.interval == 0:
                        self.generate_object(True)
                        
                        if len(self.group.sprites()) > 2:
                            sprite = self.group.sprites()[0]
                            if not sprite.is_clicked:
                                CountLoader.count = 0
                            self.group.remove(sprite)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_time = time.time()
                    print(self.circle_time, click_time)
                    self.is_push = True
                    self.group.update(event.pos)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.is_push = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.interval += 1

                    if event.key == pygame.K_DOWN:
                        self.interval -= 1

                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == pygame.K_z:
                        click_time = time.time() * 1000
                        dm_time = click_time - self.circle_time
                        print(dm_time)
                        print(self.bpm * self.interval)
                        if self.bpm * self.interval > dm_time > 0:
                            self.show_mark("Классно")
                        self.group.update(pygame.mouse.get_pos())
                    if event.key == pygame.K_x:
                        self.group.update(pygame.mouse.get_pos())


            self.screen.blit(self.image, self.image.get_rect())
            self.group.draw(self.screen)
            for i in self.group.sprites():
                if i.name == "slider":
                    i.move_circle()
            text = self.font.render(f"Count: {CountLoader.count}", True, "black")
            self.screen.blit(text, text.get_rect(bottomleft=(0, 600)))
            pygame.display.flip()
            clock.tick(FPS)
