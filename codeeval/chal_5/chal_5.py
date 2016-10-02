#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #5 (DETECTING CYCLES)
https://www.codeeval.com/open_challenges/5/

AUTHOR: Erik Johnson
DATE: 2016-May-24

APROACH:
    With only 50 numbers in the input sequence, this also becomes a
fairly trivial problem: Just build a dict storing the indices where
numbers were first seen. When you hit a number the second time the cycle
repeats from the index where it was first seen through the index where
it was seen a second time minus one.
"""


if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        d = {}

        # loop over nums in one line
        l = line.rstrip().split()
        for i in range(len(l)):
            n = l[i]
            if not d.has_key(n):
                d[n] = i
            else:
                lines_out.append(' '.join(l[d[n] : i]))
                break

    print '\n'.join(lines_out)
    sys.stdout.flush()
