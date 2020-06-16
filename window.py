#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Window management and decoration module
"""

import os

import pygame as pg

def load(resources_dir, icon_file, window_resolution=(600, 600)):
    """ Window loading function
    """
    pg.display.init()
    display = pg.display.set_mode(window_resolution)
    pg.display.set_caption('MacGyver-2D')
    icon(resources_dir, icon_file)
    return display

def icon(resources_dir, icon_file):
    """ Window icon's loading function
    """
    with open(os.path.join(resources_dir, icon_file), 'r') as file:
        ico = pg.image.load(file)
    pg.display.set_icon(ico)

def background_init(labyrinth_matrix, display, surfaces):
    """ Walls and corridors background textures in pygame window initialisation
    """
    x_iterator, y_iterator = 0, 0
    while y_iterator in range(15):
        while x_iterator in range(15):
            if labyrinth_matrix[y_iterator][x_iterator] == 'W':
                display.blit(surfaces['wall'], (x_iterator*40, y_iterator*40))
            else:
                display.blit(surfaces['corridor'], (x_iterator*40, y_iterator*40))
            x_iterator += 1
        y_iterator += 1
        x_iterator = 0
    pg.display.flip()
    return display

def main():
    """ Function used to call script's possibilities
    """
        # pylint: disable-msg=import-outside-toplevel
    import settings as stg
    # pylint: enable-msg=import-outside-toplevel
    load(stg.RESOURCES_DIR, stg.ICON_FILE)

if __name__ == '__main__':
    main()
