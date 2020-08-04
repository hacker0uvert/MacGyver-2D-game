#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Backend labyrinth grid generation and management module.
"""

from resources import settings as stg

class Labyrinth:
    """ Generation and interactions with the grid labyrinth on which the game is played
    """

    def __init__(self):
        """ Labyrinth class initiator
        """
        self.labyrinth_matrix, self.drop_point, self.exit_point = self.grid_gen()
        self.grid_len = self.grid_length()
        self.box_px_len = self.boxes_pixel_length()
        self.corridors_coordinates = []
        self.counters_coordinates = []

    @classmethod
    def grid_gen(cls):
        """ Generates the grid statically
        Labyrinth's walls are symbolised with 'W', corridors with 'c', and counters with 'i'
        Drop and exit points are coordinates tuples.
        """
        matrix_json = stg.json_load(stg.SCRIPT_DIR, stg.MATRIX_FILE)
        labyrinth_matrix = matrix_json['labyrinth_matrix']
        drop_point = tuple(matrix_json['drop_point'])
        exit_point = tuple(matrix_json['exit_point'])
        return labyrinth_matrix, drop_point, exit_point

    def grid_length(self):
        """ Method used to get the grid's line boxes number
        """
        grid_len = len(self.labyrinth_matrix[0])
        return grid_len

    def boxes_pixel_length(self):
        """ Method used to define each grid's boxe's length in pixels.
        Corresponds to window's line pixels definition divided by line's boxes number.
        """
        box_px_len = int(stg.WINDOW_RESOLUTION[0] / self.grid_len)
        return box_px_len
