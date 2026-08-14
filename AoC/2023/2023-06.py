#!/usr/bin/env python
# file: AoC2023-08.py

"""
https://adventofcode.com/2023/day/8
"""

# from math import prod
from pathlib import Path
import sys

# GLOBAL DATA
NL = '\n'

# my AoC 2023 Day 8 input
DATA_FILENAME = "2023-08.input.txt"

LR_STR = None  # init'ed in readInputFile
LR_INDEX = 0


def nextLR() -> str:
    global LR_INDEX
    lr = LR_STR[LR_INDEX]
    LR_INDEX += 1
    if LR_INDEX > len(LR_STR) - 1:
        LR_INDEX = 0

    return lr


def readInputFile(data_path: Path) -> dict:
    """
    Read the input file, build dict and list of left/right syms.

    :param filename:
    :return: LR_str, lookup dict
    """

    assert data_path.is_file()
    with open(data_path, 'r') as fd:
        lines = fd.readlines()

    global LR_STR
    LR_STR = lines[0].strip()  # "LRLRLRRRLLL..."

    # "LRV = (NNC, BHD)"  # sample line
    lookup_d = {}
    for line in lines[2:]:
        a, b, c = [line[start:start + 3] for start in (0, 7, 12)]
        lookup_d[a] = (b, c)

    # create dict

    return lookup_d


def part_one(d: dict) -> str:

    key = 'AAA'
    count = 0
    while True:
        lr = nextLR()
        node = d[key]
        key = node[0 if lr == 'L' else 1]
        count += 1
        if key == 'ZZZ':
            break

    return f"arrived on 'ZZZ' in {count} steps"
    # 19667 accepted on 2025Nov13 (first try! ;) )


def main(data_filename: str) -> int:
    d = readInputFile(Path(data_filename))
    print(part_one(d))


    return 0  # NORMAL EXIT


if __name__ == '__main__':
    rc = main(DATA_FILENAME)
    sys.exit(rc)
