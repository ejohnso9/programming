// ProjectEuler.net Problem #4
(function fib(N, dumpToConsole) {
    var n0 = 1,
        n_1 = 1,
        temp,
        total = 0;

    while (n0 <= N) {
        if (dumpToConsole) {
            console.log(n0);
        }

        if (n0 % 2 == 0) {
            total += n0;
        }

        // next number
        temp = n0 + n_1;
        n_1 = n0;
        n0 = temp;
    }

    return total;
})(4e6);

