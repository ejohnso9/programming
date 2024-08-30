#!/usr/bin/env python
#        1         2         3         4         5         6         7         8         9         0         1         2
#23456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
# run on pythonanywhere.com @ Python version 3.9.5

r"""
https://docs.python.org/3/library/html.parser.html#module-html.parser
Solution for: https://adventofcode.com/2023/day/5

DISCUSSION
    I'm starting this problem mid July 2024, about half a year after the
contest started. By now, I'm sure there are plenty of solutions out on
the internet. I even saw a step-by-step walkthrough of one of the
problems when I was simply trying to use Google to get back to my last
problem statement.

    You either believe I am doing my own work or you don't. I attest
that I am. My solution may look like other's solutions. My var names and
coding style are unique, but the general approach about how to attack a
problem is generally not going to be: smart people are going to tend to
generally do things in a similar way. You give several thousand smart
people the same problem, there's likely going to be a relatively small
number of general approaches.

    Since I'm in no hurry, I am basically writing code the same as I do
for production for an employer. That is, properly documented, properly
commented, well-organized with meaningful var and function names, etc.
If I were trying to tear through this on Christmas Eve or day, trying to
desperately be in the first 100, that would all be skipped.

    Python is a dynamically-typed language. Yet adding type hints is a
form of documentation: it aids understandability for anyone else that
might have to understand (maintain) my code.


My solution is going to be implemented around 2 core functions:

1) getMapRow(ip: int) -> tuple[int]
   given a map (represented as a list of tuples) and an input return
   the index of the map row to use for that input (or None if we
   need to use the default "mapping" (i.e., input value is returned
   unchanged).

2) mapInput(x_i: int, row_tuple: tuple[int]) -> int
   That is, given an applicable row from some map, convert int x into the
   mapped value (which will be x_i (unchanged) in the case row_tuple is
   None).

I'll make a 3rd function, mapSeed() that uses the two above to convert a
seed to a location in one swell foop (plus some supporting functions to
get data loaded up in a form ready for the core functions to use).


STRATEGY
    I can see from reading the input file that it's not all that big.
    The maps are given in a logical order:
        seed -> soil
        soil -> fertilizer
        fertilizer -> water
        ...
        humidity -> location

    If I load a list of maps, I can map seed -> location by iterating
over the list and applying my two core functions, building up a list of
(seed, location) values.

    The question is phrased as:

    "What is the lowest location number that corresponds to any of the
    initial seed numbers?"

    My understanding is that, because of this instruction:

    "Any source numbers that aren't mapped correspond to the same
    destination number."

    ...every seed is going to map to some location. I could simply build
up a list of seed locations and take min() of that, but as a matter of
general principle and programming style, I would first build a list of
(seed, location) tuples, then just extract the minimal location value.
"""


# Standard Python Library
from common import load_lines
from pathlib import Path
import pdb  # https://pymotw.com/2/pdb/
import sys


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-05.input.txt"
# INPUT_FILENAME = "2023-05_sample.txt"


def loadSeeds(lines: list[str]) -> list[int]:
    """Just extract the seed values a list of ints"""
    for line in lines:
        if line.startswith('seeds:'):
            line = line[6:]
            seeds = [int(w) for w in line.split()]
            break

    return seeds


def loadDicts(lines: list[str]) -> list[tuple]:
    """
    I know dict definitions start on line 2
    """

    lol_tuples = []
    ls = None

    for line in lines[2:]:
        line_s = line.strip()
        # blank line at end of map
        if not len(line_s):
            continue
        elif line_s.endswith('map:'):
            # start new map
            if ls:
                lol_tuples.append(ls)
            ls = []
        else:
            loi = [int(w) for w in line_s.split()]
            ls.append(tuple(loi))

    # we may be missing a final blank line to cause the last list to get appended
    if ls:
        lol_tuples.append(ls)

    return lol_tuples


def findMapRow(value: int, map: list):
    """
    Given one particular map and a value, return the applicable map tuple
    or None if no map row was applicable.
    """

    for i, tup in enumerate(map):
        dest, src, width = tup
        if src <= value <= src + width:
            return tup

    return None


def mapInput(value: int, map_tuple):
    if not map_tuple:
        return value

    dest, src, width = map_tuple
    offset = value - src

    return dest + offset


def mapSeed(seedValue: int, maps: list) -> int:
    """
    Given a starting seed value, map it through all the maps
    """

    value = seedValue
    for map in maps:
        tup = findMapRow(value, map)
        value = mapInput(value, tup) if tup else value

    return value


def main(input_file: Path):

    # read the input data file, process it
    lines = load_lines(input_file)
    seeds: list[int] = loadSeeds(lines)
    print(seeds)
    maps = loadDicts(lines)

    # do all the mapping, generating (seed, location) tuples
    data = [(seed, mapSeed(seed, maps)) for seed in seeds]
    sorted_data = sorted(data, key=lambda t: t[1])
    seed, location = sorted_data[0]
    print(f"seed: {seed} at location: {location}")
    # BINGO!!! First try: location: 486613012

    sys.exit()

    ls_of_dicts = load_dicts(lines)

    print(f"loaded {len(lines)} lines")


    # Part 1:
    # pdb.set_trace()
    # print(len(match_counts))
    TODO = "TODO"
    print(f"Part 1: {TODO}")  # <TODO> accepted on <when?>

    # Part 2:
    # print(f'Part 2: {TODO}')  # <TODO> accepted on <when?>

    return 0  # main() normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main(Path(INPUT_FILENAME))
    print(f"exit({rc}).")

# EOF

