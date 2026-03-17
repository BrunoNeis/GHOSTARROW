#!/usr/bin/python
# -*- coding: utf-8 -*-
from importlib.metadata import pass_none

import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
       # self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))


    def run(self):
        while True:
           menu = Menu(self.window)
           menu.run()
           pass
           #  check for all evesnts
            #   for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # close Window
            #        quit()  # end pygame.