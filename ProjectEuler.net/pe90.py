#!/usr/bin/env python
# file: pe90.py
# ProjectEuler.net Problem #90
# https://projecteuler.net/problem=90

r"""
PROBLEM STATEMENT

Each of the six faces on a cube has a different digit (0 to 9) written
on it; the same is done to a second cube. By placing the two cubes
side-by-side in different positions we can form a variety of 2-digit
numbers.

For example, the square number 64 could be formed:
    '6' '4'


In fact, by carefully choosing the digits on both cubes it is possible
to display all of the square numbers below one-hundred:
    [01, 04, 09, 16, 25, 36, 49, 64, 81]

For example, one way this can be achieved is by placing
    {0, 5, 6, 7, 8, 9} on one cube and
    {1, 2, 3, 4, 8, 9} on the other cube.

However, for this problem we shall allow the 6 or 9 to be turned
upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} on one cube
and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be
displayed; otherwise it would be impossible to obtain 09.

In determining a distinct arrangement we are interested in the digits on
each cube, not the order.

    {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
    {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct
sets in the last example both represent the extended set {1, 2, 3, 4, 5,
6, 9} for the purpose of forming 2-digit numbers.

How many distinct arrangements of the two cubes allow for all of the
square numbers to be displayed?


DISCUSSION
-----------
    This is a rather interesting problem and causes me to think about a
number of things, in particular the way in which these sorts of problems
sort of become a miniture model for computing / software development
issues in the real world of professional programming. 

    Sometimes, I can craft programs that will find solutions to problems
without really understanding the problem. If I understand the solution
space well enough, and if that solution space is small enough that I can
generate all possible solutions and I have a way to evaluate a potential
solution to determine if it is an actual solution, then I may be able to
simply iterate through the solution space and filter out workable
solutions.

    The key is in understanding the solution space, having an intuitive
idea about how much computing is involved to evaluate that. Sometimes, a
naieve approach like this is fine. Prefessional programming is often an
"art" of striking a "reasonable" balance between: computer time,
developer time, memory utilization, CPU utilization, file utilization,
etc.

    Sometimes "simple" by kinda dumb/unsophisticated code is preferable
to "smarter" code - that is more complex code that makes optimizations
to be more efficient, but then is necessarily more complicated to write,
understand, and maintain.  Good documentation, good variable names, good
comments, good program organization can go a long ways towards "human
understandability". That applied to both code that I create and I will
have to maintain, and code that I create that someone else may have to
read, understand, change, maintain.

    So, in this case, I am thinking about some of the optimizations that
might be made... For example, I need to be able to form the numbers:
    [01, 04, 09]

    The only possible solutions will have 0 on one of the cubes and 1 on
the other. Likewise 0 on one of the cubes and 4 on the other. 0 might be
on both cubes. It is *NOT* a requirement that 0 be on one cube and
{1, 4, 9} be together on the other. 

    I've worked with the Python module 'itertools' enough to know that
I've got some help when it comes to generating combinations and
permutations - I don't have to solve generating such things from
scratch. I also know that Python has a set type:

>>> s = {1, 2, 3}
>>> s
{1, 2, 3}
>>> type(s)
<class 'set'>
>>> {1, 2, 3} == {2, 3, 1}

I've got some additional support there.

Here's the square numbers I have to form with two cubes:
    [01, 04, 09, 16, 25, 36, 69, 64, 81] 

I notice that there is no '7'. My first thought was that I could reduce
the size of the search space by generating combinations of a set that
doesn't have 7. That seems smart. But what's the question?

    "How many distinct arrangements of the two cubes allow for all of
    the square numbers to be displayed?"

    Well... there may well be arrangements that have a 7 on one cube or
possible even both cubes that can still form all the required square
numbers? This also brings into focus the idea that a number might be
duplicated on one or both cubes and potentially more than one number.


PLANNING / DESIGN
------------------
    (All of this text is being written before even getting into trying
to write code: its the problem analysis phase).

    Given the discussion, there's some trickiness and still some "wiggle
room" in terms of trying to optimize the space of potential soluions to
try.

    One core part of my solution will be a function that simply takes
two sets of digits and evaluates whether you can form the set of
complete square numbers:
    [01, 04, 09, 16, 25, 36, 69, 64, 81] 

    The can most efficiently be some by simply having some set-testing
statements. For example:

    def testSolution(s1: set, s2: set) -> bool:
        if not (0 in s1 and 1 in s2) or (0 in s2 and 1 in s1):
            return False
        # ...
    
    Those sorts of tests can perhaps be coded in a data structure and
applied with less code, but my point here is that if two potential
solutions sets can't form 01 (taking them in either order), then
evaluation of that solution is over. There's no more code execution
needed to determine whether that's a potential solution.

    The next question is, can I generate all the potential solutions
that I need to look at? Looking at the square numbers, one potential
solution is to split cubes by the tens and ones place:

    tens: {0, 1, 2, 3, 6, 8}
    ones: {1, 4, 5, 6, 9}

That's curious: there are only five different digits in the ones place.
That means there is room to put any of the 10 digits on the sixth face
and I have a soltuion in combination with the tens set (above):
    {1, 4, 5, 6, 9, 1}
    {1, 4, 5, 6, 9, 2}
    ...,
    {1, 4, 5, 6, 9, _}
    ...,
    {1, 4, 5, 6, 9, 7}
    {1, 4, 5, 6, 9, 8}
    {1, 4, 5, 6, 9, 9}

    Moreover, this set has both a 6 and 9, which means I really only
need to include one of them and then I've got two free faces for putting
anything:
    {1, 4, 5, 6, _, _}  # all of these combinations
    {1, 4, 5, 9, _, _}  # and all of these combinations

    Only one of the square numbers end in 6, which means I don't need 6
on both cubes. But here again, I need to focus on the question. It's not
that I don't need 6 on both, but how do I define a space of possible
solutions that includes all the ones I need to count, but isn't
unnecessarily big. For example, here's some possible 2-sets:
    {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0}
    {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 1}
    {0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 2}
    ...

    I don't think that's a reasonable definition of the space I want to
check, but it's not immediately clear how to define a substantially
smaller space.

    1 and 6 are present in both 'tens' and 'ones' and I don't need to
form either 11 or 66. That seems like it may open up a "degree of
freedom" - to not have 1 and 6 in both sets.

    squares: [01, 04, 09, 16, 25, 36, 49, 64, 81] 

    The only square numbers that have to be formed with a 1 are:
        [01, 16, 81]

    If I eliminate 1 from one set, then I have to have {0, 6, 8} in the
other set. The square numbers needing a 6 are: [16, 36, 64], such that
if I eliminate 6 from one set, then I have to have {1, 3, 4} in the other
set.

    I picked this problem to tackle because it was rated at 40%...
    I'm starting to see why.

    I am thinking along the lines of trying to define a couple of
"master sets" from which to form other sets from, then letting Python
rip on iterating through generating all the 2-sets of 6 elements passing
all possible two-sets to the evaluation function.

    Probably another key fact is that nine of ten digits are used in
the square numbers. Between the two sets, it has to cover all digits
except 7. Given one set, this can be used to impose some restrictions on
the space of the other set.


    Well, I just re-read the problem and thankfully gained a simplifying
insight:

    "Each of the six faces on a cube has a different digit (0 to 9)
    written on it; the same is done to a second cube."


    Ok, that will help a lot. Actually, way more than I thought...

>>> ls = list(combs('0123456789', 6))
>>> len(ls)
210

210 squared is 44100
That's a perfectly doable number of combinations to throw against my
eval function (i.e., my test function for whether two sets can form all
the required digit combinations).


POSTMORTEM
    I had to do a fair amount of thinking and writing before getting
down to the solution I wanted to try. I wasted some time thinking about
how to try to deal with duplicate numbers on a cube. After re-reading
that, iterating through all the 6-combinations of the digits seemed
quite doable. Putting the squares as a data structure and then simply
checking 1 digit in one set and the other digit in the other set or
vice-versa keeps code short and simple.
    Python's itertools are a good thing to know about and Python native
set type make member checking and set operations a breeze.
"""


