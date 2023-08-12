#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DESCRIPTION

DISCUSSION
    This is not the first time I have seen John Conway's "Look-and-Say" sequence.
    In fact, probably the best introduction to that sequence is here:
    https://oeis.org/A005150

    If you search that page for "ejohnso9" (my email address), you'll find my
    own Python implementation of A005150(), a function which takes N and returns
    the first N terms of that sequence (which I wish I had documented):

    def A005150(n):
        seq = [1] + [None] * (n - 1) # allocate entire array space
        def say(s):
            acc = '' # initialize accumulator
            while len(s) > 0:
                i = 0
                c = s[0] # char of first run
                while (i < len(s) and s[i] == c): # scan first digit run
                    i += 1
                acc += str(i) + c # append description of first run
                if i == len(s):
                    break # done
                else:
                    s = s[i:] # trim leading run of digits
            return acc
        for i in range(1, n):
            seq[i] = int(say(str(seq[i-1])))
        return seq
        # E. Johnson (ejohnso9(AT)earthlink.net), Mar 31 2008

    ...which I guess I sent to Neil Sloane on or about Mar 31, 2008. I do remember
    sending him some code, and I remember my considerable surprise some time later
    to see my own code appear on that page. I don't remember whether I got an email
    from him or not, and I don't remember exactly why I sent in a solution. Looking
    at the solution above it:
        # Olivier Mengue (dolmen(AT)users.sourceforge.net), Jul 01 2005
    I notice that mine has the same name, same input, same output. I was probably
    looking at that and feeling like that was a Python version of C code and felt
    like I wanted something a bit more understandable, a bit more Pythonic. I don't
    actually know if my solution is faster or not. It might be. It might be slower.

    At any rate, this is not the first time I've come across Look-and-Say, and I
    see no reason I should not re-use the internal say() function from the OEIS page.

STRATEGY
    separate say() from OEIS page, iteratively feed the starting input back into it.
"""

import sys
# import pdb  # http://pymotw.com/2/pdb/

# GLOBAL DATA
NL = '\n'


def say(s):
    acc = ''  # initialize accumulator
    while len(s) > 0:
        i = 0
        c = s[0]  # char of first run
        while i < len(s) and s[i] == c:  # scan first digit run
            i += 1
        acc += str(i) + c  # append description of first run
        if i == len(s):
            break  # done
        else:
            s = s[i:]  # trim leading run of digits
    return acc


def main():
    input_s = "1113122113"  # from the web page: https://adventofcode.com/2015/day/10
    for i in range(50):
        input_s = say(input_s)

    print(len(input_s))  # 360154 verified correct on 2022Jul26


if __name__ == '__main__':
    main()

# EOF
