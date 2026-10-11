#!/usr/bin/env python
# file: count_unicolour_rectangles.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:


"""
DESCRIPTION:
    module for 1 function: count_unicolour_rectangles()


AUTHOR:
    Erik Johnson: ejohnso9@earthlink.net

HISTORY
    2026Oct10 Created
"""


# --------------------------------------------------------------------------------------------------
# Problem Set #2:  
# https://github.com/ikokkari/PythonProblems/blob/main/Additional%20Python%20Problems.pdf
# --------------------------------------------------------------------------------------------------
    
# 22. Count monochromatic rectangles (NB: naming discrepancy here)
def count_unicolour_rectangles(grid: list[str]) -> int:
    """
    Count of how many rectilinear rectangles have all 4 corners same color.
    """

    count: int = 0
    nrows, ncols = len(grid), len(grid[0])  # width, height

    # scan upper left corners from (0, 0) to (nrows - 1, ncols - 1)
    for r1 in range(nrows - 1):
        for c1 in range(ncols - 1):
            color = grid[r1][c1]  # color @ UL corner

            # scan down for row below UL corner w/ same color
            for r2 in range(r1 + 1, nrows):
                if grid[r2][c1] != color:
                    continue

                # scan to right for cols w/ same color
                for c2 in range(c1 + 1, ncols):
                    if grid[r1][c2] != color:
                        continue

                    # now, cell at: (r2, c2) either matches other 3 corners or not
                    if grid[r2][c2] == color:
                        count += 1
                        # print(f"({r1}, {c1}), ({r2}, {c1}), ({r1}, {c2}), ({r2}, {c2})")

    return count


# ENTRY POINT
if __name__ == '__main__':

    # This module just defines one function (and tests 2nd example).

    # TEST DATA (from the problem statement)
    TEST_DATA = [
        # grid 1: count = 1
        (['aba',
          'ccc',
          'ada'], 1),

        # grid 2: count = 5
        (['bbbbccba',
          'cdacaabc',
          'acdcdcdc',
          'cddacdab',
          'cbaaaabd'], 5),
    ]

    f = count_unicolour_rectangles  # the function under test
    grid, exp = (TEST_DATA[1][i] for i in (0, 1))
    assert f(grid) == exp

# EOF
