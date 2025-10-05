#!/usr/bin/env python

filename = 'day1input.txt'


if __name__ == '__main__':
    with open(filename, 'r') as fd:
        lines = fd.readlines()

    print(f"read {len(lines)} lines from '{filename}'")

    a_ls, b_ls = [], []
    for i, line in enumerate(lines):
        try:
            a, b = [int(w) for w in line.strip().split()]
            a_ls.append(a)
            b_ls.append(b)
        except ValueError as ve_x:
            print(f"ValueError at i={i}")

    a_ls.sort()
    b_ls.sort()
    total_diff = 0
    for i in range(len(lines)):
        a, b = a_ls[i], b_ls[i]
        diff = abs(a - b)
        total_diff += diff

    print(f"total_diff is: {total_diff}")

    b_dict = {}
    for b in b_ls:
        try:
            b_dict[b] += 1
        except KeyError:
            b_dict[b] = 1

    score = 0
    for a in a_ls:
        if a in b_dict:
            score += a * b_dict[a]
    print(f"Part 2 score is: {score}")  # 19437052 accepted 2024Dec24

# EOF
