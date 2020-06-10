#! /usr/bin/env python3
# coding: utf-8

""" Window management and decoration module
"""

import os

import pygame as pg

def load(directory='resources', icon_file='MacGyver.png', window_resolution=(600, 600)):
    """ Window loading function
    """
    pg.display.init()
    window = pg.display.set_mode(window_resolution)
    pg.display.set_caption('MacGyver-2D')
    icon(directory, icon_file)
    return window

def icon(directory='resources', icon_file='MacGyver.png'):
    """ Window icon's loading function
    """
    # TODO : replace png file by a reference to an external file container
    with open(os.path.join(directory, icon_file), 'r') as file:
        ico = pg.image.load(file)
    pg.display.set_icon(ico)

def background_init(labyrinth_matrix, display, surfaces):
    """ Walls and corridors background textures in pygame window initialisation
    """
    i = 0
    j = 0
    while j < 15:
        while i < 15:
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
    load()

if __name__ == '__main__':
    main()
