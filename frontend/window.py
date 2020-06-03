#! /usr/bin/env python3
# coding: utf-8

""" Window management and decoration module
"""

import os

import pygame as pg

def load(window_resolution=(640, 480)):
    """ Window loading function
    """
    pg.display.init()
    pg.display.set_mode(window_resolution)
    pg.display.set_caption('MacGyver-2D')
    icon()

def icon(directory='resources', icon_file='MacGyver.png'):
    """ Window icon's loading function
    """
    # TODO : replace png file by a reference to an external file container
    with open(os.path.join(directory, icon_file), 'r') as file:
        ico = pg.image.load(file)
    pg.display.set_icon(ico)

def main():
    """ Function used to call script's possibilities
    """
    load()

if __name__ == '__main__':
    main()
