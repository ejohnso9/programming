#!/usr/bin/env python
"""
Solution for CodeEval challenge #161 (GAME OF LIFE)
https://www.codeeval.com/open_challenges/161/

AUTHOR: Erik Johnson
DATE: 2016-Oct-02
"""

import sys

N = 10

# compute number of adjacent neighbors
def n_adj(g, r, c):

    # top, middle, bottom row index
    t, m, b = r - 1, r, r + 1

    # inside column
    if c > 0 and c < N - 1:
        # inside row & col
        if r > 0 and r < N - 1:
            l = [
                g[t][c-1], g[t][c], g[t][c+1],
                g[m][c-1],          g[m][c+1],
                g[b][c-1], g[b][c], g[b][c+1],
            ]

        # top or bottom row
        else:
            # top row
            if r == 0:
                l = [
                    g[m][c-1],          g[m][c+1],
                    g[b][c-1], g[b][c], g[b][c+1],
                ]
            # bottom row
            else:
                # t, m = N - 2, N - 1
                l = [
                    g[t][c-1], g[t][c], g[t][c+1],
                    g[m][c-1],          g[m][c+1],
                ]

    # left or right column
    else: 

        # left column
        if c == 0:
            if r == 0: # UL corner
                l = [ g[1][0], g[1][1], g[0][1] ]
            elif r == N - 1: # LL corner
                l = [ g[t][0], g[t][1], g[m][1] ]
            else: # left side
                l = [
                    g[t][0], g[t][1],
                             g[m][1],
                    g[b][0], g[b][1],
                ]

        # right column
        else:
            if r == 0: # UR corner
                l = [ g[0][N-2], g[1][N-2], g[1][N-1] ]
            elif r == N - 1: # LR corner
                l = [ g[m][N-2], g[t][N-2], g[t][N-1] ]
            else: # right side
                t, m , b = r - 1, r, r + 1
                l = [
                    g[t][c-1], g[t][c],
                    g[m][c-1],         
                    g[b][c-1], g[b][c],
                ]

    return sum(l)


# create new grid (lol) given the current one
def next_gen(cur_gen):
    new_gen = []
    for i in range(N):
        new_gen.append([0] * N)

    for r in range(N):
        for c in range(N):
            alive = cur_gen[r][c] == 1
            n = n_adj(cur_gen, r, c)
            new_gen[r][c] = life(alive, n)

    return new_gen

# intermediate computing going directly off of 0/1 cells:
# these two funcs interchange representation
char2int = lambda c: 1 if c == '*' else 0
int2char = lambda i: '*' if i == 1 else '.'

# the basic life rules
def life(alive, n):
    if alive:
        return 1 if (n == 2 or n == 3) else 0
    else:
        return 1 if n == 3 else 0

if __name__ == "__main__":
    lines_out = []
    g0 = [] # list of lists of (0, 1) ints
    for line in open(sys.argv[1], 'r'):
        g0.append(map(char2int, list(line.rstrip())))

    # lines_out.append("%s %s" % (i, p))
    ng = g0
    for i in range(10):
        ng = next_gen(ng)

    for row in ng:
        lines_out.append(''.join(map(int2char, row)))

    print '\n'.join(lines_out)
    sys.stdout.flush()
