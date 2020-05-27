#! /usr/bin/env python3
# coding: utf-8

import pygame as pg

import backend.labyrinth as lbth


def main():
    """ ---> Docstring to be completed <---
    """
    labyrinth_matrix, drop_point, exit_point = lbth.grid_generation()
    print(labyrinth_matrix, drop_point, exit_point)

if __name__ == '__main__':
    main()
