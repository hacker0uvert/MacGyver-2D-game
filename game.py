#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" MacGyver game : you're gonna have to help him escape!
"""

import backend as bckd
import frontend as frtd

def main():
    """ TODO : Docstring to be completed
    """
    labyrinth_matrix, drop_point, exit_point = bckd.grid_gen(stg.SCRIPT_DIR, stg.MATRIX_FILE)
    display = frtd.Window()
    display.load()
    surfaces = frtd.Texture()
    surfaces.surfaces_dict()
    display = wdw.background_init(labyrinth_matrix, display, surfaces)

if __name__ == '__main__':
    main()
