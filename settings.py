#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module used to store game settings
"""

import json
import os

# directories
SCRIPT_DIR = os.path.split(os.path.abspath(__file__))[0]
SURFACES_JSON_DIR = SCRIPT_DIR
RESOURCES_DIR = os.path.join(SCRIPT_DIR, 'resources')

# files
MATRIX_FILE = 'matrix.json'
SURFACES_FILE = 'surfaces.json'
ICON_FILE = 'MacGyver.png'

# parameters
WINDOW_RESOLUTION = (600, 600)
WINDOW_CAPTION = 'MacGyver-2D'

def json_load(directory, json_file):
    """ Json file loading function
    """
    with open(os.path.join(directory, json_file), 'r') as file:
        json_content = json.load(file)
    return json_content
