#! /usr/bin/env python3
# coding: utf-8

""" Generation and interactions with the 15 boxes grid labyrinth
on which the game is played
"""
import json
import os

def grid_generation(directory='.', matrix_file='matrix.json'):
    """ Generates the 15 boxes grid statically
    Labyrinth's walls are symbolised with 'W', corridors with 'c'.
    Drop and exit points are coordinates tuples.
    Structure is stored in the "matrix.json" file
    """
    with open(os.path.join(directory, matrix_file), 'r') as file:
        matrix_json = json.load(file)
    labyrinth_matrix = matrix_json['labyrinth_matrix']
    drop_point = tuple(matrix_json['drop_point'])
    exit_point = tuple(matrix_json['exit_point'])
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
