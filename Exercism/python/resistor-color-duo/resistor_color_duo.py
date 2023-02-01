
_COLOR_STR = "Black Brown Red Orange Yellow Green Blue Violet Grey White"
COLORS = [w.lower() for w in _COLOR_STR.split()]

def value(colors):
    c1, c2 = [c.lower() for c in colors[:2]]
    idx1, idx2 = [COLORS.index(color) for color in (c1, c2)]
    return 10 * idx1 + idx2
