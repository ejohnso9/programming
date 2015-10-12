#!/usr/bin/env python

import sys
from math import ceil, log

"""
Solution for codeeval challenge #27 (DECIMAL TO BINARY)
https://www.codeeval.com/open_challenges/27/

AUTHOR: Erik Johnson

DISCUSSION:
    Not much to discuss here, really.
"""

if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        n = int(line.strip())
        if n == 0:
            print "0"
        else:
            p = max(2, int(ceil(log(n, 2))))
            l = [int((n & 2**i) > 0) for i in xrange(p)]
            l.reverse()
            print ''.join([str(i) for i in l])

