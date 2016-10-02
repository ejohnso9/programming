#!/usr/bin/env python
"""
Solution for CodeEval challenge #NN (NAME)
https://www.codeeval.com/open_challenges/NN/

AUTHOR: Erik Johnson
DATE: 2016-Oct-02

DISCUSSION:
"""

import sys

def f(line):
    """outputs value for input line"""

    # do something useful here

    return line


if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        lines_out.append(f(line))

    print '\n'.join(lines_out)
    sys.stdout.flush()
