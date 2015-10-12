#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #2 (LONGEST LINES)
https://www.codeeval.com/open_challenges/NN/

AUTHOR: Erik Johnson
DATE: 2015-MAR-04

DISCUSSION:
"""

if __name__ == "__main__":

    lines = [line.strip() for line in open(sys.argv[1], 'r').readlines()]
    N = int(lines[0])
    lod = [] # list of dicts
    for line in lines[1:]:
        lod.append({'len': len(line), 'line': line})

    # sort 'lod' by line length
    lod.sort(key=lambda d: d['len'],reverse=True)
    for i in range(N):
        print lod[i]['line']

