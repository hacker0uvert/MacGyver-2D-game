#! /usr/bin/env python3
# coding: utf-8

""" Module generating and interacting with the 15 boxes grid labyrinth on which the game is played
"""

import numpy as np

def grid_generation():
    """ Function used to generate the 15 boxes grid
    """
    # labyrinth's walls are symbolised with 1, corridors with 0. Matrix is generated statically.
    labyrinth_matrix = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

def main():
    pass

if __name__ == '__main__':
    main()