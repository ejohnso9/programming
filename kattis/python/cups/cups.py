#!/usr/bin/env python3

"""
DESCRIPTION
    https://open.kattis.com/contests/x4dmg8/problems/cups

AUTHOR
    Erik Johnson

HISTORY
    2020Dec19  Created
"""

import sys

# GLOBAL DATA
NL = '\n'

def process(data):
    new_l = []
    for line in data:
        color, radius = line.split()
        try:
            diam = int(radius) * 2
        except ValueError as ve:
            # reversed: "diam color"
            diam, color = int(color), radius
        new_l.append((diam, color))
        
    # default tuple sort (i.e., by first element first)
    return sorted(new_l)


def output(answers):
    print(NL.join([t[1] for t in answers]))


def main():
    answers = []
    fd = sys.stdin
    n_cases = int(fd.readline().strip())
    lines = fd.readlines()
    answers = process(lines)
    output(answers)


if __name__ == '__main__':
    main()

