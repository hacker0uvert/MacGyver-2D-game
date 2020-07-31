#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module used to store game settings
"""

import json
import os

# directories #
SCRIPT_DIR = os.path.split(os.path.abspath(__file__))[0]
RESOURCES_DIR = os.path.join(SCRIPT_DIR, 'resources')

# files #
MATRIX_FILE = 'matrix.json'
SURFACES_FILE = 'surfaces.json'
ICON_FILE = 'MacGyver.png'

# parameters #
WINDOW_RESOLUTION = (600, 600)
WINDOW_CAPTION = 'MacGyver-2D'
FPS = 25
WON_MESSAGE = "Well done, MacGyver has gone OUT!"
WON_MESSAGE_COLOR = (34, 215, 255)
DEAD_MESSAGE = "Well well well, MacGyver is DEAD!"
DEAD_MESSAGE_COLOR = (127, 30, 20)

def len_message():
    """ Defines which one of WON_MESSAGE or DEAD_MESSAGE is the longest
    """
    won_msg_len = len(WON_MESSAGE)
    dead_msg_len = len(DEAD_MESSAGE)
    if won_msg_len > dead_msg_len:
        returned_len = won_msg_len
    elif dead_msg_len > won_msg_len:
        returned_len = dead_msg_len
    else:
        returned_len = won_msg_len
    return returned_len

# Font proportion has been calculated afer numerous tests, with different window resolutions.
# Its value is dimensionned, so that in all test cases, full message is displayed on screen.
FONT_PROPORTION = 2.667
FONT_SIZE = int(WINDOW_RESOLUTION[0] / len_message() * FONT_PROPORTION)
# sprites are listed with their name, sprite.group name, and visibility boolean
SPRITES_LIST = [
    ('macgyver', 'mobile', True),
    ('guardian', 'motionless', True),
    ('needle', 'motionless', True),
    ('plastube', 'motionless', True),
    ('ether', 'motionless', True),
    ('syringe', 'motionless', False),
    ('dead', 'motionless', False),
    ('counter', 'motionless', False)
    ]

def json_load(directory, json_file):
    """ Json file loading function
    """
    with open(os.path.join(directory, json_file), 'r') as file:
        json_content = json.load(file)
    return json_content
