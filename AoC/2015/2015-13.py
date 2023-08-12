#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DESCRIPTION
    https://adventofcode.com/2015/day/13

--- Day 13: Knights of the Dinner Table ---
In years past, the holiday feast with your family hasn't gone so well.
Not everyone gets along! This year, you resolve, will be different.
You're going to find the optimal seating arrangement and avoid all those
awkward conversations.

You start by writing up a list of everyone invited and the amount their
happiness would increase or decrease if they were to find themselves
sitting next to each other person. You have a circular table that will
be just big enough to fit everyone comfortably, and so each person will
have exactly two neighbors.

For example, suppose you have only four attendees planned, and you
calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness
units (because David talks so much), but David would gain 46 happiness
units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice
(Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to
Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains
41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical
scenario, you find that this one is the most optimal, with a total
change in happiness of 330.

What is the total change in happiness for the optimal seating
arrangement of the actual guest list?

--- Part Two ---
In all the commotion, you realize that you forgot to seat yourself.
At this point, you're pretty apathetic toward the whole thing, and
your happiness wouldn't really go up or down regardless of who you
sit next to. You assume everyone else would be just as ambivalent
about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships
that involve you a score of 0.

What is the total change in happiness for the optimal seatingx
 arrangement that actually includes yourself?

DISCUSSION
    Like other solutions here, we basically need two things:
        A) Something to generate the possible arrangements
        B) A function to give a value for a given arrangement

    As mentioned elsewhere, Python already has a nice permutation
    generator in itertools.permutations() - no point in re-inventing
    that wheel.

    Part 1 fell out after following my strategy immediately.
    Again, with a decent design, going from Part 1 to part 2 looks to be
    quite easy.

    Part 2 raises an interesting point. Here, we are creating
    one-time throw away programs, and so whether I make a modification
    to the valuation function to look for a special value, or whether
    I modify data may seem like it doesn't much matter one way or the
    other.

    But in practice, when you are the author of code that is already "out
    there" in the wild, so to speak - that is, exposed to other programmers
    which may already be calling functions and classes which have already
    been released, getting a new solution without having to modify code
    (i.e., by modifying input data only) (especially code which has already
    been tested and verified to give correct answers) seems like a huge win
    - the clear path to prefer.

    I didn't check Part 1 into git separately, so you can't check the file
    history, but I'm telling you that the changes that I am making for
    Part 2 a solely confined to the labelled parts within main().

STRATEGY
    * Parse the text of the seating arrangement to make a dict that gives
        values for who's sitting next to who.

    * Implement the function to evaluate a seating arrangement.

    * Use itertools.permutations() to walk over all the arrangements and
        get the max value.

