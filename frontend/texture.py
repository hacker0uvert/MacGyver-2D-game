#! /usr/bin/env python3
# coding: utf-8

""" Textures manipulation module
"""

import os
import json

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
    # creation of a new Surface with the cropped texture's horizontal and vertical dimensions
    cropped_texture_surface = pg.Surface((x_length, y_length))
    # pylint: enable-msg=too-many-function-args
    # adding the cropped texture to the newly created Surface
    cropped_texture_surface.blit(texture_surface, (0, 0), coordinates)
    # converting the Surface to a 40*40 pixels rectangle, so as to correspond
    # to window's 600*600 pixels definition: 15*15 texture rectangles matrix
    cropped_texture_surface = pg.transform.scale(cropped_texture_surface, (40, 40))
    return cropped_texture_surface

def get_surface(directory, img_file, coordinates):
    """ Texture surface image file load and crop
    """
    texture_surface = surface_load(directory, img_file)
    cropped_texture_surface = crop_surface(texture_surface, coordinates)
    return cropped_texture_surface

def load_surfaces_json(directory='.', surfaces_file='surfaces.json'):
    """ Surfaces dictionnary loading function, from json file
    """
    with open(os.path.join(directory, surfaces_file), 'r') as file:
        surfaces_json = json.load(file)
    return surfaces_json

def surfaces_dict(surface_json_directory='.', resources_directory='resources'):
    """ Surfaces dictionnary definition function.
    Values are defined from surfaces_json dict.
    """
    surfaces_json = load_surfaces_json(surface_json_directory)
    surfaces = {}
    for i in surfaces_json:
        surface = get_surface(resources_directory, surfaces_json[i][0], surfaces_json[i][1])
        surfaces[i] = surface
    return surfaces

def main():
    """ Surfaces are printed on script self load for test purposes
    """
    # disabling pylint message, as window module is only needed for tests
    # pylint: disable-msg=import-outside-toplevel
    import window as wdw
    # pylint: enable-msg=import-outside-toplevel
    window = wdw.load()
    surfaces = surfaces_dict()
    i = 0
    while i < len(surfaces):
        window.blit(surfaces[list(surfaces.keys())[i]], (i*40, 0))
        i += 1
    pg.display.flip()

if __name__ == '__main__':
    main()
