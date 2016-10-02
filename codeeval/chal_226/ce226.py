#!/usr/bin/env python
"""
Solution for CodeEval challenge #226 (TRY TO SOLVE IT)
https://www.codeeval.com/open_challenges/226/

AUTHOR: Erik Johnson
DATE: 2016-Oct-02

DISCUSSION:
    Once you take the hint and put Python's string.translate() function to work,
    this problem becomes trivial.
"""

import sys
import string

XLATE = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "uvwxyznopqrstghijklmabcdef" )



if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        line = line.rstrip()
        lines_out.append(line.translate(XLATE))

    print '\n'.join(lines_out)
    sys.stdout.flush()
