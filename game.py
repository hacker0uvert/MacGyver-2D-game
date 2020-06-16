#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" MacGyver game : you're gonna have to help him escape!
"""

import settings as stg
import labyrinth as lbth
import texture as txtr
import window as wdw

def main():
    """ TODO : Docstring to be completed
    """
    labyrinth_matrix, drop_point, exit_point = lbth.grid_gen(stg.SCRIPT_DIR, stg.MATRIX_FILE)
    display = wdw.load(stg.RESOURCES_DIR, stg.ICON_FILE)
    surfaces = txtr.surfaces_dict(stg.SURFACES_JSON_DIR, stg.RESOURCES_DIR, stg.SURFACES_FILE)
    display = wdw.background_init(labyrinth_matrix, display, surfaces)

if __name__ == '__main__':
    main()
