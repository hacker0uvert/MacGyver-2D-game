#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Frontend package: window management module.
"""

import os

import pygame as pg

from backend import labyrinth as bckd
from resources import settings as stg

LABYRINTH = bckd.Labyrinth()
BX_PX_LN = LABYRINTH.box_px_len
CLOCK = pg.time.Clock()

class Window:
    """ Physical window management
    """

    def __init__(self):
        """ Window class initiator
        set_mode needs a pygame display init. Pylint raises a "defined outside __init__" warning
        if self.screen is initialised from Window.load()
        """
        self.screen = None

    def load(self):
        """ Window loading method
        """
        pg.display.init()
        self.screen = pg.display.set_mode(stg.WINDOW_RESOLUTION)
        pg.display.set_caption(stg.WINDOW_CAPTION)
        Window.icon()

    @classmethod
    def icon(cls):
        """ Window icon's loading method
        """
        with open(os.path.join(stg.SCRIPT_DIR, stg.ICON_FILE), 'r') as file:
            ico = pg.image.load(file)
        pg.display.set_icon(ico)

    def background_init(self, surfaces):
        """ Walls and corridors background textures initialisation.
        In the json file, 'wall' is corresponding to 'W' in the labyrinth_matrix.
        'c' stands for 'corridor'
        'i' for 'items_counter'
        """
        x_itr, y_itr = 0, 0
        while y_itr in range(LABYRINTH.grid_len):
            while x_itr in range(LABYRINTH.grid_len):
                if LABYRINTH.labyrinth_matrix[y_itr][x_itr] == 'W':
                    self.screen.blit(surfaces['wall'], (x_itr*BX_PX_LN, y_itr*BX_PX_LN))
                elif LABYRINTH.labyrinth_matrix[y_itr][x_itr] == 'c':
                    self.screen.blit(surfaces['corridor'], (x_itr*BX_PX_LN, y_itr*BX_PX_LN))
                    # corridors coordinates list generation
                    LABYRINTH.corridors_coordinates.append((x_itr, y_itr))
                elif LABYRINTH.labyrinth_matrix[y_itr][x_itr] == 'i':
                    self.screen.blit(surfaces['counter'], (x_itr*BX_PX_LN, y_itr*BX_PX_LN))
                    # counter coordinates list generation
                    LABYRINTH.counters_coordinates.append((x_itr, y_itr))
                x_itr += 1
            y_itr += 1
            x_itr = 0
        pg.display.flip()
        # drop_point and exit_point coordinates tuples remove from LABYRINTH.corridors_coordinates
        # so MovingObject.random_coordinates() won't use those coordinates
        LABYRINTH.corridors_coordinates.remove(LABYRINTH.drop_point)
        LABYRINTH.corridors_coordinates.remove(LABYRINTH.exit_point)

    def print_end_message(self, exit_status):
        """ Method used to define and print won message onscreen.
        """
        pg.font.init()
        # font size is proportionate to display's horizontal resolution
        font = pg.font.Font(None, stg.FONT_SIZE)
        if exit_status == 'won':
            font_surface = font.render(stg.WON_MESSAGE, True, stg.WON_MESSAGE_COLOR)
        elif exit_status == 'lose':
            font_surface = font.render(stg.DEAD_MESSAGE, True, stg.DEAD_MESSAGE_COLOR)
        font_rect = font_surface.get_rect(center=(stg.RESOLUTION/2, stg.RESOLUTION/2))
        self.screen.blit(font_surface, font_rect)
        pg.display.update()
        # wait for three seconds before closing display
        CLOCK.tick(0.3)
        on_air = False
        return on_air
