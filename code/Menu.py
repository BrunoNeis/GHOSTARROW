#!/usr/bin/python
# -*- coding: utf-8 -*-
from pydoc_data.topics import topics
from tkinter.font import Font
import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_BLACK, MENU_OPTION, COLOR_RED


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/Menubg.png")
        self.rect = self.surf.get_rect(left = 0, top=0 )

    def run(self, WIDTH=None):
        pygame.mixer_music.load("./asset/grimghosts.mp3")
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(150, text="GHOST ARROW",  text_color=(COLOR_BLACK), text_center_pos=((WIN_WIDTH/2),200))

            for i in range(len(MENU_OPTION)):
                self.menu_text(50, MENU_OPTION[i], text_color=(COLOR_RED),text_center_pos=(300 + 200 * i, 350))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close Window
                    quit()  # end pygame.

#text menu
    def menu_text(self,text_size:int, text: str, text_color: tuple , text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont(name="Blood Victim Zombie", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        pass