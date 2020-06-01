#! /usr/bin/env python3
# coding: utf-8

""" Window management and decoration module
"""

import pygame as pg

def load():
    """ Window load function
    """
    pg.init()
    pg.display.set_mode((640, 480))
    pg.display.set_caption('MacGyver-2D')
    icon()

def icon():
    """ Window icon's load function
    """
    with open('resources/MacGyver.png', 'r') as file:
        ico = pg.image.load(file)
        pg.display.set_icon(ico)

def main():
    """ Function used to call script's possibilities
    """
    load()

if __name__ == '__main__':
    main()
    pg.display.quit()
