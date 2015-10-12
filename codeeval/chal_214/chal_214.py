#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #214 (TIME TO EAT)
https://www.codeeval.com/open_challenges/214/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        lol = []
        for time in line.split():
            l = [int(s) for s in time.split(':')]
            l.append(time)
            lol.append(l)

        lol.sort()
        l2 = [e[3] for e in lol]
        l2.reverse()
        lines_out.append(' '.join(l2))

    print '\n'.join(lines_out)
