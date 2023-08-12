#!/usr/bin/env python
# run on pythonanywhere.com at version 3.9.5

r"""
DESCRIPTION
    https://adventofcode.com/2015/day/14

--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but
must rest occasionally to recover their energy. Santa would like to know
which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or
resting (not moving at all), and always spend whole seconds in either
state.

For example, suppose you have the following Reindeer:

    - Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    - Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km.
After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
On the eleventh second, Comet begins resting (staying at 140 km), and
Dancer continues on for a total distance of 176 km. On the 12th second,
both reindeer are resting. They continue to rest until the 138th second,
when Comet flies for another ten seconds. On the 174th second, Dancer
flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and
Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by
that point). So, in this situation, Comet would win (if the race ended
at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after
exactly 2503 seconds, what distance has the winning reindeer traveled?


DISCUSSION
    Basically, we need an eval function, given the length of time to
    evaluate for and a reindeer's parameters.

    So, there's basically two periods: flying, resting
    You can start with an int, then iterate over the two periods,
    subtracting the time of that period, until you get down to a point
    where there are not enough second left to complete the last period.
    Then you simply make an evaluation, and add to the total:
        0 if not enough enough time to finish rest
        speed * seconds_left if not enough time to finish fly

STRATEGY

"""

# import pdb  # http://pymotw.com/2/pdb/

# GLOBAL DATA
NL = '\n'
REINDEER = """\
Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.
"""

# TEST DATA
# REINDEER = """\
# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# """


def lineToTuple(line):
    words = line.split()
    def fType(value, index):
        return int(value) if index in [3, 6, 13] else value
    return tuple([fType(words[i], i) for i in [0, 3, 6, 13]])


def makeReindeerDict(text):
    reindeer_d = {}
    for line in text.split(NL)[:-1]:
        t = lineToTuple(line)
        reindeer_d[t[0]] = t[1:]

    return reindeer_d


def distance(params, time):
    # init func state
    speed, t_fly, t_rest = params
    t = time  # value decremented in loop
    flying = True
    dist = 0

    # decrement all the periods
    while True:
        t_period = t_fly if flying else t_rest
        if t_period <= t:
            dist += speed * t_fly if flying else 0
            t -= t_period
            flying = not flying
        else:
            dist += speed * t if flying else 0
            break

    return dist


def main():
    # time = 1000  # TEST
    time = 2503  # from description
    reindeer_d = makeReindeerDict(REINDEER)
    for name, rd_params in reindeer_d.items():
        dist = distance(rd_params, time)
        print(name, dist)

    # above dumps out:
    """
Vixen 2640
Blitzen 2496
Rudolph 2540
Cupid 2592
Donner 2655
Dasher 2460
Comet 2493
Prancer 2484
Dancer 2516
    """
    # 2655 is the max of those values, verified correct on 2022Jul29


if __name__ == '__main__':
    main()

# EOF
