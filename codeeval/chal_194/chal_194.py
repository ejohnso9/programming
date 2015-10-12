#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #194  (TWENTY FORTY EIGHT)
https://www.codeeval.com/open_challenges/194/

AUTHOR: Erik Johnson

DISCUSSION:

Sample input

RIGHT; 4; 4 0 2 0|0 0 0 8|4 0 2 4|2 4 2 2
UP; 4; 2 0 2 0|0 2 0 4|2 8 0 8|0 8 0 16
"""

def get_col(lol, index, up=False):
    pass

def combine(a):
    rv_l = []
    b = filter(None, a) # drop zeroes
    N = len(b)

    i = 0
    while i < N:
        bi = b[i]

        # just append last element
        if i == (N - 1):
            rv_l.append(bi)
            break;

        if b[i] == b[i + 1]:
            rv_l.append(2 * bi)
            i += 2
        else:
            rv_l.append(bi)
            i += 1

    return rv_l


if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        # ignoring first two elements - not needed!
        direction, size, data = [x.strip() for x in line.split(';')]
        size = int(size)
        lol = []
        for row in data.split('|'):
            lol.append([int(s) for s in row.split()])

        print lol
        # print ''.join([chr(i - offset) for i in iList])

