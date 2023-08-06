
"""
DESCRIPTION
    An example fetching data via URL: fetching data on a URL is not a
    requirement here, but I figured that since the AoC website already
    has a page with my data, why not just read that dynamically and not
    even bother getting the data over here in a static way at all?

    In order to do so, you must first have logged into the AoC website,
    and then a session cookie is needed. That can be found in Chrome by
    R-clicking on a page, selecting "Inspect", then select "Application"
    tab, then under "Storage", "Cookies".

    So, it is a bit manual to go fetch the session cookie. This is
    basically a Proof of Concent (POC) just because I felt like it.

AUTHOR
    Erik Johnson

HISTORY (see also: git log <filename>)
    2022Jul25 update comments
    2022Jan03 working
    2022Jan03 created
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

    # PART 1: sum up all the paper needed
    total = 0
    for i, line in enumerate(lines):
        l, w, h = [int(s) for s in line.split('x')]
        # print(f"{i}: {t}")
        dims = [l * w, w * h, l * h]
        small = min(dims)
        sub_total = 2 * sum(dims) + small
        total += sub_total
    print(f"paper total is: {total}")  # 1598415

    # PART 2: sum up all the ribbon needed
    total = 0
    for i, line in enumerate(lines):
        l, w, h = [int(s) for s in line.split('x')]
        sub_total = 2 * sum(sorted([l, w, h])[:2])
        total += sub_total + (l * w * h)
    print(f"ribbon total is: {total}")  # 


if __name__ == '__main__':
    main()
