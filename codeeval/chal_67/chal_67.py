#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #NN  (NAME)
https://www.codeeval.com/open_challenges/NN/

AUTHOR: Erik Johnson

DISCUSSION:
"""

d = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
      '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15 }

if __name__ == "__main__":

    op = []
    for s in open(sys.argv[1], 'r'):
        i = len(s[:-1])
        n = 0
        for c in s[:-1]:
            n += d[c] * 16 ** (i-1)
            i -= 1
        op.append(str(n))

    print '\n'.join(op)
