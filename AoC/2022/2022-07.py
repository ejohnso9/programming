#!/usr/bin/env python 

"""
Advent of Code solution for Day 6
    https://adventofcode.com/2022/day/6

THOUGHTS/IDEAS/DISCUSSION:
    There are probably lots of ways to represent a directory structure.
    For this problem, one fairly straightforward ways seems to me is as
    linked dicts.

    That is, a hierarchical native Python dicts where a dict has:
        - a list of other dirs under it
        - a list of files within (with their size)
        - a link (obj ref) to get back to the containing parent dir

HISTORY
    2023Aug09  ej  created
"""

from typing import Callable
# from functools import partial

# GLOBAL DATA
DAY = 7
LINES = None
FILENAME = f"2022-{DAY:02d}.input.txt"
PROBLEM = f"Aoc 2022 Day {DAY},"

# SYMCONSTS
PARENT = '_parent'
FILES = '_files'
DIRS = '_dirs'
NAME = '_name'


def readInputFile(filePath_str):
    """read input file (just once)"""
    global LINES
    if not LINES:
        with open(filePath_str, 'r') as fd:
            LINES = fd.readlines()

    return LINES


def initFileSystem():
    """Build inital rep for our mock file system"""

    return newDir('/', None)


def newDir(name, parent_d):
    return {
        NAME: name,
        PARENT: parent_d,
        DIRS: list(),
        FILES: list(),
    }


def chdir(from_cur_dir, to_name):
    # special cases
    if to_name == '/':
        return ROOT

    if to_name == '..':
        return from_cur_dir[PARENT]

    # just find the right local (child) dir
    for d in from_cur_dir[DIRS]:
        if d[NAME] == to_name:
            return d

    # NOT FOUND!
    raise RuntimeError


def addDir(toDir, newDirName):
    # add another dir rep
    new_d = newDir(newDirName, parent_d=toDir)
    toDir[DIRS].append(new_d)


def addFile(toDir, fileName, fileSize):
    toDir[FILES].append((fileName, fileSize))


def processCommands(input_lines, startingDir):

    cur_dir = startingDir

    for line in input_lines:
        words = line.split()
        if words[0] == '$':  # input command
            # cd: change directory
            if words[1] == "cd":
                cur_dir = chdir(cur_dir, words[2])

        # add new directory
        elif words[0] =='dir':
            addDir(cur_dir, words[1])

        # add a new file
        else:
            size, name = int(words[0]), words[1]
            addFile(cur_dir, name, size)


def getSize(fileOrDir):
    # files are represented as tuples
    if type(fileOrDir) is tuple:
        return fileOrDir[1]

    # dirs are represented as dict and the size of one is:
    #   the size its dirs (recursively)
    #   plus the sum total of the sizes of its files
    else:
        this_dir = fileOrDir
        files_sz = sum([getSize(f) for f in this_dir[FILES]])
        dirs_sz = sum([getSize(d) for d in this_dir[DIRS]])
        return files_sz + dirs_sz


def getDirs(this_dir, parent_path, acc_ls):
    if parent_path == '':
        path = '/'
    else:
        path = parent_path + '/' + this_dir[NAME]
    acc_ls.append(path)

    # recursively call this on each child
    for child_dir in this_dir[DIRS]:
        getDirs(child_dir, path, acc_ls)


def main():
    """Implements AoC Day N"""

    # initialize file system representation
    global ROOT
    ROOT = initFileSystem()
    lines = readInputFile(FILENAME)
    processCommands(lines, ROOT)  # NB: root modified!

    acc = list()
    getDirs(ROOT, '', acc_ls=acc)
    for p in acc:
        print(p)

    # Part 1: first unique 4 characters found after reading 'answer' chars
    # s = "abcd"  # TEST: should not fail, have to read 4 chars to find unique part
    # part = 1
    # answer = f_findUniqueIndex(s, n)
    # exp = 1134  # submitted and accepted on 2023Aug09 (2nd try)
    # print(f"{PROBLEM} Part {part}: first uniq{n} after: {answer} chars")
    # print(s[answer - n: answer])
    # print()

    # Part 2: same as part one, but find longer unique part
    # part = 2
    # n = 14
    # answer = f_findUniqueIndex(s, n)
    # exp = 2263  # submitted and accepted on 2023Aug09 (1st try)
    # print(f"{PROBLEM} Part {part}: first uniq{n} after: {answer} chars")
    # print(s[answer - n: answer])


# ENTRY POINT
if __name__ == '__main__':
    main()


# EOF
