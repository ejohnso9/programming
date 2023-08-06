#!/usr/bin/env python 

"""
Advent of Code solution for Problem #1 (first part)

IDEAS:
    1) Develop a Python or other library of functions for doing typical things
        the need to get done in A0C, ProjectEuler, etc. type problems. (The idea
        being, with such a library, you should be able to get through a typical problem
        by leveraging functional code to do typical sorts of things, like find the min
        or max value of some function over some data set, etc.)
    2) Take some small set of these AoC problems and solve them in a smattering of languages
        and look at performance:
        - Python
        - F#
        - C#
        - Lua
        - C
        - JS (in browser page directly, via Node on CLI)
        - JS leveraging GPU
        - Scheme
        - maybes:
            - TypeScript
            - Erlang
            - APL, J

        use Python to drive commands as separate processes to get answers
        Actually, probably what we want are launched processes that can be communicated with
        via socket and passed data so that I can "eliminate" timing all the launching process
        (i.e., I really want to mainly time computing of the problem in each environment.)

        Separately, it may also be interesting to look at separate processes:
            - per run (this would probably tend to make Python look bad, versus timing 1000 runs
                of the problem in 1 Python process.) If you are invoking 1 process how does
                Node, Python, F#, Erlang etc. stack up to each other (i.e., look at overhead of
                interpreter start vs. just code computation.)

HISTORY
    2023Aug06  ej  created
"""

FILENAME = "2022-01a.input.txt"


# convert a line of text into the one int for the line, else None value if that won't parse
def intOrNone(line):
    try:
        return int(line)
    except ValueError:
        return None


def getCaloriesEachElf(lines):
    lsOfInts = [intOrNone(line) for line in lines]
    acc_loi = list()  # calories of each else
    totalCals = 0  # sum of calories for one elf
    for index, value_i in enumerate(lsOfInts):
        # when we hit None, add another sum on the list and start new sum
        if value_i is None:
            acc_loi.append(totalCals)
            totalCals = 0  # sum of calories for one elf
        else:
            totalCals += value_i

    return acc_loi  # total calories for each elf


def processLines(lines):
    caloriesEachElf = getCaloriesEachElf(lines)
    return max(caloriesEachElf)


def main():
    with open(FILENAME, 'r') as fd:
        lines = fd.readlines()

    # print the top elf's total calories
    maxCals = processLines(lines)
    print(f"2022P1: Part 1: top elf total cal: {maxCals}")  # 68787 submitted and accepted on 2023Aug06

    # print the total calories of the top 3 elves
    sortedTotalCals = sorted(maxCals)
    print(f"2022P1: Part 2: top 3 elves total cal: {sum(sortedTotalCals[:2])}")
    #  submitted and accepted on 2023Aug06


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
