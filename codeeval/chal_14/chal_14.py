#!/usr/bin/env python
"""
Solution for codeeval challenge #19 (BIT POSITIONS)
https://www.codeeval.com/open_challenges/19/

AUTHOR: Erik Johnson
DATE: 2015-JUN-15

DISCUSSION:
"""

import sys
from itertools import permutations

if __name__ == "__main__":

    ans_l = []
    fd = open(sys.argv[1], 'r')

    for line in fd.readlines():
        s = line.strip()
        iterator = permutations(s)
        s_l = [''.join(t) for t in list(iterator)]
        s_l.sort()
        ans_l.append(','.join(s_l))

    fd.close()
    print '\n'.join(ans_l)

