#!/usr/bin/env python

import sys

"""
TEMPLATE
Solution for codeeval challenge #161 (GAME OF LIFE)
https://www.codeeval.com/open_challenges/161/

AUTHOR: Erik Johnson
DATE: 2016-Sep-30
"""

N = 10

# compute number of adjacent neighbors
def n_adj(g, r, c):

    if c > 0 and c < N - 1:
        # inside column
        if r > 0 and r < N - 1:
            # inside row & col
        else:
            # top or bottom row
            if r == 0:
                l = [ g[
    else: 
        # left or right column
        if r == 0: # top row
            if c == 0: # UL corner
                l = [ g[1][0], g[1][1], g[0][1] ]
            else: # UR corner
                l = [ g[0][N-2], g[1][N-2], g[1][N-1] ]
        else: # bottom row
            if c == 0: # LL corner
                l = [ g[N-2][0], g[N-2][1], g[N-1][1] ]
            else: # LR corner
                l = [ g[N-1][N-2], g[N-2][N-2], g[N-2][N-1] ]

    return sum(l)

# create new grid (lol) given the current one
def next_gen(cur_gen):
    new_gen = [[0] * N] * N

    for r in range(N):
        for c in range(N):
            new_gen[r][c] = life(n_adj(cur_gen, r, c))

    return new_gen

# map initial cell chars to int
f = lambda c: 1 if c == '*' else 0

# the basic life rules
life = labmda n: 1 if (n == 2 or n == 3) else 0

if __name__ == "__main__":
    lines_out = []
    lol = [] # list of lists of (0, 1) ints
    for line in open(sys.argv[1], 'r'):
        lol.append(map(f, list(line.rstrip())))

    # lines_out.append("%s %s" % (i, p))

    for row in lol:
        print row
    # print '\n'.join(lines_out)
    sys.stdout.flush()
