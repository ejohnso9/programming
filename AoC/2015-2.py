
"""
DESCRIPTION
    An example fetching data via URL.
    You have to get the session value, which can be found in Chrome by R-clicking on
    a page, selecting "Inspect", then select "Application" tab, then under "Storage",
    "Cookies".
"""
import sys

DATA

# print(len(DATA))

# PART 1
left = sum([1 for c in DATA if c == '('])
print(f"left is: {left}")
right = sum([1 for c in DATA if c == ')'])
print(f"right is: {right}")
print(abs(left - right))  # 280

# PART 2
print(DATA[0:10])
floor = 0
for i, c in enumerate(DATA):
    x = 1 if c == '(' else -1
    floor += x
    if floor == -1:
        print(f"i is: {i}")  # 1796 is printed, AoC wants 1-based index, so 1797
        break