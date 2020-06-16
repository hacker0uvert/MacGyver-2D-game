#! /usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module used to store game settings
"""

import os

# directories
SCRIPT_DIR = os.path.split(os.path.abspath(__file__))[0]
SURFACES_JSON_DIR = SCRIPT_DIR
RESOURCES_DIR = os.path.join(SCRIPT_DIR, 'resources')

# files
MATRIX_FILE = 'matrix.json'
SURFACES_FILE = 'surfaces.json'
ICON_FILE = 'MacGyver.png'
