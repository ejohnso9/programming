#! /usr/bin/env python

"""
DESCRIPTION:
    A working solution for Python challenge problem #10, which starts at:

        http://www.pythonchallenge.com/pc/return/bull.html

Click on the bull and arrive at sequence.txt whose contents are:

a = [1, 11, 21, 1211, 111221,

Original page asks:  len(a[30]) = ?

I guess we are looking for a number which is the length of the 31st
element of this sequence.

After looking at this for a while, I didn't see a pattern that quite
fits. Rather than spending a lot of time trying to solve the sequence
itself, I would rather find the sequence and get on with coding it.  I
have been aware of the Online Encyclopedia of Integer Sequences long
before I came to this problem and I am smart enough to know that
sometimes it is better to just look up stuff on the internet and bring
those resources to bear on a problem than to solve the problem from
scratch. Let's get on with the coding part:

This appears to be the "Look and Say sequence": 

    http://www.research.att.com/~njas/sequences/A005150

which is basically "describe the previous term".
That is, it starts with a '1', and the description of that is: "one 1",
or, in digits "11". The description of that is then, "two 1's", or "21",
and the description of that is "one 2 and one 1's" or "1211", and so on.

(NOTE: Actually, there is some code at that web page as well which I could
simply convert to python using the same jusification as above, but that
would take the programming fun out of this - A problem I think will be
enjoyable and not really very hard.)

So, the question "Is it possible for you to have more than 9 of a digit
in a row?" immediately springs to mind, with the obvious follow-on of
"What would be the description of such a string?"  This string has
twelve ones in it: '111111111111' The description for such a thing would
seem to logically be "121" (i.e., "twelve 1's"), but the first part of
that description would logically be "one two" and then you have the
problem of that dangling "one" in the description by itself.  I beleive,
with the exception of the first term to get things bootstrapped, that
every succeeding term should have an even number of digits (or
characters).  

To "say" a term means to construct the description for a given sequence
of digits. That is, count the number of occurences of first digit, write
the number for that followed by that digit. That is, the description
comes as a concatenation of pairs of digits, so "121" would be an
invalid description.

This is a bit of a tangent and a problem I will come back to later.
Right now, the problem at hand is: len(a[30])

INITIAL PROBLEM DESIGN
=======================
I think I want a recursive function that can take some parameters like
the previous sequence (or part of it), and an accumulator and just build
up the description as you go, ending the recursion when you measure the
lengh of the last digit run in the string.
"""


# IMPORTS
#=======================================================================
import sys


# GLOBAL DATA
#=======================================================================

"""
DESCRIPTION:
    Analyze the first digit run in string 's' and append the
    description to 'acc'.

PARAMETERS:
    s - string: A sequence of digits, 1-9  (note no '0's!)
    acc - accumulator
"""

#-----------------------------------------------------------------------
def say(s, acc=''):
    if type(s) == int:
        s = str(s)
    length = len(s)
    i = 0
    c = s[0]
    while (i < length and s[i] == c):
        i += 1

    # Now, i is either pointing at the first non-d character in s, or i
    # is pointing one position past the end of s (and it's easy to
    # determine which). That is, either we're done with this description
    # or we need to call ourselves again with s less the first digit
    # run.

    if i == length:
        return acc + str(i) + c
    else:
        return say(s[i:], acc + str(i) + c)

#-----------------------------------------------------------------------
def Mengue(n): 
    """This is the solution given at: 
    http://www.research.att.com/~njas/sequences/A005150
    It seems a bit odd to me in that it returns the first n elements of
    the sequence rather than element n. It is non recursive, less
    intuitive but probably substantially more efficient than my solution.
    """

    p = "1" 
    seq = [1] 
    while (n > 1): 
        q = '' 
        idx = 0 # Index 
        l = len(p) # Length 
        while idx < l: 
            start = idx 
            idx = idx + 1 
            while idx < l and p[idx] == p[start]: 
                idx = idx + 1 
            q = q + str(idx-start) + p[start] 
        n, p = n - 1, q 
        seq.append(int(p)) 
    return seq 

#-----------------------------------------------------------------------
def A005150_1(n):
    """
    First iteration - problems with recursive say():
    Here I am using the name of the function given on the web page to
    provide equivalent semantics to the function given my Mengue using
    my own say() function. This works fine, up to a point, but because
    the Look and Say sequence grows quite rapidly, this function soon
    runs into the inherent recursion limit of the Python interpreter
    (which is normally set at a default of 1000).

    You can manually boost this recusion limit up by using methods
    provided on the sys module. dir(sys) has a lot of stuff in it.
    Here's a neat little trick to find what you are looking for in a big
    list of stuff:

    >>> import sys
    >>> [x for x in dir(sys) if x.find('recur') != -1]
    ['getrecursionlimit', 'setrecursionlimit']

    """

    seq = [1] + [None] * (n - 1)
    def say(s, acc=''):
        i = 0
        c = s[0]
        while (i < len(s) and s[i] == c):
            i += 1
        if i == len(s):
            return acc + str(i) + c
        else:
            return say(s[i:], acc + str(i) + c)
    for i in xrange(1, n):
        seq[i] = int(say(str(seq[i-1])))
    return seq

#-----------------------------------------------------------------------
def A005150(n):
    seq = [1] + [None] * (n - 1)  # allocate entire array space
    def say(s):
        acc = ''                  # initialize accumulator
        while len(s) > 0:
            i = 0
            c = s[0]              # char of first run
            while (i < len(s) and s[i] == c):  # scan first digit run
                i += 1
            acc += str(i) + c  # append description of first run
            if i == len(s):
                break          # done
            else:
                s = s[i:]      # trim leading run of digits
        return acc
    for i in xrange(1, n):
        seq[i] = int(say(str(seq[i-1])))
    return seq
#-----------------------------------------------------------------------

#///////////////////////////////////////////////////////////////////////
# MAIN
#
# PREREQUISITES:
#     FIRST and SECOND arrays defined above
if __name__ == '__main__':

    sys.setrecursionlimit(100000)
    a = A005150(31)
    print len(str(a[30]))  # prints "5808"


# END MAIN
#///////////////////////////////////////////////////////////////////////

"""
SOLUTION DISCUSSION:

    Problem #11 starts at:

        http://www.pythonchallenge.com/pc/return/5808.html


    One common trade off in computing time versus size. Another common
one is efficiency versus understandability or the "natural expression"
of a problem in code. Sometimes what is most straightforward and
"natural" is not efficient.

    This bothers me somewhat because I rather like my solution. Let's
see if i can find some sort of a blend that still seems pretty natural
but is not recursive:
"""

#-----------------------------------------------------------------------
def say_nr(s):
    "A non-recursive version of say()"
    
    if type(s) == int:
        s = str(s)

    acc = ''  # description accumulator

    while len(s) > 0:
        length = len(s)
        i = 0
        c = s[0]
        while (i < length and s[i] == c):
            i += 1

        acc += str(i) + c

        # i now either pointing at the first non-c character in s, or
        # i is one position past the end of s 
        if i == length:
            break
        else:
            s = s[i:]  # trim leading run of digits

    return acc
