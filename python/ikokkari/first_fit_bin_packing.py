#!/usr/bin/env python
# file: first_fit_bin_packing.py
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 textwidth=100:


"""
DESCRIPTION:
    module for 1 function: first_fit_bin_packing()


AUTHOR:
    Erik Johnson: ejohnso9@earthlink.net

HISTORY
    2026Oct08 
"""


# --------------------------------------------------------------------------------------------------
# Problem Set #2:  
# https://github.com/ikokkari/PythonProblems/blob/main/Additional%20Python%20Problems.pdf
# --------------------------------------------------------------------------------------------------
    
# 14. First fit bin packing
def first_fit_bin_packing(items: list[int], capacity: int) -> list[int]:
    """
    return list of bins (each element is total of items held in that bin)
    """

    bins: list[int] = [items[0]]  # init: first item has to go in a bin
    for item in items[1:]:
        fit = False  # did the item fit into one of the existing bins?
        for i, bin_tot in enumerate(bins):
            if item <= capacity - bin_tot:
                bins[i] += item
                fit = True
                break

        if not fit:
            bins.append(item)

    return bins


# ENTRY POINT
if __name__ == '__main__':

    # This module just defines this one function and test data for it

    # TEST DATA (from the problem statement)
    TEST_DATA = [
        # Items, capacity, expected_result
        ([3, 2, 3], 7, [5, 3]),
        ([8, 6, 1, 9, 7], 9, [9, 6, 9, 7]),
        ([9, 10, 6, 1, 4], 13, [10, 10, 10]),
        ([11, 8, 3, 14, 10, 13, 14], 17, [14, 8, 14, 10, 13, 14]),
        ([18, 12, 6, 10, 2, 3, 4, 17, 7], 53, [51, 28]),
    ]

    f = first_fit_bin_packing  # the function under test
    for item_ls, cap, exp in TEST_DATA:
        assert f(item_ls, cap) == exp

# EOF
