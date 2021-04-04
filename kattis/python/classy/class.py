#!/usr/bin/env python3

"""
DESCRIPTION
    https://open.kattis.com/contests/x4dmg8/problems/classy

AUTHOR
    Erik Johnson

HISTORY
    2020Dec20  Created
"""

import sys

# GLOBAL DATA
NL = '\n'
RANK_D = {
    'upper': 0,
    'middle': 1,
    'lower': 2,
}


def pop_dups(l):
    """
    @param l: list of (count, value) tuples
    """
    rv_l = []  # list of elements w/ same count
    while len(l) > 1 and l[0][0] == l[1][0]:
        rv_l.append(l.pop(0))  # remove a dup

    # last el w/ count same as 1st of orig arg 'l'
    rv_l.append(l.pop(0))

    return rv_l


def pad(lol):
    max_i = max([len(l[0]) for l in lol])
    # replace int rank list w/ padded list of int ranks
    for l in lol:
        ranks = l[0]  # inner list
        n = len(ranks)
        if n < max_i:
            ranks.extend((max_i - n) * [1])

    # print(f"m is: {m}")


def process(lines):
    # return processed data for 1 test case
    lol = []  # [[int_ranks, name]]
    for line in lines:
        words = line.split()
        name = words[0][:-1]
        ranks = reversed(words[1].split('-'))
        int_ranks = [RANK_D[key] for key in ranks]
        lol.append([int_ranks, name])

    pad(lol)    # make all int_rank lists same length
    lol.sort()  # by int ranks

    # sub-process duplicate ranks
    #   pop_dups() pulls elements out of arg list, 'lol'
    #     continue until 'lol' is empty
    rv_l = []  # final list of names
    while lol:
        same_ranks_l = pop_dups(lol)  # list of 1 or more
        if len(same_ranks_l) > 1:
            # sort the sub list by name
            names = [l[1] for l in same_ranks_l]
            names.sort()  # alphabetically by name
            rv_l.extend(names)
        else:
            # just tack on 1 more name
            name = same_ranks_l[0][1]
            rv_l.append(name)

    # all names this case, sorted by: (rank, name)
    return rv_l


def output(names_l):
    print(NL.join(names_l))
    print('=' * 30 + NL)


def main():
    answers = []
    fd = sys.stdin
    n_cases = int(fd.readline())
    for case_i in range(n_cases):
        n_lines = int(fd.readline())
        lines = []
        for i in range(n_lines):
            lines.append(fd.readline().strip())
        names = process(lines)
        output(names)


if __name__ == '__main__':
    main()

