#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Frontend package textures manipulation module.
"""

import os

import pygame as pg

import settings as stg
import backend as bckd

LABYRINTH = bckd.Labyrinth()
BX_PX_LN = LABYRINTH.box_px_len

class Texture:
    """ Textures manipulation
    """

    def __init__(self):
        """ Class initiator
        """

    def surface_load(self, img_file):
        """ Texture surface image loading function
        """
        with open(os.path.join(stg.RESOURCES_DIR, img_file), 'r') as file:
            texture_surface = pg.image.load(file).convert_alpha()
        return texture_surface

    def crop_surface(self, texture_surface, coordinates):
        """ Texture surface crop function
        """
        x_length = coordinates[2] - coordinates[0]
        y_length = coordinates[3] - coordinates[1]
        # creation of a new Surface with the cropped texture's horizontal and vertical dimensions
        cropped_texture_surface = pg.Surface((x_length, y_length))
        # adding the cropped texture to the newly created Surface
        cropped_texture_surface.blit(texture_surface, (0, 0), coordinates)
        # for a window's definition of 600*600 and a 15*15 matrix:
        # converting the Surface to a 40*40 pixels rectangle, so as to correspond
        # to window's 600*600 pixels definition: 15*15 texture rectangles matrix
        cropped_texture_surface = pg.transform.scale(cropped_texture_surface, (BX_PX_LN, BX_PX_LN))
        return cropped_texture_surface

    def get_surface(self, img_file, coordinates):
        """ Texture surface image file load and crop
        """
        texture_surface = self.surface_load(img_file)
        cropped_texture_surface = self.crop_surface(texture_surface, coordinates)
        return cropped_texture_surface

    def load_surfaces_json(self):
        """ Surfaces dictionary loading function, from json file
        """
        surfaces_json = stg.json_load(stg.SCRIPT_DIR, stg.SURFACES_FILE)
        return surfaces_json
