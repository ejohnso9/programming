#!/usr/bin/env python
# developed under Python 3.10

"""
AUTHOR: Erik Johnson

DATE: 2022Aug09

DESCRIPTION (from the CodeWars web page)

This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

    seven(times(five())) # must return 35
    four(plus(nine())) # must return 13
    eight(minus(three())) # must return 5
    six(divided_by(two())) # must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations:
    plus, minus, times, divided_by

Each calculation consist of exactly one operation and two numbers.

The most outer function represents the left operand, the most inner function
represents the right operand.
Division should be integer division.

For example, this should return 2, not 2.666666...:
    eight(divided_by(three()))

DISCUSSION
    Functions can themselves have attributes in Python.
    DRY: (D)on't (R)epeat (Y)ourself principle!
    All the numberic functions are essentially the same - I don't want
    to explicitly define each one (as the given boilerplate code leads
    you to do). Likewise, all the operator functions are essentially
    the same.

    NB: I'm not playing code golf here: this is an example of how I do
        production code.
"""


from operator import add, sub, mul, floordiv


CLASS_FUNCTION = "<class 'function'>"  # value of str(type(f)) when f a function


def makeNumFunc(num):
    def num_func(a=None):
        if a is None:  # when called w/ no arg: 
            return num_func.num  # just return the numeric value
        elif str(type(a)) == CLASS_FUNCTION:  # when called with op func...
            # remap this into a call on the op func w/ 2 args
            return a(num_func.num, a.r_val)

    num_func.num = num  # assign the numeric value
    return num_func


def makeOpFunc(f_name):
    def op_func(a, b=None):
        if b is None:  # called w/o args
            op_func.r_val = a  # just save numeric value for later call w/ 2 args
            return op_func
        else:  # called w/ 2 args
            return op_func.op(a, b)  # do the actual operator

    op_func.op = {
        'plus': add,
        'minus': sub,
        'times': mul,
        'divided_by': floordiv,
    }[f_name]
    
    return op_func


# instantiate the numeric functions
f_names = "zero one two three four five six seven eight nine"
for i, f_name in enumerate(f_names.split()):
    locals()[f_name] = makeNumFunc(i)
    
# instantiate the operator functions
op_names = "plus minus times divided_by"
for i, f_name in enumerate(op_names.split()):
    locals()[f_name] = makeOpFunc(f_name)

    
# TEST CODE - not really part of the solution
"""
# try it
i = three()
print(f"three() is: {i}")
i = divided_by(three())
print(f"divided_by(three()) is: {i}")
i = eight(divided_by(three()))
print(f"eight(divided_by(three())) is: {i}")
# the rest of the sample test suite
values = [
    seven(times(five())),  # 35)
    four(plus(nine())),  # 13)
    eight(minus(three())),  # 5)
    six(divided_by(two())),  # 3)
]
for i, val in enumerate(values):
    print(f"test[{i}] is: {val}")
"""

# EOF

