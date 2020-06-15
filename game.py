#! /usr/bin/env python3
# coding: utf-8

""" MacGyver game : you're gonna have to help him escape!
"""

import backend.labyrinth as lbth
import frontend.texture as txtr
import frontend.window as wdw

def main():
    """ TODO : Docstring to be completed
    """
    labyrinth_matrix, drop_point, exit_point = lbth.grid_gen(lbth.SCRIPT_DIR, lbth.MATRIX_FILE)
    display = wdw.load(wdw.RESOURCES_DIR, wdw.ICON_FILE)
    surfaces = txtr.surfaces_dict(txtr.SURFACES_JSON_DIR, txtr.RESOURCES_DIR, txtr.SURFACES_FILE)
    display = wdw.background_init(labyrinth_matrix, display, surfaces)

if __name__ == '__main__':
    main()
