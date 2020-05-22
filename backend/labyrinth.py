#! /usr/bin/env python3
# coding: utf-8

""" Module generating and interacting with the 15 boxes grid labyrinth on which the game is played
"""

import numpy as np
import pickle as pk

def grid_generation():
    """ Function used to generate the 15 boxes grid statically
    Labyrinth's walls are symbolised with 1, corridors with 0.
    Structure is stored in the "matrix" binary file
    """
    with open("matrix", "rb") as file:
	    depickler = pk.Unpickler(file)
	    labyrinth_matrix = depickler.load()
	return labyrinth_matrix
    

def main():
    pass

if __name__ == '__main__':
    main()