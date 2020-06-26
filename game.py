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
        # quit event definition
        for event in frtd.pg.event.get():
# pylint doesn't recognize pygame's quit member
# pylint: disable-msg=no-member
            if event.type == frtd.pg.QUIT:
# pylint: enable-msg=no-member
                on_air = False
            elif event.type == frtd.pg.KEYDOWN:
                if event.key == frtd.pg.K_DOWN:
                    macgyver.physical_move(0, 1)
                elif event.key == frtd.pg.K_UP:
                    macgyver.physical_move(0, -1)
                elif event.key == frtd.pg.K_LEFT:
                    macgyver.physical_move(-1, 0)
                elif event.key == frtd.pg.K_RIGHT:
                    macgyver.physical_move(1, 0)
        display.screen.blit(background, (0, 0))
        frtd.SPRITES.draw(display.screen)
        frtd.pg.display.update()

# pylint: disable-msg=no-member
frtd.pg.quit()
# pylint: enable-msg=no-member


if __name__ == '__main__':
    main()
