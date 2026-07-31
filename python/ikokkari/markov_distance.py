# 63. Markov distance
def markov_distance(t1: tuple[int, int, int], t2: tuple[int, int, int]) -> int:
    """
    Compute the Markov distance between two given tuples.
    (looks like the "parent" tuple is always (a, b, 3 * a * b - c))
    """

    # make sure input tuples are in sorted order
    ls1 = sorted(t1)  # NB: this actually becomes list[int] (no need for tuple)
    ls2 = sorted(t2)  # NB: this actually becomes list[int] (no need for tuple)
    dist = 0  # i.e., count of parent climbs
    while ls1 != ls2:
        # climb upward on the tree one step for the largest tuple, reassign 3rd element of biggest tuple
        ls = ls1 if ls1[2] > ls2[2] else ls2
        a, b, c = ls
        ls[2] = 3 * a * b - c  # <- always replacing 3rd element
        ls.sort()
        dist += 1

    return dist
