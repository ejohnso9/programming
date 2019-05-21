#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #9 (STACK IMPLEMENTATION)
https://www.codeeval.com/open_challenges/NN/

AUTHOR: Erik Johnson
DATE: 2016-Jun-02

DISCUSSION
    Maybe a problem such as this graduates from "easy" to "moderate"
    under a language like C, but under Python this still rates
    "trivial".
"""


if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        s = line.rstrip()
        l = list(reversed(s.split()))
        lines_out.append(' '.join(l[::2]))

    print '\n'.join(lines_out)
    sys.stdout.flush()
