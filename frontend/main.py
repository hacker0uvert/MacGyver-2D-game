#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Frontend main submodule.
"""

from resources import settings as stg
from frontend import movingobject as mvobj

def sprites_gen(surfaces):
    """ Sprites generation and conversion into MovingObject function
    """
    for name, group, visibility in stg.SPRITES_LIST:
        surface = surfaces[name]
        mvobj.MovingObject(name, surface, group, visibility)
