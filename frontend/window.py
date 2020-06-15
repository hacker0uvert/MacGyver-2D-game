#! /usr/bin/env python3
# coding: utf-8

""" Window management and decoration module
"""

import os

import pygame as pg

SCRIPT_DIR = os.path.split(os.path.abspath(__file__))[0]
RESOURCES_DIR = os.path.join(SCRIPT_DIR, 'resources')
ICON_FILE = 'MacGyver.png'

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
    i, j = 0, 0
    while j in range(15):
        while i in range(15):
            if labyrinth_matrix[j][i] == 'W':
                display.blit(surfaces['wall'], (i*40, j*40))
            else:
                display.blit(surfaces['corridor'], (i*40, j*40))
            i += 1
        j += 1
        i = 0
    pg.display.flip()
    return display

def main():
    """ Function used to call script's possibilities
    """
    load(RESOURCES_DIR, ICON_FILE)

if __name__ == '__main__':
    main()
