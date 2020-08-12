#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Frontend package textures manipulation module.
"""

import os

import pygame as pg

from resources import settings as stg
from frontend import window as wdw

BX_PX_LN = wdw.BX_PX_LN

class Texture:
    """ Textures manipulation
    """

    def __init__(self, img_file, coordinates):
        """ Class initiator
        """
        self.img_file = img_file
        self.coordinates = coordinates
        self.cropped_texture_surface = self.get_surface()

    @classmethod
    def load_surfaces_json(cls):
        """ Surfaces dictionary loading method, from json file
        """
        cls.surfaces_json = stg.json_load(stg.SCRIPT_DIR, stg.SURFACES_FILE)

    @classmethod
    def surfaces_dict(cls):
        """ Surfaces dictionary definition method.
        Values are defined from surfaces_json dict.
        """
        cls.surfaces = {}
        cls.load_surfaces_json()
        for i in cls.surfaces_json:
            texture = cls(cls.surfaces_json[i][0], cls.surfaces_json[i][1])
            surface = texture.cropped_texture_surface
            cls.surfaces[i] = surface

    def surface_load(self):
        """ Texture surface image loading method
        """
        with open(os.path.join(stg.SCRIPT_DIR, self.img_file), 'r') as file:
            texture_surface = pg.image.load(file).convert_alpha()
        return texture_surface

    def crop_surface(self, texture_surface):
        """ Texture surface crop method
        """
        x_length = self.coordinates[2] - self.coordinates[0]
        y_length = self.coordinates[3] - self.coordinates[1]
        # creation of a new Surface with the cropped texture's horizontal and vertical dimensions
        cropped_texture_surface = pg.Surface((x_length, y_length))
        # adding the cropped texture to the newly created Surface
        cropped_texture_surface.blit(texture_surface, (0, 0), self.coordinates)
        # for a window's definition of 600*600 and a 15*15 matrix:
        # converting the Surface to a 40*40 pixels rectangle, so as to correspond
        # to window's 600*600 pixels definition: 15*15 texture rectangles matrix
        cropped_texture_surface = pg.transform.scale(cropped_texture_surface, (BX_PX_LN, BX_PX_LN))
        return cropped_texture_surface

    def get_surface(self):
        """ Texture surface image file load and crop
        """
        texture_surface = self.surface_load()
        cropped_texture_surface = self.crop_surface(texture_surface)
        return cropped_texture_surface
