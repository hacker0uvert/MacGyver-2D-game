#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Frontend package: MovingObject module is used to enhance native Pygame's Sprite class functions.
"""

import random

import pygame as pg

import backend as bckd
import settings as stg

LABYRINTH = bckd.Labyrinth()
MOTIONLESS_SPRITES = pg.sprite.Group()
MOBILE_SPRITES = pg.sprite.Group()
BX_PX_LN = LABYRINTH.box_px_len

class MovingObject(pg.sprite.Sprite):
    """ Sprites (characters and objects) management
    """

    sprites = {}
    picked_objects = []

    def __init__(self, name, surface, group, visible):
        """ Class initiator.
        MacGyver and Guardian are respectively positionned on drop_point and exit_point.
        Ether, needle and plastube sprites are randomly dropped in the corridors.
        Above actions are applied to each element thanks to the name argument,
        which enables sprite recognition.
        """
        pg.sprite.Sprite.__init__(self)
        # value used to define if object has been collected by MacGyver
        self.name = name
        self.group = group
        self.visible = visible
        self.image = surface
        self.rect_def()
        self.sprites[self.name] = self
        if self.visible:
            self.add_to_sprites()
        if self.name == 'macgyver':
            self.direction = 'right'
            self.right_image = self.image
            self.left_image = pg.transform.flip(self.image, True, False)
            self.physical_move(LABYRINTH.drop_point[0], LABYRINTH.drop_point[1])
            self.won = False
            self.dead = False
        if self.name == 'guardian':
            self.physical_move(LABYRINTH.exit_point[0], LABYRINTH.exit_point[1])
        if self.name in ('ether', 'needle', 'plastube'):
            self.random_coordinates()

    def rect_def(self):
        """ MovingObject rectangle definition, from image surface
        """
        self.rect = self.image.get_rect()

    def add_to_sprites(self):
        """ MovingObject addition to the all_SPRITES group, so as to be blitted on the screen.
        """
        if self.group == 'motionless':
            MOTIONLESS_SPRITES.add(self)
        elif self.group == 'mobile':
            MOBILE_SPRITES.add(self)

    def pick(self):
        """ Method used to specify that an object was picked by MacGyver while moving on the grid.
        Object is deleted from SPRITES group, as it mustn't be blitted on the screen anymore.
        """
        if self.name in ('ether', 'needle', 'plastube', 'syringe'):
            self.physical_move(0, 0, corridor=False)
            MovingObject.picked_objects.append(self.name)


    def physical_move(self, x_case_move, y_case_move, corridor=True):
        """ Movement from present physical position to x_case_move horizontal,
        y_case_move vertical new cases (negative move authorised).
        x_move and y_move correspond to the same movement, converted into pixels,
        depending on the current display size and number of grid cases.
        New coordinates are verified, so that sprite can't get out of display.
        """
        if not corridor:
            coordinates = LABYRINTH.counters_coordinates.pop(0)
            x_new_coordinates = coordinates[0] * BX_PX_LN
            y_new_coordinates = coordinates[1] * BX_PX_LN
            x_move = x_new_coordinates - self.rect.x
            y_move = y_new_coordinates - self.rect.y
            move_boolean = True
        elif corridor:
            x_move = x_case_move * BX_PX_LN
            y_move = y_case_move * BX_PX_LN
            x_new_coordinates = self.rect.x + x_move
            y_new_coordinates = self.rect.y + y_move
            x_cond = x_new_coordinates <= (stg.WINDOW_RESOLUTION[0] - BX_PX_LN)
            y_cond = y_new_coordinates <= (stg.WINDOW_RESOLUTION[1] - BX_PX_LN)
            if x_cond and x_new_coordinates >= 0 and y_cond and y_new_coordinates >= 0:
                move_boolean = self.check_if_corridor(x_new_coordinates, y_new_coordinates)
        if move_boolean:
            self.rect.move_ip(x_move, y_move)
            # macgyver's direction management
            if self.name == 'macgyver':
                if x_move < 0 and self.direction == 'right':
                    self.direction = 'left'
                    self.image = self.left_image
                elif x_move > 0 and self.direction == 'left':
                    self.direction = 'right'
                    self.image = self.right_image


    def check_if_corridor(self, x_coordinates, y_coordinates):
        """ Used to verify if a position is a corridor in labyrinth's matrix.
        This is to ensure that sprites are unable to get threw or on a wall.
        grid_case is a tuple, corresponding to the grid's case position in the labyrinth_matrix.
        """
        grid_case = (int(x_coordinates / BX_PX_LN), int(y_coordinates / BX_PX_LN))
        case_texture = LABYRINTH.labyrinth_matrix[grid_case[1]][grid_case[0]]
        if case_texture == 'c':
            corridor = True
            if (grid_case == LABYRINTH.exit_point and self.name == 'macgyver'):
                if 'syringe' in MovingObject.picked_objects:
                    self.won = True
                else:
                    self.dead = True
                    self.image = MovingObject.sprites['dead'].image
        else:
            corridor = False
        return corridor

    def random_coordinates(self):
        """ Random coordinates generation, in labyrinth_matrix's coordinates range
        """
        if len(LABYRINTH.corridors_coordinates) < 1:
            raise ValueError("Not enough corridors available to generate syringe's items.")
        i = random.randint(0, len(LABYRINTH.corridors_coordinates) - 1)
        coordinates = LABYRINTH.corridors_coordinates.pop(i)
        x_coord, y_coord = coordinates[0], coordinates[1]
        self.physical_move(x_coord, y_coord)
