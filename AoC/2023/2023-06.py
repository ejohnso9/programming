#!/usr/bin/env python
# file: AoC2023Day6.ipynb

"""
https://adventofcode.com/2023/day/6
"""

from math import prod

# GLOBAL DATA
NL = '\n'

# my AoC 2023 Day 6 input
data = """
Time:        45     97     72     95
Distance:   305   1062   1110   1695
"""

# parse input data into a usable data structure
values = []
for line in data.split(NL)[1:-1]:
    ints = [int(w) for w in line.split()[1:]]
    values.append(ints)


def n_ways(secs: int, record: int) -> int:
    """How many different ways can boat win in this 'secs'-long race?"""

    # 0 can never win
    count = 0
    for i in range(1, secs):
        t = i * (secs - i)
        if t > record:
            count += 1

    return count


ts = []
for t, record in zip(values[0], values[1]):
    ts.append(n_ways(t, record))

print(f'product is: {prod(ts)}')