from copy import copy
import itertools
import sys

#
# GLOBAL DATA
#

# the 1-digit ints, 0 -9
DIGITS = list(range(10))

# there's nine 2-digit squares, here's the data as 2-tuples
SQUARES_LS = [
    (0, 1), (0, 4), (0, 9), (1, 6),
    (2, 5), (3, 6), (4, 9), (6, 4),
    (8, 1),
]


def isValid(s1: set, s2: set) -> bool:
    """
    Evaluate whether all the necessary digit combinations can be formed
    from the two input sets.
    """

    for d1, d2 in SQUARES_LS:
        if not (d1 in s1 and d2 in s2) and not (d1 in s2 and d2 in s1):
            return False

    return True


def augment(digits: set) -> set:
    if 6 in digits:
        return digits.union({9})

    if 9 in digits:
        return digits.union({6})

    return digits


def main():
    solutions = []
    for tup1 in itertools.combinations(DIGITS, 6):
        ext_set1 = augment(set(tup1))
        for tup2 in itertools.combinations(DIGITS, 6):
            ext_set2 = augment(set(tup2))
            if isValid(ext_set1, ext_set2):
                str1 = ''.join([str(i) for i in tup1])
                str2 = ''.join([str(i) for i in tup2])
                s1 = str1 + ':' + str2
                s2 = str2 + ':' + str1  # same two cubes in other order not considered unique
                if s1 not in solutions and s2 not in solutions:
                    solutions.append(s1)

    # DEBUG
    # for i, s in enumerate(solutions):
    #     print(f"{i+1}: {s}")

    print(f"PE90 number of distinct solutions is: {len(solutions)}")
    # 1217 accepted on 2024Jul31:
    """
    Congratulations, the answer you gave to problem 90 is correct.

    You are the 12485th person to have solved this problem.

    This problem has a difficulty rating of 40%. The highest difficulty rating you had previously solved was 25%. 
    This is a new record. Well done!
    """


# ENTRY POINT
if __name__ == '__main__':
    rc = main()
    print("done.")
    print(f"sys.exit({rc})")
    sys.exit(rc)

# EOF
