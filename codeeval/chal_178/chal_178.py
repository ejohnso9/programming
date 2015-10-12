#!/usr/bin/env python

import sys, math

"""
Solution for codeeval challenge #178  (MATRIX ROTATION)
https://www.codeeval.com/open_challenges/178/

AUTHOR: Erik Johnson

DISCUSSION:
    Let's not even make a 2d anything out of the data - you just need to get the
    list indices to come out correctly, and that's not that tough.


a b c d
a b c d e f g h i j k l m n o p
a b c d e f g h i
"""


if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        l = [s.strip() for s in line.split(' ')]
        n = int(math.sqrt(len(l)))
        l2 = []
        for col in xrange(n):
            for row in xrange(n - 1, -1, -1):
                i = row * n + col
                l2.append(l[i])

        lines_out.append(' '.join(l2))

    print '\n'.join(lines_out)
