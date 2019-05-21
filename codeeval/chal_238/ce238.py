#!/usr/bin/env python
"""
Solution for CodeEval challenge #238 (CODE COMBINATIONS)
https://www.codeeval.com/open_challenges/238/

AUTHOR: Erik Johnson
DATE: 2016-Oct-02

DISCUSSION:
    Most of these "moderate" challenges are really more like "easy".
"""

import sys

def compute_line(line):
    """outputs value for input line"""

    n = 0

    # build "grid", 'g': a list of lists
    g = [list(s.strip()) for s in line.strip().split('|')]
    n_rows = len(g)
    n_cols = len(g[0])

    for r in xrange(n_rows - 1):
        for c in xrange(n_cols - 1):
            l = [g[r][c], g[r][c+1], g[r+1][c], g[r+1][c+1]]
            if ''.join(sorted(l)) == 'cdeo':
                n += 1
            
    return str(n)


if __name__ == "__main__":
    lines_out = []

    for line in open(sys.argv[1], 'r'):
        lines_out.append(compute_line(line))

    print '\n'.join(lines_out)
    sys.stdout.flush()
