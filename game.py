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
    display.background_init(surfaces)
    clock = frtd.CLOCK

    # game time
    on_air = True
    while on_air:
        # Frames Per Second definition
        clock.tick(frtd.stg.FPS)
        # quit event definition
        for event in frtd.pg.event.get():
# pylint doesn't recognize pygame's quit member
# pylint: disable-msg=no-member
            if event.type == frtd.pg.QUIT:
# pylint: enable-msg=no-member
                on_air = False
        frtd.pg.display.update()
        frtd.SPRITES.draw(display.screen)
        frtd.pg.display.update()

# pylint: disable-msg=no-member
frtd.pg.quit()
# pylint: enable-msg=no-member


if __name__ == '__main__':
    main()
