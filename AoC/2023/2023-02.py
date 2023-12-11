#!/usr/bin/env python
#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# run on pythonanywhere.com @ Python version 3.9.5

r"""
Solution for: https://adventofcode.com/2023/day/2

DISCUSSION
    Nearly trivial: just some simple text parsing and a little bit 
    of aggregration.

STRATEGY
    N/A

# NB: I'm not playing code golf here (though documentation may be
# somewhat lacking). This is basically the way I write production code.
"""



# Standard Python Library
import string
import sys


# GLOBAL DATA
NL = '\n'
INPUT_FILENAME = "2023-02.txt"

COLOR_MAP = {
    'red': 0,
    'green': 1,
    'blue': 2,
}


def parse_line(line):
    """
    Parse an input line and return data in the form:
        (game_num, [(R,G,B), ...])
        where:
            game_num: the int game index
            the second tuple value is a list
            (R,G,B) is a triple of int values for (red, green, blue)
    """

    data_ls = []

    def parse_part(part):
        ls = [0, 0, 0]
        for word2 in part.split(','):
            count_s, color = word2.split()
            for map_color, index in COLOR_MAP.items():
                if color == map_color:
                    ls[index] = int(count_s)

        return tuple(ls)

    idx = line.index(':')
    game_num = int(line[:idx].split()[1])
    for part in line[idx + 1:].split(';'):
        data_ls.append(parse_part(part))

    return game_num, data_ls



# Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red
def load_lines():
    """
    a simple helper to read the input file, return a list of
    strings as lines (stripped on end, but unchanged at front)
    """

    if len(sys.argv) > 1:
        # NB!!!: this is 0 only within VSCode (would normally be 1)
        filename = sys.argv[0] 
    else:
        filename = INPUT_FILENAME

    with open(filename, 'r') as fd:
        lines = [line.rstrip() for line in fd.readlines()]

    return lines


def build_max_list(games: list) -> list:
    """
    Convert the list of all the game data into one 3-tuple of the max values
    seen each game. So, the return list is one flat list of 3-tuples, indexed
    by natural C-array indices (i.e., Game 1, from line 1 in the text file has
    its max tuple first in the list (at Python index=0)).
    """

    rv_ls = list()
    for game_num, data_ls in games:
        maxes = [0] * 3
        for i in range(3):
            maxes[i] = max([t[i] for t in data_ls])
        rv_ls.append(tuple(maxes))

    return rv_ls


def is_valid_game(game_t, max_t):
    return all([game_t[i] <= max_t[i] for i in range(3)])


def main():

    # read the data file
    lines = load_lines()
    print(f"loaded {len(lines)} lines")

    # get lines parsed and data settled
    data = [parse_line(line) for line in lines]

    # build a new list of 3-tuples: (R,G,B) maxes for each game
    maxes_ls = build_max_list(data)

    # then find what are valid games for only: (12, 13, 14) cubes
    max_t = (12, 13, 14)
    valid_game_nums = [i + 1 for i, game_t in enumerate(maxes_ls)
                       if is_valid_game(game_t, max_t)]

    print(sum(valid_game_nums))  # 2716 accepted 2023Dec10T18:30

    return 0  # normal exit code


# ENTRY POINT
if __name__ == '__main__':
    rc = main()
    print(f"exit({rc})")

# EOF
