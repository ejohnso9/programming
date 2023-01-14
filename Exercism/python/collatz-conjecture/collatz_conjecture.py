def steps(n):
    # validation
    if not (type(n) == int and n >= 1):
        raise ValueError("Only positive integers are allowed")

    # run the Collatz operation until we get to 1
    count = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1

    return count


def main():
    steps(16)


if __name__ == '__main__':
    main()

# EOF
