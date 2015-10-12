#!/usr/bin/env python
"""
Solution for codeeval challenge #19 (BIT POSITIONS)
https://www.codeeval.com/open_challenges/19/

AUTHOR: Erik Johnson
DATE: 2015-JUN-15

DISCUSSION:
"""

import sys

if __name__ == "__main__":

    ans_l = []
    for line in open(sys.argv[1], 'r'):
        line = line.strip()
        # NOTE: i & j are 1-based indices here!
        x, i, j = [int(n) for n in line.split(',')]
        x = int(x)
        bits = list(bin(x))

        if bits[-i] == bits[-j]:
            ans_l.append('true')
        else:
            ans_l.append('false')


    # print all the output in 1 call
    print '\n'.join(ans_l)

