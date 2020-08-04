#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" MacGyver game : you're gonna have to help him escape!
Angus has been captured in a labyrinth, retained inside by a dangerous guard.
You're his last chance to get out!
Grab all elements distributed troughout the maze to anesthetize the jailer!
Your legendary hero is on his way to survive one more time!
"""

import pygame as pg

from frontend import window as wdw
from frontend import main as frtd
from frontend import texture as txtr
from frontend import movingobject as mvobj
from backend import main as bckd
from resources import settings as stg

def main():
    """ Displayed elements are managed by the frontend submodule.
    Each frame, background is blitted, then sprites groups are drawn on the screen.
    This way, sprites movements are taken into account.
    While on_air, the program will loop, waiting for user's inputs (keyboard's directional keys).
    This part is treated by the backend submodule.
    """
    display = wdw.Window()
    display.load()
    txtr.Texture.surfaces_dict()
    clock = wdw.CLOCK
    display.background_init(txtr.Texture.surfaces)
    background = display.screen.copy()
    frtd.sprites_gen(txtr.Texture.surfaces)
    macgyver = mvobj.MovingObject.sprites['macgyver']
    # allowed events management
    pg.event.set_allowed((pg.QUIT, pg.KEYDOWN))

    # game time!
    on_air = True
    while on_air:
        # Frames Per Second definition
        clock.tick(stg.FPS)
        display.screen.blit(background, (0, 0))
        mvobj.MOTIONLESS_SPRITES.draw(display.screen)
        mvobj.MOBILE_SPRITES.draw(display.screen)
        if macgyver.states['won']:
            on_air = display.print_end_message('won')
        elif macgyver.states['dead']:
            on_air = display.print_end_message('lose')
        pg.display.update()
        event = pg.event.wait()
        on_air = bckd.get_events(event, on_air, macgyver)


if __name__ == '__main__':
    main()
