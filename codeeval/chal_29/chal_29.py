#!/usr/bin/env python

import sys, re, string

"""
Solution for codeeval challenge #29 (UNIQUE ELEMENTS)
https://www.codeeval.com/open_challenges/29/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":
    lines_out = []
    for line in open(sys.argv[1], 'r'):
        ints_l = line.strip().split(',')
        last = ints_l[0]
        l = [last]

        for i in ints_l[1:]:
            if i != last:
                l.append(i)
                last = i

        lines_out.append(','.join(l))

    print '\n'.join(lines_out)
