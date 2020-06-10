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
    labyrinth_matrix, drop_point, exit_point = lbth.grid_generation('backend')
    display = wdw.load(directory='frontend/resources')
    surfaces = txtr.surfaces_dict('frontend', 'frontend/resources')
    display = wdw.background_init(labyrinth_matrix, display, surfaces)

if __name__ == '__main__':
    main()
