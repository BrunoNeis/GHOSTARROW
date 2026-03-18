#!/usr/bin/python
# -*- coding: utf-8 -*-
from pydoc_data.topics import topics
import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Menubg.png")
        self.rect = self.surf.get_rect(left = 0, top=0 )

    def run(self,):
        pygame.mixer_music.load("./asset/grimghosts.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close Window
                    quit()  # end pygame.

