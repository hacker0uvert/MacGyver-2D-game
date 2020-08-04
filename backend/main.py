#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Backend main submodule.
"""

import pygame as pg

from frontend import movingobject as mvobj

def get_events(event, on_air, macgyver):
    """ Function used to manage pygame keyboard and quit events.
    MacGyver's collisions with other sprites are checked.
    An index is returned, indicating the sprite with whom the collision took place.
    """
    syringe = mvobj.MovingObject.sprites['syringe']
    if event.type == pg.KEYDOWN:
        if event.key in (pg.K_DOWN, pg.K_KP2):
            macgyver.physical_move(0, 1)
        elif event.key in (pg.K_UP, pg.K_KP8):
            macgyver.physical_move(0, -1)
        elif event.key in (pg.K_LEFT, pg.K_KP4):
            macgyver.physical_move(-1, 0)
        elif event.key in (pg.K_RIGHT, pg.K_KP6):
            macgyver.physical_move(1, 0)
        elif event.key == pg.K_ESCAPE:
            on_air = False
        collision_index = macgyver.rect.collidelist(mvobj.MOTIONLESS_SPRITES.sprites())
        if collision_index != -1:
            mvobj.MOTIONLESS_SPRITES.sprites()[collision_index].pick()
            pk_obj = mvobj.MovingObject.picked_objects
            syringe_conditions = 'needle' in pk_obj and 'ether' in pk_obj and 'plastube' in pk_obj
            if syringe_conditions and 'syringe' not in pk_obj:
                syringe.visible = True
                syringe.add_to_sprites()
                syringe.pick()
    # quit event definition
    elif event.type == pg.QUIT:
        on_air = False
    return on_air
