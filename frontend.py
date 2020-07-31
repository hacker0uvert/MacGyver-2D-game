#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Frontend window management and textures manipulation module.
MovingObject is used to add functionnalities to the native Pygame Sprite class.
"""

import os
import random

import pygame as pg

import backend as bckd
import settings as stg

LABYRINTH = bckd.Labyrinth()
CLOCK = pg.time.Clock()
MOTIONLESS_SPRITES = pg.sprite.Group()
MOBILE_SPRITES = pg.sprite.Group()
BX_PX_LN = LABYRINTH.box_px_len

class Window:
    """ Physical window management
    """

    def __init__(self):
        """ Window class initiator
        """
        self.icon_file = stg.ICON_FILE
        self.window_resolution = stg.WINDOW_RESOLUTION
        self.window_caption = stg.WINDOW_CAPTION
        # set_mode needs a pygame display init. pylint raises a "defined outside __init__" warning.
        self.screen = None

    def load(self):
        """ Window loading function
        """
        pg.display.init()
        self.screen = pg.display.set_mode(self.window_resolution)
        pg.display.set_caption(self.window_caption)
        self.icon()

    def icon(self):
        """ Window icon's loading function
        """
        with open(os.path.join(stg.RESOURCES_DIR, self.icon_file), 'r') as file:
            ico = pg.image.load(file)
        pg.display.set_icon(ico)

    def background_init(self, surfaces):
        """ Walls and corridors background textures initialisation.
        In the json file, 'wall' is corresponding to 'W' in the labyrinth_matrix.
        'c' stands for 'corridor'
        'i' for 'items_counter'
        """
        lab = LABYRINTH
        x_itr, y_itr = 0, 0
        while y_itr in range(lab.grid_len):
            while x_itr in range(lab.grid_len):
                if lab.labyrinth_matrix[y_itr][x_itr] == 'W':
                    self.screen.blit(surfaces['wall'], (x_itr*BX_PX_LN, y_itr*BX_PX_LN))
                elif lab.labyrinth_matrix[y_itr][x_itr] == 'c':
                    self.screen.blit(surfaces['corridor'], (x_itr*BX_PX_LN, y_itr*BX_PX_LN))
                    # corridors coordinates list generation
                    lab.corridors_coordinates.append((x_itr, y_itr))
                elif lab.labyrinth_matrix[y_itr][x_itr] == 'i':
                    self.screen.blit(surfaces['counter'], (x_itr*BX_PX_LN, y_itr*BX_PX_LN))
                    # counter coordinates list generation
                    lab.counters_coordinates.append((x_itr, y_itr))
                x_itr += 1
            y_itr += 1
            x_itr = 0
        pg.display.flip()
        # drop_point and exit_point coordinates tuples remove from lab.corridors_coordinates
        lab.corridors_coordinates.remove(lab.drop_point)
        lab.corridors_coordinates.remove(lab.exit_point)

    def print_end_message(self, exit_status):
        """ Method used to define and print won message onscreen.
        """
        pg.font.init()
        # font size is proportionate to display's horizontal resolution
        font = pg.font.Font(None, stg.FONT_SIZE)
        if exit_status == 'won':
            font_surface = font.render(stg.WON_MESSAGE, True, stg.WON_MESSAGE_COLOR)
        elif exit_status == 'lose':
            font_surface = font.render(stg.DEAD_MESSAGE, True, stg.DEAD_MESSAGE_COLOR)
        font_rect = font_surface.get_rect(center=(stg.RESOLUTION/2, stg.RESOLUTION/2))
        self.screen.blit(font_surface, font_rect)
        pg.display.update()
        # wait for three seconds before closing display
        CLOCK.tick(0.3)
        on_air = False
        return on_air


class Texture:
    """ Textures manipulation
    """

    def __init__(self):
        """ Class initiator
        """

    def surface_load(self, img_file):
        """ Texture surface image loading function
        """
        with open(os.path.join(stg.RESOURCES_DIR, img_file), 'r') as file:
            texture_surface = pg.image.load(file).convert_alpha()
        return texture_surface

    def crop_surface(self, texture_surface, coordinates):
        """ Texture surface crop function
        """
        x_length = coordinates[2] - coordinates[0]
        y_length = coordinates[3] - coordinates[1]
        # creation of a new Surface with the cropped texture's horizontal and vertical dimensions
        cropped_texture_surface = pg.Surface((x_length, y_length))
        # adding the cropped texture to the newly created Surface
        cropped_texture_surface.blit(texture_surface, (0, 0), coordinates)
        # for a window's definition of 600*600 and a 15*15 matrix:
        # converting the Surface to a 40*40 pixels rectangle, so as to correspond
        # to window's 600*600 pixels definition: 15*15 texture rectangles matrix
        cropped_texture_surface = pg.transform.scale(cropped_texture_surface, (BX_PX_LN, BX_PX_LN))
        return cropped_texture_surface

    def get_surface(self, img_file, coordinates):
        """ Texture surface image file load and crop
        """
        texture_surface = self.surface_load(img_file)
        cropped_texture_surface = self.crop_surface(texture_surface, coordinates)
        return cropped_texture_surface

    def load_surfaces_json(self):
        """ Surfaces dictionary loading function, from json file
        """
        surfaces_json = stg.json_load(stg.SCRIPT_DIR, stg.SURFACES_FILE)
        return surfaces_json


class MovingObject(pg.sprite.Sprite):
    """ Sprites (characters and objects) management
    """

    sprites = {}
    PICKED_OBJECTS = []

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
            MovingObject.PICKED_OBJECTS.append(self.name)


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
                if 'syringe' in MovingObject.PICKED_OBJECTS:
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


def surfaces_dict():
    """ Surfaces dictionary definition function.
    Values are defined from surfaces_json dict.
    """
    surfaces = {}
    textures = Texture()
    surfaces_json = textures.load_surfaces_json()
    for i in surfaces_json:
        surface = textures.get_surface(surfaces_json[i][0], surfaces_json[i][1])
        surfaces[i] = surface
    return surfaces

def sprites_gen(surfaces):
    """ Sprites generation and conversion into MovingObject function
    """
    for name, group, visibility in stg.SPRITES_LIST:
        surface = surfaces[name]
        MovingObject(name, surface, group, visibility)
