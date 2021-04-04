#!/usr/bin/env python
# Python 3 (dev under Python 3.6.1)

"""
2019Apr22

https://open.kattis.com/problems/parsinghex

REFERENCE:
    https://www.geeksforgeeks.org/maximum-area-quadrilateral/

    Brahmagupta's Formula:
        p2 = (a + b + c + d) / 2.0 # semi-perimeter
        maxArea = sqrt((p2 - a) * (p2 - b) * (p2 - c) * (p2 - d))
"""

import sys, math

def maxArea(a, b, c, d):
    # Brahmagupta's Formula:
    p2 = (a + b + c + d) / 2.0 # semi-perimeter
    return math.sqrt((p2 - a) * (p2 - b) * (p2 - c) * (p2 - d))

# main
args = [int(x) for x in sys.stdin.readline().split()]
print(maxArea(*args))
