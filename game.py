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

if __name__ == '__main__':
    main()
