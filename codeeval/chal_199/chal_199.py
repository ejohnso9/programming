#!/usr/bin/env python

import sys, math

"""
Solution for codeeval challenge #199  (STRING MASK)
https://www.codeeval.com/open_challenges/199/

AUTHOR: Erik Johnson

DISCUSSION:

hello 11001
world 10000
cba 111
"""


if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        l = []
        word, bits = line.split()
        for i, c in enumerate(word):
            if int(bits[i]):
                c2 = c.upper()
            else:
                c2 = c
            l.append(c2)
        
        lines_out.append(''.join(l))

    print '\n'.join(lines_out)
