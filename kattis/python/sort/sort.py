#!/usr/bin/env python3

"""
DESCRIPTION
    https://open.kattis.com/contests/x4dmg8/problems/sort

AUTHOR
    Erik Johnson

HISTORY
    2020Dec19  Created
"""

import sys


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


def process(ints_l):
    index_d = {}
    count_d = {}
    for idx, i in enumerate(ints_l):
        if i in count_d:
            count_d[i] += 1
        else:
            count_d[i] = 1

        # keep track of where i first appeared
        if i not in index_d:
            index_d[i] = idx

    op_l = []  # output list of ints
    l = [(count, i) for i, count in count_d.items()]
    l.sort()  # stable wrt to duplicate values
    l.reverse()  # biggest count values first
    while l:
        # remove N elements w/ same count value, sort those dups
        # by index value
        dup_l = pop_dups(l)  # (count, val) tuples w/ same count
        count = dup_l[0][0]
        l2 = [(index_d[val], val) for count, val in dup_l]
        l2.sort()
        for idx, val in  l2:
            op_l.extend(count * [val])

    return op_l


def output(ints_l):
    print(' '.join([str(el) for el in ints_l]))


def main():
    fd = sys.stdin
    ignore = fd.readline()
    line = fd.readline().strip()
    ints_l = [int(s) for s in line.split()]
    ints_l = process(ints_l)
    output(ints_l)


if __name__ == '__main__':
    main()