"""

from itertools import permutations

# GLOBAL DATA
NL = '\n'


# my puzzle input:
DATA = """\
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 81 happiness units by sitting next to Carol.
Alice would lose 42 happiness units by sitting next to David.
Alice would gain 89 happiness units by sitting next to Eric.
Alice would lose 89 happiness units by sitting next to Frank.
Alice would gain 97 happiness units by sitting next to George.
Alice would lose 94 happiness units by sitting next to Mallory.
Bob would gain 3 happiness units by sitting next to Alice.
Bob would lose 70 happiness units by sitting next to Carol.
Bob would lose 31 happiness units by sitting next to David.
Bob would gain 72 happiness units by sitting next to Eric.
Bob would lose 25 happiness units by sitting next to Frank.
Bob would lose 95 happiness units by sitting next to George.
Bob would gain 11 happiness units by sitting next to Mallory.
Carol would lose 83 happiness units by sitting next to Alice.
Carol would gain 8 happiness units by sitting next to Bob.
Carol would gain 35 happiness units by sitting next to David.
Carol would gain 10 happiness units by sitting next to Eric.
Carol would gain 61 happiness units by sitting next to Frank.
Carol would gain 10 happiness units by sitting next to George.
Carol would gain 29 happiness units by sitting next to Mallory.
David would gain 67 happiness units by sitting next to Alice.
David would gain 25 happiness units by sitting next to Bob.
David would gain 48 happiness units by sitting next to Carol.
David would lose 65 happiness units by sitting next to Eric.
David would gain 8 happiness units by sitting next to Frank.
David would gain 84 happiness units by sitting next to George.
David would gain 9 happiness units by sitting next to Mallory.
Eric would lose 51 happiness units by sitting next to Alice.
Eric would lose 39 happiness units by sitting next to Bob.
Eric would gain 84 happiness units by sitting next to Carol.
Eric would lose 98 happiness units by sitting next to David.
Eric would lose 20 happiness units by sitting next to Frank.
Eric would lose 6 happiness units by sitting next to George.
Eric would gain 60 happiness units by sitting next to Mallory.
Frank would gain 51 happiness units by sitting next to Alice.
Frank would gain 79 happiness units by sitting next to Bob.
Frank would gain 88 happiness units by sitting next to Carol.
Frank would gain 33 happiness units by sitting next to David.
Frank would gain 43 happiness units by sitting next to Eric.
Frank would gain 77 happiness units by sitting next to George.
Frank would lose 3 happiness units by sitting next to Mallory.
George would lose 14 happiness units by sitting next to Alice.
George would lose 12 happiness units by sitting next to Bob.
George would lose 52 happiness units by sitting next to Carol.
George would gain 14 happiness units by sitting next to David.
George would lose 62 happiness units by sitting next to Eric.
George would lose 18 happiness units by sitting next to Frank.
George would lose 17 happiness units by sitting next to Mallory.
Mallory would lose 36 happiness units by sitting next to Alice.
Mallory would gain 76 happiness units by sitting next to Bob.
Mallory would lose 34 happiness units by sitting next to Carol.
Mallory would gain 37 happiness units by sitting next to David.
Mallory would gain 40 happiness units by sitting next to Eric.
Mallory would gain 18 happiness units by sitting next to Frank.
Mallory would gain 7 happiness units by sitting next to George.
"""

# from the problem statement
TEST_DATA = """\
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""


def buildSeatingDict(lines):
    d = {}
    for line in lines:
        words = line.split()
        who1 = words[0]
        who2 = words[-1]
        who2 = who2[:-1]  # strip trailing '.'
        value = int(words[3])
        if words[2] == 'lose':
            value = -value
        d[(who1, who2)] = value

    return d


def f_value(tup, seating_d):
    """valuation function for a seating arrangement"""
    # compute the value for the ends first
    val = seating_d[(tup[0], tup[-1])]
    val += seating_d[(tup[0], tup[1])]
    val += seating_d[(tup[-1], tup[-2])]
    val += seating_d[(tup[-1], tup[0])]

    # now, the rest is regular
    for i in range(1, len(tup) - 1):
        val += seating_d[(tup[i], tup[i - 1])]
        val += seating_d[(tup[i], tup[i + 1])]

    return val


def main():

    # these 3 lines are as they were for Part 1
    lines = DATA.split(NL)[:-1]
    seating_d = buildSeatingDict(lines)
    names = list(set([t[0] for t in seating_d]))

    # Part 2: add myself ('ej') into the seating arrangement...
    me = 'ej'
    for name in names:
        seating_d[(me, name)] = 0
        seating_d[(name, me)] = 0
    names.append(me)  # ...and to the 'names' list

    # now the rest is *EXACTLY* the same: no other code changes!
    max_val = -1e12
    for p in permutations(names):
        val = f_value(p, seating_d)
        if val > max_val:
            max_val = val

    print(f"max is: {max_val}")
    # 709 verified correct for Part 1 on 2022Aug02
    # 668 verified correct for Part 2 on 2022Aug02
    #   :( everybody (on average) is happier without me there


if __name__ == '__main__':
    main()

# EOF
