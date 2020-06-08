#! /usr/bin/env python3
# coding: utf-8

""" Textures manipulation module
"""

import os

import pygame as pg

def surface_load(directory, img_file):
    """ Texture surface image loading function
    """
    with open(os.path.join(directory, img_file), 'r') as file:
        texture_surface = pg.image.load(file).convert()
    return texture_surface

def crop_surface(texture_surface, coordinates):
    """ Texture surface crop function
    """
    x_length = coordinates[2] - coordinates[0]
    y_length = coordinates[3] - coordinates[1]
    # pylint doesn't understand pg.Surface call thus returns an arguments error
    # pylint: disable-msg=too-many-function-args
    cropped_texture_surface = pg.Surface((x_length, y_length))
    # pylint: enable-msg=too-many-function-args
    cropped_texture_surface.blit(texture_surface, (0, 0), coordinates)
    return cropped_texture_surface

def main():
    """ Surfaces are printed on script self load for test purposes
    """
    # TODO : replace variables by a reference to an external file container
    directory = 'resources'
    floor_texture_coordinates = (300, 20, 339, 59)
    wall_texture_coordinates = (0, 240, 19, 259)
    floor_texture_file = 'structures.png'
    wall_texture_file = 'floor-tiles-20x20.png'
    window_resolution = (640, 480)
    pg.display.init()
    window = pg.display.set_mode(window_resolution)
    wall_texture = surface_load(directory, wall_texture_file)
    cropped_wall_texture = crop_surface(wall_texture, wall_texture_coordinates)
    floor_texture = surface_load(directory, floor_texture_file)
    cropped_floor_texture = crop_surface(floor_texture, floor_texture_coordinates)
    window.blit(cropped_wall_texture, (0, 0))
    window.blit(cropped_floor_texture, (45, 0))
    pg.display.flip()

if __name__ == '__main__':
    main()
