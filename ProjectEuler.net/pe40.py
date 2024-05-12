#!/usr/bin/env python

"""
This is notes (maybe later a program for
ProjectEuler problem #40:

    https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.
(ej: the 15th is 2, the 17th is 3, etc.)

If d[n] represents the nth digit of the fractional part,
find the value of the following expression.

    d[1] * d[10] * d[100] * ... * d[1000000]

So, I could perhaps be very clever and work out formulas to do this in
an incredibly efficent manner, using almost no computer memory.

If the required indices went up into the billions, trillions, and
beyond, I would do that. But the reality is that generating a string
with 1 million characters is well within what I would call "normal"
operating ranges for Python on a modern desktop computer.

So, the first approach is to simply plunk down the Python code to form
the string, extract the digits, multiply out the int and see if that
isn't the answer. If it is, I'll probably just go on and not think about
how I would form code to access things like d[1e30], d[1e50], etc.

There's probably some interesting math and computing in that approach -
I am probably more pragmatic than I am clever.

In fact, output of my program on 2024Feb16 was:

20:12 ~/src/git/programming/ProjectEuler.net$ python pe40.py 
count = 1000005
[1, 1, 5, 3, 7, 2]
product is: 210

And 210 is actually the accepted number.

So, am I dumb for not getting into all the math to solve this in a
"smarter" way, or am I smart to leverage the power of modern computers
to quickly solve this problem in a "dumb" way?

This problem is far too small to be forcing people to work out all the
math so that you can access things like d[1e30].

Problem #40 solved @ 2024Feb16.

"""


import math


N = 6

def main() -> int:
    count = 0
    i = 0
    strs = ['_']  # such that s[1] will be the first fractional digit
    while count < 10 ** N:
        i += 1
        s = str(i)
        strs.append(s)
        count += len(s)

    print(f"count = {count}")
    s = ''.join(strs)

    num_ls = [int(s[10 ** x]) for x in range(N)]
    print(num_ls)
    print(f"product is: {math.prod(num_ls)}")

    

if __name__ == '__main__':
    main()


# EOF

