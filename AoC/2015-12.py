#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DESCRIPTION

--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent
order. Unfortunately, their accounting software uses a peculiar storage
format. That's where you come in.

They have a JSON document which contains a variety of things: arrays
([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first
job is to simply find all of the numbers throughout the document and add
them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?


DISCUSSION
    At the top level, the JSON file is translated to a native Python
dict (in this case with keys: a, b, c, d, e, f). I need a general
evaluator function that can recursively iterate over an object and
convert that into a number. Let's call that: 
    numerate(obj)

    Just browsing over the data, it looks like there are no floats. In
fact, the file doesn't have a '.' char in it.

STRATEGY
    numerate(obj) basically needs to check the type of its argument and
    then do a limited number of things:
        A) some things evaluate directly:
            numbers (ints) are themselves
            empty lists are 0
            empty dicts are 0
            strings: evaluate as 0
        B) some things need to recurse:
            lists: value is sum of numerate() applied to each element
            dicts: value is the sum of numerate() applied to each item value

    Seems like that should cover it?
"""


import sys
import json
# import pdb  # http://pymotw.com/2/pdb/


def numerate(thingy):
    """short, sweet, beautiful! (This is why I love Python)"""
    _type = type(thingy)
    if _type is str:
        return 0
    elif _type is int:
        return thingy
    elif _type in [list, dict]:
        if len(thingy) == 0:
            return 0

        if _type is list:
            return sum([numerate(item) for item in thingy])
        else:  # dict
            # special clause for Part 2
            if 'red' in thingy.keys() or 'red' in thingy.values():
                return 0
            return sum([numerate(value) for value in thingy.values()])
    else:
        raise RuntimeError(f"unexpected type: {_type}")


def main():

    # load the JSON input file
    filename = '2015-12.input.json'
    with open(filename, 'r') as fd:
        text = fd.read()
    d = json.loads(text)  # dict

    # both parts verified correct on: 2022Jul29
    print(numerate(d))  # Part 1: 111754, Part 2: 65402


if __name__ == '__main__':
    main()

# EOF
