
def super_tiny_rng(seed: int, n: int, n_bits: int) -> list[int]:
    x: int = seed
    rand_ints = []  # RV: qty: n, random {n_bits}-bit ints
    for run_i in range(n):
        bits = []
        for i in range(n_bits):
            x += (x * x) | 5  # the basic RNG operation (provides 1 bit)
            bits.append(int(bool(x & 0x80000000)))  # extract high-order bit from x
            x = x & 0xFFFFFFFF  # reduce x to 32-bit version of x
        bits.reverse()  # LSB first: 2^0 as el[0]
        rand_int = sum([bits[i] * 2**i for i in range(n_bits)])
        rand_ints.append(rand_int)

    return rand_ints  # RV: qty: n, random {n_bits}-bit ints


if __name__ == '__main__':
    """the published test cases for Problem set 2.65 St. Bitus' Dance"""

    loi = super_tiny_rng(831769172, 3, 8)
    assert loi == [39, 170, 1]

    loi = super_tiny_rng(2376066489, 3, 12)
    assert loi == [2138, 3320, 2731]

    loi = super_tiny_rng(2528054762, 5, 31)
    assert loi == [1425110951, 1066116851, 1565670465, 1613085173, 1921709156]

    loi = super_tiny_rng(1419340007, 7, 64)
    assert loi == [2372072775304310267, 14757952967543449990,
                   2275344065262535408, 668817182494655816,
                   14695084848187285985, 6287545658816032331,
                   13919832216633589446]

    print(loi)

