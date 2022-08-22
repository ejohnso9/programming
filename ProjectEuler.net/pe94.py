#!/usr/bin/env python
# ProjectEuler.net Problem #54
# https://projecteuler.net/problem=54

"""

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

    The area is integral when b * h is integral.
    If b were 2, the H would be 0 or 2. 0 doesn't really make sense, but
    2 might. Given b and H, we can solve for h as:
        (b/2)^2 + h^2 = H^2
        (1/4) + h^2 = 4
        h = sqrt(4 - 1/4)
        h = sqrt(15/3)  # == sqrt(3.75)
        That's not integral:
        int(sqrt(3.75)) != sqrt(3.75)

    That is the primary test for whether an "almost equilateral" triangle
    (AET) has integer area.

    The next case for b = 2 would lead to H in [1, 3]...
        (b/2)^2 + h^2 = H^2
        1^2 + h^2 = 1^2         1^2 + h^2 = 3^2
        1 + h^2 = 1             1 + h^2 = 9
        h^2 = 0                 h = sqrt(8)
        degenerate triangle     not integral

    We could equivalently iterate over H and let 'b' be either (H - 1) or (H + 1).
    It doesn't matter, so I'll just pick to iterate over 'b'.
    I've already shown the case for b in [1, 2]. Once b is as big as 3, I don't have
    to worry about sqrt() of negative or zero numbers.
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

# GLOBAL DATA
NL = '\n'


def pe94():


def main():

    i = pe94()


if __name__ == '__main__':
    main()


# EOF
