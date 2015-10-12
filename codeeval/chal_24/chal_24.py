#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #24 (SUM OF INTEGERS FROM FILE)
https://www.codeeval.com/open_challenges/24/

AUTHOR: Erik Johnson

DISCUSSION:
"""

if __name__ == "__main__":
    lines_out = []
    lines = open(sys.argv[1], 'r').readlines()
    lines_out.append(str(sum([int(s) for s in lines])))
    print '\n'.join(lines_out)
