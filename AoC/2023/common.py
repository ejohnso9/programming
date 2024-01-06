#!/usr/bin/env python
#        1         2         3         4         5         6         7         8         9         0         1         2
#23456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# run on pythonanywhere.com @ Python version 3.9.5

"""
Library of common code supporting Advent of Code solutions
"""


def load_lines(filename):
    """
    a simple helper to read the input file, return a list of strings as lines
    ('\n' (and any other whitespace) stripped from end, but unchanged at front)
    """

    with open(filename, 'r') as fd:
        lines = fd.readlines()

    return [line.rstrip() for line in lines]

