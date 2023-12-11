#!/Users/ejohnson/bin/python

"""
DESCRIPTION
    Just dump the CLI args to terminal, exit.

"""


import sys


if __name__ == '__main__':

    for i, arg in enumerate(sys.argv):
        print(f'{i}: "{arg}"')

# EOF

