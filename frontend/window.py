#! /usr/bin/env python3
# coding: utf-8

""" Window management and decoration module
"""

import os

import pygame as pg

def load():
    """ Window loading function
    """
    pg.display.init()
    pg.display.set_mode((640, 480))
    pg.display.set_caption('MacGyver-2D')
    icon()

def icon():
    """ Window icon's loading function
    """
    # TODO : replace png file by a reference to an external file container
    directory = 'resources'
    icon_file = 'MacGyver.png'
    foldername = os.path.basename(os.getcwd())
    if foldername != 'frontend':
        directory = str('frontend/'+directory)
    with open(os.path.join(directory, icon_file), 'r') as file:
        ico = pg.image.load(file)
        pg.display.set_icon(ico)

def main():
    """ Function used to call script's possibilities
    """
    load()

if __name__ == '__main__':
    main()
