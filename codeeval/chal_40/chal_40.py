#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #40 (SELF DESCRIBING NUMBERS)
https://www.codeeval.com/open_challenges/40/

AUTHOR: Erik Johnson
DATE: 2015-OCT-04

DISCUSSION:
"""


if __name__ == "__main__":

    lines_out = []
    for line in open(sys.argv[1], 'r'):
        counts = [0] * 10
        line = line.strip()
        N = len(line)
        for i in [int(c) for c in line]:
            counts[i] += 1

        if ''.join([str(i) for i in counts[:N]]) == line:
            zero_one = '1'
        else:
            zero_one = '0'

        lines_out.append(zero_one)

    print '\n'.join(lines_out)
