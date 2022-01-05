
"""
DESCRIPTION
    An example fetching data via URL.
    You have to get the session value, which can be found in Chrome by R-clicking on
    a page, selecting "Inspect", then select "Application" tab, then under "Storage",
    "Cookies".
"""

import sys
import requests
from pathlib import Path

# GLOBAL DATA
NL = '\n'
URL = 'https://adventofcode.com/2015/day/2/input'
SESS = '53616c7465645f5fcd6717488ba525bffab3b13653a7a0a7a4f5ae3d057c80582fd776cec4ea020d44b48994573d91af'
FILENAME = '2015-2.input'


def getDataLines(url, sess):
    filename = Path(FILENAME)
    if filename.exists():
        print(f"reading from: {filename}")
        with open(filename, 'r') as fd:
            lines = fd.readlines()
        return lines
    else:
        print(f"fetching from URL: {url}")
        req = requests.get(url, cookies={'session': sess})
        data = req.text
        with open(filename, 'w') as fd:
            fd.write(data)
        return data.split(NL)


def main():

    lines = getDataLines(URL, SESS)
    total = 0

    # sum up all the paper needed
    for i, line in enumerate(lines):
        l, w, h = [int(s) for s in line.split('x')]
        # print(f"{i}: {t}")
        dims = [l * w, w * h, l * h]
        small = min(dims)
        sub_total = 2 * sum(dims) + small
        total += sub_total

    # print(f"i is: {i}")
    print(f"total is: {total}")  # 1597514


if __name__ == '__main__':
    main()
