#!/usr/bin/env python

"""
DESCRIPTION
    solution to Kattis problem:
        https://open.kattis.com/problems/10kindsofpeople

THOUGHTS / DISCUSSION
    The solution rate on this problem is low, which is why I decided to try it.
    That probably stems from the fact that a straight recursive solution will
    eat up a bunch of memory and Python will quit (crash), even after this:

    sys.setrecursionlimit(100000)

    One can get the same effect by using a list like a data stack and
    simply iterating to process each argument put on our own "stack".

    Even using my own data structure as a stack instead of making recursive
    native function calls tends to run out of time. Next approach is to map
    regions just once using an indexed value. If the two starting coordinates
    don't have the same value, then they are in different regions. If they are
    the same, but value 0 or 1, then they are not in a mapped region and it's
    not clear whether they are in the same region or different. Mapping one of
    the two regions will then reveal whether they are in the same region or not.
    In that way, the recursive search only has to take place (at most) once per
    region (perhaps not at all).
"""

import sys
from sys import stdin


# def find(cur_row, cur_col, tgt_row, tgt_col, grid):
#     stack = list()
#     found = dict()
#     tgt_type = grid[tgt_row][tgt_col]
#     stack.append((cur_row, cur_col))  # tuple
# 
#     # helper
#     # def look(row, col):
#     #     # ignore positions passed here of other type
#     #     if grid[row][col] == tgt_type and (row, col) not in found:
#     #         found[(row, col)] = True
#     #         stack.append((row, col))

# GLOBAL DATA
NEITHER = "neither"
OUTPUT = ["binary", "decimal"]


def mapRegion(grid, start_row, start_col, regionIndex, n_rows, n_cols) -> None:
    start01 = grid[start_row][start_col]  # orig 0 or 1 value of input (row, col)
    stack = [(start_row, start_col)]

    while stack:
        row, col = stack.pop()
        grid[row][col] = regionIndex  # int we are setting this region to

        # up
        if row - 1 >= 0:
            if grid[row-1][col] == start01:
                stack.append((row-1, col))

        # right
        if col + 1 <= n_cols - 1:
            if grid[row][col+1] == start01:
                stack.append((row, col+1))

        # down
        if row + 1 <= n_rows - 1:
            if grid[row+1][col] == start01:
                stack.append((row+1, col))

        # left
        if col - 1 >= 0:
            if grid[row][col-1] == start01:
                stack.append((row, col-1))

    return  # None: done mapping the region at (start_row, start_col)

        # look around (orthogonally)
        if cur_row > 0:
            up = cur_row - 1, cur_col
            if grid[up[0]][up[1]] == tgt_type and up not in found:
                found[up] = True
                stack.append(up)

        if cur_row < n_rows - 1:
            down = cur_row + 1, cur_col
            if grid[down[0]][down[1]] == tgt_type and down not in found:
                found[down] = True
                stack.append(down)

        if cur_col > 0:
            left = cur_row, cur_col - 1
            if grid[left[0]][left[1]] == tgt_type and left not in found:
                found[left] = True
                stack.append(left)

        if cur_col < n_cols - 1:
            right = cur_row, cur_col + 1
            if grid[right[0]][right[1]] == tgt_type and right not in found:
                found[right] = True
                stack.append(right)

def output(zeroOrOne):
    print(OUTPUT[zeroOrOne])


if __name__ == '__main__':

    # fd = open('data.txt', 'r')
    # readline = fd.readline
    readline = stdin.readline

    # readline = stdin.readline
    n_rows, n_cols = [int(w) for w in readline().split()]

    # load initial grid
    grid = list()
    for i in range(n_rows):
        grid.append([int(c) for c in list(readline().strip())])

    # manage state: for all the mapped regions, keep track of whether it was originally 0 or 1
    regionList = [0, 1]  # regionList[2] will be 0 or 1 after we assign 2 to a contiguous region of 0's or 1's
    regionIndex = 1  # next call to mapRegion() will set 2's into the grid

    # iterate the query part of the input data
    for i in range(int(readline())):  # 3rd line has single int for number of following lines
        # use 0-based indices here
        r1, c1, r2, c2 = [int(w) - 1 for w in readline().split()]
        region1 = grid[r1][c1]  # region index (orig 0 | 1)
        region2 = grid[r2][c2]  # region index (orig 0 | 1)
        if region1 != region2:
            print(NEITHER)  # different values can't be same region
        else:
            # both coordinates have same index: but is that a 0/1 region or a mapped region?
            if region1 in (0, 1):
                # need to map one of the regions: that will either put the two coordinates
                # in the same (non-0/1)-region or regions having different indices
                # (NB: doesn't really matter which region is mapped: just map first region)
                regionIndex += 1
                regionList.append(region1)  # was the mapped region originally a 0 or 1 region?
                mapRegion(grid, r1, c1, regionIndex, n_rows, n_cols)

                # now, re-check the region index of the two input coords
                region1 = grid[r1][c1]  # region index (orig 0 | 1)
                region2 = grid[r2][c2]  # region index (orig 0 | 1)
                if region1 == region2:
                    # now both in newly-mapped region
                    output(regionList[region1])  # "binary" | "decimal"
                else:
                    print(NEITHER)  # can't get to (r2, c2) from (r1, c1)
            else:
                # both (r1, c1) and (r2, c2) in the same mapped region:
                # just output which kind of region it originally was
                output(regionList[region1])  # "binary" | "decimal"

# EOF
