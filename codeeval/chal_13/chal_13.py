#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #13  (REMOVE CHARACTERS)
https://www.codeeval.com/open_challenges/13/

AUTHOR: Erik Johnson

DISCUSSION:
"""

def f(n):
    """documentation"""
    # func body

    return None


if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        (words, find) = [s.strip() for s in line.split(',')]
        for c in find:
            words = words.replace(c, '')

        print words

