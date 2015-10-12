#!/usr/bin/env python

import sys, os

"""
Solution for codeeval challenge #26 (FILE SIZE)
https://www.codeeval.com/open_challenges/26/

AUTHOR: Erik Johnson
"""

if __name__ == "__main__":
    print os.path.getsize(sys.argv[1])
