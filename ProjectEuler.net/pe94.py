#!/usr/bin/env python
# ProjectEuler.net Problem #54
# https://projecteuler.net/problem=54

r"""

DESCRIPTION (from problem at: https://projecteuler.net/problem=94)

It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has
an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which
two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral
side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

DISCUSSION / STRATEGY
    Let's adopt some naming...
    let:
        'h' be the height of the "almost equilateral" triangle.
        'b' be it's base
        'H' be the hypotenuse of the right triangle such that (b/2)^2 + h^2 == H^2

             /|\
            / | \
           /  |  \
        H /   |h  \ H
         /    |    \
        /     |     \
        -------------
              b

    If b is the main number we are going to iterate over, then
        H = b + 1
     or H = b - 1

    The area is integral (an even integer value) when (b/2) * h is integral.
    If b were 2, the H would be 0 or 2. 0 doesn't really make sense, but
    2 might. Given b and H  as (1, 2), we can solve for h as:
        (b/2)^2 + h^2 = H^2
        (1/4) + h^2 = 4
        h = sqrt(4 - 1/4)
        h = sqrt(15/4)  # == sqrt(3.75), is not integral.
        int(sqrt(3.75)) != sqrt(3.75)

    That is the primary test for whether an "almost equilateral" triangle
    (AET) has integer area.

    The next case for b = 2 would lead to H in [1, 3]...
        b, H = 2, 1             b, H = 2, 3
        (b/2)^2 + h^2 = H^2     (b/2)^2 + h^2 = H^2
        (2/2)^2 + h^2 = 1^2     (2/2)^2 + h^2 = 3^2
        1 + h^2 = 1             1 + h^2 = 9
        h^2 = 0                 h = sqrt(8)
        degenerate triangle     not integral

    We could equivalently iterate over H and let 'b' be either (H - 1) or (H + 1).
    It doesn't matter, so I'll just pick to iterate over 'b'.
    I've already shown the case for b in [1, 2]. Once b is as big as 3, I don't have
    to worry about sqrt() of negative numbers or zero.

    For b = 3, H in [2, 4]:
        (3/2)^2 + h^2 = 2^2         (3/2)^2 + h^2 = 4^2
        9/4 + h^2 = 4               9/4 + h^2 = 16
        h = sqrt(4 - 9/4)           h = sqrt(16 - 9/4)
        1.3228756555322954          3.7080992435478315
    Neither of these is integral.

    The example they give of the AET: 5-5-6  corresponds to the well-known (3,4,5)
    right triangle, where b = 6, H = 5, h = 4
        (b/2)^2 + h^2 = H^2
        3^2 + 4^2 = 5^2
        9 + 16 = 25  # is True
        sqrt(25) == int(sqrt(25))  # is True

    So, iterate b in range(3, ~1e9 / 3.0). But what exactly is the stopping condition?
    1e9 / 3.0 is: 333_333_333 + 1/3
    if b were 333_333_333, H would be in [333_333_332, 333_333_334]
    Let ot = 333_333_333. Then the two perimeters would be:
    [(ot - 1) * 2 + ot, (ot + 1) * 2 + ot]
    [999999997, 1000000001]
    One of these is too big, the other would be acceptable.

"""

from math import sqrt


# GLOBAL DATA
NL = '\n'


def isIntArea(b, H):
    """
    Predicate for whether b2^2 + h^2 = H^2 ?
    h = sqrt(H^2 - b2^2)
    h =? int(h)
    """

    b_2 = b / 2.0
    H_sq = H * H
    h = sqrt(H ** 2 - half_b ** 2)
    if

    if b % 2 == 1:
        # odd
        if k % 2 == 1:  # odd
            temp = half_b * h
            is_int_area = temp == int(temp)
    else:
        # even
        # => half_b is whole number, area can only be integer if h is integer
        is_int_area = h == int(h)

    return h if is_int_area else False


def pe94():
    perim_total = 0
    # having run this, I know there aren't any solutions right near the boundary:
    # for b in range(333_300_000, 333_334_000):
    bil3 = 333_333_333  # ~1/3 of a billion (1e9)
    for b in range(3, 200):
        if b % 5e6 == 0:
            print(b)
        for H in [b + 1, b - 1]:
            h = isIntArea(b, H)
            if h:
                print(t3)
                perim_total += b + 2 * H

    print(f"perimeter total is: {perim_total}")
    # TODO: sum up perimeters


def main():

    # Run Project Euler Problem #94
    pe94()


if __name__ == '__main__':
    main()

"""
(3.0, 4.0, 5)
(8.0, 15.0, 17)
(33.0, 56.0, 65)
(120.0, 209.0, 241)
(451.0, 780.0, 901)
(1680.0, 2911.0, 3361)
(6273.0, 10864.0, 12545)
(23408.0, 40545.0, 46817)
(87363.0, 151316.0, 174725)
(326040.0, 564719.0, 652081)
(1216801.0, 2107560.0, 2433601)
(4541160.0, 7865521.0, 9082321)
(16947843.0, 29354524.0, 33895685)
(46302367.0, 80198051.0, 92604733)
(63250208.0, 109552575.0, 126500417)
(71724130.5, 124229837.0, 143448260)
(88671971.5, 153584361.0, 177343944)
(92604732.0, 160396102.0, 185209465)
(97145894.0, 168261623.0, 194291787)
(101078654.5, 175073364.0, 202157308)
(118026495.5, 204427888.0, 236052992)
(126500418.0, 219105150.0, 253000835)
(139515498.5, 241647933.0, 279030998)
(143448259.0, 248459674.0, 286896519)
(147381019.5, 255271415.0, 294762040)
(151922181.5, 263136936.0, 303844362)
(155854942.0, 269948677.0, 311709883)
perimeter total is: 9399467725   WRONG!
"""

# EOF
