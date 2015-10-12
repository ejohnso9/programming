#!/usr/bin/env python

import sys, math

"""
Solution for codeeval challenge #92 (PENULTIMATE WORD)
https://www.codeeval.com/open_challenges/92/

AUTHOR: Erik Johnson

DISCUSSION:
"""


if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        print line.split()[-2]
