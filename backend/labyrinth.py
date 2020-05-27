#! /usr/bin/env python3
# coding: utf-8

""" Module generating and interacting with the 15 boxes grid labyrinth on which the game is played
"""

import numpy as np

def grid_generation():
    """ Function used to generate the 15 boxes grid statically
    Labyrinth's walls are symbolised with 'W', corridors with 'c'.
    Drop and exit points are coordinates tuples.
    Structure is stored in the "matrix.npy" binary file
    """
    with open('matrix.npy', 'rb') as file:
        labyrinth_matrix = np.load(file)
        drop_point = tuple(np.load(file))
        exit_point = tuple(np.load(file))
    return labyrinth_matrix, drop_point, exit_point


def main():
    """ In case script is self executed, all imported values are shown
    """
    labyrinth_matrix, drop_point, exit_point = grid_generation()
    print("Imported values verification:")
    print(f"- game matrix: \n {labyrinth_matrix}")
    print("- drop point coordinates:")
    print(f"{drop_point}, on a: \'{labyrinth_matrix[drop_point]}\' value")
    print("- exit point coordinates:")
    print(f"{exit_point}, on a: \'{labyrinth_matrix[exit_point]}\' value")

if __name__ == '__main__':
    main()
