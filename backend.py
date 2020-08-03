#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Backend labyrinth grid generation and management module
"""

import pygame as pg

import settings as stg
import frontend.movingobject as mvobj

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

def get_events(event, on_air, macgyver):
    """ Function used to manage pygame keyboard and quit events.
    MacGyver's collisions with other sprites are checked.
    An index is returned, indicating the sprite with whom the collision took place.
    """
    syringe = mvobj.MovingObject.sprites['syringe']
    if event.type == pg.KEYDOWN:
        if event.key in (pg.K_DOWN, pg.K_KP2):
            macgyver.physical_move(0, 1)
        elif event.key in (pg.K_UP, pg.K_KP8):
            macgyver.physical_move(0, -1)
        elif event.key in (pg.K_LEFT, pg.K_KP4):
            macgyver.physical_move(-1, 0)
        elif event.key in (pg.K_RIGHT, pg.K_KP6):
            macgyver.physical_move(1, 0)
        elif event.key == pg.K_ESCAPE:
            on_air = False
        collision_index = macgyver.rect.collidelist(mvobj.MOTIONLESS_SPRITES.sprites())
        if collision_index != -1:
            mvobj.MOTIONLESS_SPRITES.sprites()[collision_index].pick()
            pk_obj = mvobj.MovingObject.picked_objects
            syringe_conditions = 'needle' in pk_obj and 'ether' in pk_obj and 'plastube' in pk_obj
            if syringe_conditions and 'syringe' not in pk_obj:
                syringe.visible = True
                syringe.add_to_sprites()
                syringe.pick()
    # quit event definition
    elif event.type == pg.QUIT:
        on_air = False
    return on_air

def main():
    """ In case script is self executed, all imported values are shown
    """
    labyrinth = Labyrinth()
    labyrinth.grid_gen()
    print(f"Imported values verification:\n- game matrix: \n {labyrinth.labyrinth_matrix}")
    print(f"- drop point coordinates: \n{labyrinth.drop_point}, on a:")
    print(f"{labyrinth.labyrinth_matrix[labyrinth.drop_point[1]][labyrinth.drop_point[0]]} value")
    print(f"- exit point coordinates:\n{labyrinth.exit_point}, on a:")
    print(f"{labyrinth.labyrinth_matrix[labyrinth.drop_point[1]][labyrinth.drop_point[0]]} value")

if __name__ == '__main__':
    main()
