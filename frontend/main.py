#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Frontend package main module.
"""

import settings as stg
import frontend.texture as txtr
import frontend.movingobject as mvobj

def surfaces_dict():
    """ Surfaces dictionary definition function.
    Values are defined from surfaces_json dict.
    """
    surfaces = {}
    textures = txtr.Texture()
    surfaces_json = textures.load_surfaces_json()
    for i in surfaces_json:
        surface = textures.get_surface(surfaces_json[i][0], surfaces_json[i][1])
        surfaces[i] = surface
    return surfaces

def sprites_gen(surfaces):
    """ Sprites generation and conversion into MovingObject function
    """
    for name, group, visibility in stg.SPRITES_LIST:
        surface = surfaces[name]
        mvobj.MovingObject(name, surface, group, visibility)
