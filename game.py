#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" MacGyver game : you're gonna have to help him escape!
"""

import frontend as frtd
import backend as bckd

def main():
    """ TODO : Docstring to be completed
    """
    display = frtd.Window()
    display.load()
    surfaces = frtd.surfaces_dict()
    clock = frtd.CLOCK
    display.background_init(surfaces)
    background = display.screen.copy()
    frtd.sprites_gen(surfaces)
    macgyver = frtd.MOBILE_SPRITES.sprites()[0]
    # pylint doesn't recognize pygame's members (QUIT, KEYDOWN... see below)
    # pylint: disable-msg=no-member
    # allowed events management
    frtd.pg.event.set_allowed((frtd.pg.QUIT, frtd.pg.KEYDOWN))
    # pylint: enable-msg=no-member

    # game time!
    on_air = True
    while on_air:
        # Frames Per Second definition
        clock.tick(frtd.stg.FPS)
        display.screen.blit(background, (0, 0))
        frtd.MOTIONLESS_SPRITES.draw(display.screen)
        frtd.MOBILE_SPRITES.draw(display.screen)
        if macgyver.won == True:
            display.print_won_message()
            # wait for three seconds before closing display
            clock.tick(0.3)
            on_air = False
        frtd.pg.display.update()
        event = frtd.pg.event.wait()
        on_air = bckd.get_events(event, on_air, macgyver)


if __name__ == '__main__':
    main()
