#!/usr/bin/env python

import sys
from math import sqrt

"""
Solution for codeeval challenge #98 (POINT IN CIRCLE)
https://www.codeeval.com/open_challenges/98/

AUTHOR: Erik Johnson
DATE: 2015-MAR-02

DISCUSSION:
    Simple math and input parsing. Not much else to say.
"""

if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        parts = line.strip().split(';')
        (c, r, p) = [eval(s[s.find(':') + 1:]) for s in parts]
        dx = c[0] - p[0]
        dy = c[1] - p[1]
        d = sqrt(dx * dx + dy * dy)
        print "true" if d < r else "false"

