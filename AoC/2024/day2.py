#!/usr/bin/env python
"""
"""

import sys


# GLOBAL DATA
EXIT_SUCCESS = 0
filename = 'day2.input.txt'


def isSafe(i_ls: list) -> bool:
    if i_ls[0] == i_ls[1]:
        return False

    n = len(i_ls)
    if i_ls[0] < i_ls[1]:
        # increasing
        diffs = [i_ls[i + 1] - i_ls[i] for i in range(n - 1)]
    else:
        # decreasing
        diffs = [i_ls[i] - i_ls[i + 1] for i in range(n - 1)]

    return max(diffs) <= 3 and min(diffs) > 0


def isSafe2(i_ls: list, idx: int) -> bool:
    """
    Evaluation of a list of ints for whether it is safe under the modified rules.
    """

    incs, decs, errs = 0, 0, 0
    for i in range(len(i_ls) - 1):
        diff = i_ls[i + 1] - i_ls[i]
        if diff > 0 and diff <= 3:
            incs += 1
        elif diff < 0 and diff >= -3:
            decs += 1
        else:
            errs += 1

    if errs > 1:
        tf = False
    elif incs > 1:
        tf = errs == 0 and decs <= 1 or errs == 1 and decs == 0
    elif decs > 1:
        tf = errs == 0 and incs <= 1 or errs == 1 and incs == 0

    print(idx, ':', (incs, decs, errs), i_ls, tf)

    return tf


def main(lines: list, part: int) -> int:

    # Part 1
    if part == 1:
        count = 0
        for i, line in enumerate(lines):
            try:
                ls = [int(w) for w in line.strip().split()]
                if isSafe(ls):
                    count += 1
            except ValueError as ve_x:
                print(f"ValueError at i={i}")

        # Yay!!! First run: 524 accepted 2024Dec27 12:06AM
        print(f"Part 1 count is: {count}")

    # Part 2
    count = 0
    for i, line in enumerate(lines):
        ls = [int(w) for w in line.strip().split()]
        if isSafe2(ls, i):
            count += 1

        # DEBUG STOP
        if i > 20:
            sys.exit(-1)

    # 570 is too high
    print(f"Part 2 count is: {count}")

    return EXIT_SUCCESS


if __name__ == '__main__':
    with open(filename, 'r') as fd:
        lines = fd.readlines()
    print(f"read {len(lines)} lines from '{filename}'")

    rc = main(lines, part=2)
    sys.exit(rc)

# EOF
