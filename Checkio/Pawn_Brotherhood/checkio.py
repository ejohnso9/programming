
def safe_pawns(pawns: set) -> int:
    """how many pawns in the given coord list are supported (protected)?"""
    count = 0
    letters = list('abcdefgh')
    supported: bool = False
    for p in pawns:
        f, r = p[0], int(p[1])  # file, rank

        # check behind and left
        if f != 'a':  # 'a' is left-most file
            _file = letters[letters.index(f) - 1]
            left_back = f'{_file}{r - 1}'
        else:
            left_back = False

        # check behind and right
        if f != 'h':  # 'h' is right-most file
            _file = letters[letters.index(f) + 1]
            right_back = f'{_file}{r - 1}'
        else:
            right_back = False

        count += int(left_back in pawns or right_back in pawns)

    return count

assert safe_pawns({'d4', 'c3', 'g7', 'e5', 'h8', 'a1', 'f6', 'b2'}) == 7

print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"f4", "g5", "c3", "d2", "b4", "e3", "d4"}) == 6
assert safe_pawns({"f4", "e5", "g4", "e4", "b4", "d4", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
