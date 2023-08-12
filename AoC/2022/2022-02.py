#!/usr/bin/env python 

"""
Advent of Code solution for Day 2: Rock, Paper, Scissors (RPS)
https://adventofcode.com/2022/day/2

THOUGHTS/IDEAS/DISCUSSION:
    There are basically 3 different inputs for opponent selection, 3 for mine.
    This is the cross product of 3: 3 x 3 == 9 possible combinations.
    Processing a line at a time, decomposing the textual input into:
    (opponent input, my input), then defining a function that determines a win
    from those two inputs, maps my selection to a value and maps the games result
    to a value and returning the sum of those two makes a great deal of sense from a functional
    decomposition approach. However, with only 9 input combinations, a straightforward, simple,
    efficient approach is to just do the "computation" of each input by hand, and map strings such
    as ["A X", "B Z", ...] directly to an input computed by hand.

    One mapping per line gives an int value, then we can take sum(), max() etc. of a list of ints.
    (i.e., programming the KISS method)

HISTORY
    2023Aug06  ej  created
"""

# GLOBAL DATA
FILENAME = "2022-02a.input.txt"
PROBLEM = "Aoc 2022 Day 2, part "


def f_part1Value(line: str) -> int:
    """
    my selection of (rock, paper, scissors) values: (1, 2, 3)
    challenge outcome maps (lose, draw, win): to (0, 3, 6)
    """
    val_map = {
        # opponent rock
        "A X":  1 + 3, # rock vs. rock: draw
        "A Y":  2 + 6, # rock loses to paper: I win
        "A Z":  3 + 0, # rock beats scissors: I lose

        # opponent paper
        "B X":  1 + 0, # paper vs. rock: I lose
        "B Y":  2 + 3, # paper vs. paper: draw
        "B Z":  3 + 6, # paper loses to scissors: I win

        # opponent scissors
        "C X":  1 + 6, # scissors loses to rock: I win
        "C Y":  2 + 0, # scissors beats paper: I lose
        "C Z":  3 + 3, # scissors vs. scissors: draw 
    }

    return val_map[line.strip()]


def f_part2Value(line: str) -> int:
    """
    first column: opponent selection
    2nd column: needed challenge outcome: (lose, draw, win): (0, 3, 6)

    my selection of (rock, paper, scissors) values: (1, 2, 3)
    """
    val_map = {
        # opponent rock
        "A X":  0 + 3,  # lose: I play scissors
        "A Y":  3 + 1,  # draw: I play rock
        "A Z":  6 + 2,  #  win: I play paper

        # opponent paper
        "B X":  0 + 1,  # lose: I play rock
        "B Y":  3 + 2,  # draw: I play paper
        "B Z":  6 + 3,  #  win: I play scissors

        # opponent scissors
        "C X":  0 + 2,  # lose: I play paper
        "C Y":  3 + 3,  # draw: I play scissors
        "C Z":  6 + 1,  #  win: I play rock
    }

    return val_map[line.strip()]


def main():
    with open(FILENAME, 'r') as fd:
        lines = fd.readlines()

    # Part 1: my total RPS score
    f_value = f_part1Value
    p1_total = sum([f_value(line) for line in lines])
    print(f"{PROBLEM} 1: my total RPS score: {p1_total}")
    # 14297 submitted and accepted 2023Aug06

    # Part 2: The basic functional pattern remains the same: we are still aggregating a value function
    #   over all the lines of input. Just need a new function to remap input to value.
    f_value = f_part2Value
    p2_total = sum([f_value(line) for line in lines])
    print(f"{PROBLEM} 2: my total RPS score: {p2_total}")
    # 10498 submitted and accepted on 2023Aug06


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
