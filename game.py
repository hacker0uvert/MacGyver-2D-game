#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" MacGyver game : you're gonna have to help him escape!
Angus has been captured in a labyrinth, retained inside by a dangerous guard.
You're his last chance to get out!
Grab all elements distributed troughout the maze to anesthetize the jailer!
Your legendary hero is on his way to survive one more time!
"""

import pygame as pg

import frontend as frtd
import backend as bckd
import settings as stg

def main():
    """ Displayed elements are managed by the frontend package.
    While on_air, the program will loop, waiting for user's inputs (keyboard's directional keys).
    This part is treated by the backend package.
    """
    display = frtd.Window()
    display.load()
    surfaces = frtd.surfaces_dict()
    clock = frtd.CLOCK
    display.background_init(surfaces)
    background = display.screen.copy()
    frtd.sprites_gen(surfaces)
    macgyver = frtd.MovingObject.sprites['macgyver']
    # allowed events management
    pg.event.set_allowed((pg.QUIT, pg.KEYDOWN))

    # game time!
    on_air = True
    while on_air:
        # Frames Per Second definition
        clock.tick(stg.FPS)
        display.screen.blit(background, (0, 0))
        frtd.MOTIONLESS_SPRITES.draw(display.screen)
        frtd.MOBILE_SPRITES.draw(display.screen)
        if macgyver.won:
            display.print_end_message('won')
            # wait for three seconds before closing display
            clock.tick(0.3)
            on_air = False
        elif macgyver.dead:
            display.print_end_message('lose')
            # wait for three seconds before closing display
            clock.tick(0.3)
            on_air = False
        pg.display.update()
        event = pg.event.wait()
        on_air = bckd.get_events(event, on_air, macgyver)


if __name__ == '__main__':
    main()
