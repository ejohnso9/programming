#!/usr/bin/env python

"""
written for Python 2.x

Project Euler Problem #17

PROBLEM STATEMENT

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.

DISCUSSION

STRATEGY
    Just build 3 functions backed by dicts that convert the digit in the
{hundreds, tens, ones} place into the number of letters for the
corresponding word, then run the sequence 1-999, convert to string and
pick off each digit and call each of those functions, summing up the
total letters as you go. Add 11 at the end for "one thousand".

    Heh... that doesn't quite work, does it? We have these ugly teens to
deal with. Fine, just put their value in their own dict, and when you
are over 99, just take next two digits together and look for the parts
that begin with '1'.

    Well, I kept having trouble with the answer computed here not being
the accepted answer, even though it seemed like things were working as
expected. I decided to make things be able to print either the words or
the numeric value so I can try to figure out where this is going wrong.

    Wow... the numbers look to be printing correctly. If I only print
out lines where the length of the space-stripped words doesn't equal the
numeric (integer) value from my function, no lines print. I keep coming
up with 21125, but PE does not accept it.

    Third approach:  https://oeis.org/A000027/a000027.txt gives the
American English names of 0 through 11159  A partial dump of that is
below. Let's just process this text, then correct the value for all teh
missing "and"s not in this text. So, the first line below that is off is
for 101: "onehundredone" is three short, all the numbers 101 - 199 are
three short. That's 297 the text below is short for the 100's.
"twohundred" is correct, then 201 through 299 is likewise short by 297.
So, {1,2,3,4,5,6,7,8,9}-hundred are each short by 297, that's a total of
9 * 297 = 2673 characters the text below would be short. (Actually I am
just adding 3 for the numbers 100-999 that are not multiples of 100.)

    Shoot... off by one, and I finally narrowed the problem to simply
adding len("one thousand") at the end. DON'T INCLUDE SPACES!
21124 is the correct answer and the first iteration of my code was
correct except for that one extra space.

Deleting all that text for: https://oeis.org/A000027/a000027.txt
"""

import sys, pdb

ONES_D  = {
    0: (0, ''),
    1: (3, 'one'),
    2: (3, 'two'),
    3: (5, 'three'),
    4: (4, 'four'),
    5: (4, 'five'),
    6: (3, 'six'),
    7: (5, 'seven'),
    8: (5, 'eight'),
    9: (4, 'nine'),
}

TEENS_D = {
    10: (3, 'ten'),
    11: (6, 'eleven'),
    12: (6, 'twelve'),
    13: (8, 'thirteen'),
    14: (8, 'fourteen'),
    15: (7, 'fifteen'),
    16: (7, 'sixteen'),
    17: (9, 'seventeen'),
    18: (8, 'eighteen'),
    19: (8, 'nineteen'),
}

TENS_D = { 
    0: (0, ''), # e.g., 503: "five hundred and three"
    1: (None, None),  # throw TypeError out of sum() (by design)
    2: (6, 'twenty'),
    3: (6, 'thirty'),
    4: (5, 'forty'),
    5: (5, 'fifty'),
    6: (5, 'sixty'),
    7: (7, 'seventy'),
    8: (6, 'eighty'),
    9: (6, 'ninety'),
}


def ones(i, words=False):
    return ONES_D[i][1] if words else ONES_D[i][0]


def teens(i, words=False):
    return TEENS_D[i][1] if words else TEENS_D[i][0]


def tens(i, words=False):
    return TENS_D[i][1] if words else TENS_D[i][0]


def n_letters(x, words=False):
    l = [int(c) for c in list(str(x))]
    n = len(l) # 1, 2 or 3

    if n == 1:
        rv = ones(x, words)
    elif n == 2:
        t, o = l[0], l[1]
        if t == 0:
            rv = ones(o, words)
        elif t == 1:
            rv = teens(10 * t + o, words)
        else:
            if o == 0:
                rv = tens(t, True) if words else tens(t)
            else:
                if words:
                    rv = tens(t, True) + ' ' + ones(o, True)
                else:
                    rv = tens(t) + ones(o)
    else: # n == 3
        h, t, o = l[0], l[1], l[2]
        if t == 0 and o == 0:
            rv = ones(h, True) + ' hundred' if words else ones(h) + 7  # e.g., '100'
        else:
            if words:
                rv = ones(h, True) + ' hundred and ' + n_letters(10 * t + o, True)
            else:
                rv = ones(h) + 10 + n_letters(10 * t + o)

    return rv


def data_count(data):
    total = 0
    for line in data.split('\n'):
        line = line.strip()
        i_s, s = line.split()
        n = len(s)
        i = int(i_s)
        if i % 100 != 0 and i > 100:
            n += 3
        total += n

    return total


if __name__ == '__main__':

    # print "data_count =", data_count(A000027)
    # sys.exit(0)

    total = 0
    t2 = 0

    for i in range(1, 1000): # up to 999!
        n = n_letters(i)
        total += n

        s = n_letters(i, True)
        n2 = len(s.replace(' ', ''))
        t2 += n2

        if i > 0 and i < 100:
        # if n != n2:
            print "%i: '%s'" % (n, s)

    total += len("onethousand")
    t2    += len("onethousand")

    print "total letters is:", total
    print "t2:", t2


"""
one, two, three, four, five, six, seven, eight, nine
sum([3,3,5,4,4,3,5,5,4]) = 36

ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
eighteen, nineteen
sum([3,6,6,8,8,7,7,9,8,8]) = 70
"""
