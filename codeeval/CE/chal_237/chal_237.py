#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #237 (PANACEA - TRUTH OR LIE)
https://www.codeeval.com/open_challenges/237/

AUTHOR: Erik Johnson
DATE: 2016-May-19

APPROACH:
    This is pretty basic textual processing. int() take a base as a
    second arg and can convert binary or hex representations into native
    ints very easily.
"""

def testLine(line):
    """returns 'True' or 'False' (string) for input line"""
    viral, anti = line.split('|')
    v_sum = sum([int(x, 16) for x in viral.split()])
    a_sum = sum([int(x,  2) for x in  anti.split()])

    return 'True' if a_sum >= v_sum else 'False'


if __name__ == "__main__":

    lines_out = []

    for line in open(sys.argv[1], 'r'):
        lines_out.append(testLine(line.strip()))

    print '\n'.join(lines_out)
    sys.stdout.flush()
