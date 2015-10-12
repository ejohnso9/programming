#!/usr/bin/env python

import sys, os

"""
Solution for codeeval challenge #20 (LOWERCASE)
https://www.codeeval.com/open_challenges/20/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":
    for line in open(sys.argv[1], 'r'):
        line = line.strip()
        print line.lower()
