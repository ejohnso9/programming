#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #8 (REVERSE WORDS)
https://www.codeeval.com/open_challenges/8/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":
    for line in open(sys.argv[1], 'r'):
        words = line.split()
        words.reverse()
        print ' '.join(words)
