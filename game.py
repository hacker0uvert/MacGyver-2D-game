#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" MacGyver game : you're gonna have to help him escape!
"""

import frontend as frtd

def main():
    """ TODO : Docstring to be completed
    """
    display = frtd.Window()
    display.load()
    surfaces = frtd.surfaces_dict()
    clock = frtd.CLOCK
    display.background_init(surfaces)
    background = display.screen.copy()
    sprites = frtd.sprites_gen(surfaces)
    macgyver = sprites['macgyver']

    # game time!
    on_air = True
    while on_air:
        # Frames Per Second definition
        clock.tick(frtd.stg.FPS)
        display.screen.blit(background, (0, 0))
        frtd.SPRITES.draw(display.screen)
        frtd.pg.display.update()
        # pylint doesn't recognize pygame's members (QUIT, KEYDOWN... see below)
# pylint: disable-msg=no-member
        # allowed events management
        frtd.pg.event.set_allowed((frtd.pg.QUIT, frtd.pg.KEYDOWN))
        event = frtd.pg.event.wait()
        if event.type == frtd.pg.KEYDOWN:
            if event.key in (frtd.pg.K_DOWN, frtd.pg.K_KP2):
                macgyver.physical_move(0, 1)
            elif event.key in (frtd.pg.K_UP, frtd.pg.K_KP8):
                macgyver.physical_move(0, -1)
            elif event.key in (frtd.pg.K_LEFT, frtd.pg.K_KP4):
                macgyver.physical_move(-1, 0)
            elif event.key in (frtd.pg.K_RIGHT, frtd.pg.K_KP6):
                macgyver.physical_move(1, 0)
        # quit event definition
        elif event.type == frtd.pg.QUIT:
            on_air = False
# pylint: enable-msg=no-member


if __name__ == '__main__':
    main()
