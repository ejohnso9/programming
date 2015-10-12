#!/usr/bin/env python

import sys

"""
Solution for codeeval challenge #17  (SUM OF INTEGERS)
https://www.codeeval.com/open_challenges/17/

AUTHOR: Erik Johnson

DISCUSSION:
    So, I think I have seen other similar problems referred to as
"dynamic programming" problems. I don't have any formal training in
dynamic programming, but this problem is somewhat interesting in that a
little bit of cleverness can go a long ways towards efficiency.

    Given a list of N integers, find the maximum sum of contiguous
integers. One could simply brute-force it, but that is an O(N^2)
solution. You need to look at the sum of all N integers, the two sums of
N-1 integers (starting the list sum at indices 0 and 1), the three sums
of N-2 integers, ..., all the 3-element lists, all the two element lists,
and finally all the 1-element lists.

    But these elements can be combined to compute equivalent answers.
First of all, all adjacent non-negative integers can be combined, and
all the adjacent negative integers can be combined. That reduces N.

    That will reduce our list to elements that alternate positive and
negative:

    [p0, n1, p2, n3, p4, n5, ...]

    or: [n0, p1, n2, p3, n4, p5, ...]

    If the sum of any [p, n, p] triplet is positive, then it is a net
gain to just include the negative number in any contiguous run, and so
those three elements can be combined into one.

    After you can't find anymore such triplets to combine, you are left
with a list where negative elements dominate their neighbors, and can
then proceed to look at the biggest positive elements between these
negative elements.

    I don't know if this is dynamic programming, but that's my plan.

"""


def combinePosNeg(l):
    """adjacent negative or non-negative elements combined"""

    # init
    newList = []
    negative = l[0] <= 0
    newSum = 0

    # just walk down the list looking for multiple elements of same
    # kind, combining these into a new element on the new list
    for n in l:
        # negative or zero
        if n < 1:
            if negative:
                newSum += n # continue to sum negative numbers
            else: # hit other type
                newList.append(newSum)
                newSum = n
                negative = not negative
        
        # positive
        else:
            if not negative:
                newSum += n # continue to sum positive numbers
            else: # hit other type
                newList.append(newSum)
                newSum = n
                negative = not negative

    # tack on the last element
    newList.append(newSum)

    return newList


def recombine(l):
    """
    March down the list (assumed to start w/ positive element).
    Whereever
    """

    newList = []
    combined = False
    end = len(l) - 3  # index of 3rd to last element
    i = 0
    print l
    thisSum = l[i]

    while i <= end:
        next2sum = l[i+1] + l[i+2]

        if next2sum >= 0:
            thisSum += next2sum
            combined = True
        else:
            newList.append(thisSum)
            thisSum = l[i+2]

        i += 2

    print newList

    return (combined, newList)


if __name__ == "__main__":

    for line in open(sys.argv[1], 'r'):
        iList = [int(s.strip()) for s in line.split(',')]

        # combine adjacent elements of same type
        iList = combinePosNeg(iList)

        # we can drop first and last elements if negative - they
        # contibute nothing to a contiguous run of positive
        if iList[0] < 1:
            iList = iList[1:]
        if iList[-1] < 1:
            iList = iList[:-1]

        # assert: we now have a list of alternating pos/neg elements
        # where first and last element are positive

        # while elements are still getting combined, continue to make
        # passes on the list combining [pos, neg, pos] triplets
        tf = True
        while tf:
            (tf, iList) = recombine(iList)

        print max(iList)
