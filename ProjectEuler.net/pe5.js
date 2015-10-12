// JS
// ProjectEuler.net Problem #5
// https://projecteuler.net/problem=5
// First integer that is a multiple of (1..20)

// The probelm states that 2520 is the first that is a multiple of
// 1..10, so we can start our search there.
(function pe5() {

    var n = 2520,
        maxDiv = 20, // biggest divisor to search up to
        found = false;

    while (!found) {
        for (i = 2; i <= maxDiv; i++) {
            if (n % i !== 0) {
                break;
            }
        }
        if (i === maxDiv) {
            found = true;
            console.log("found: " + n);
        }
        else {
            n += 1;
            if (n % 100 === 0) {
                console.log(n);
            }
        }
    }

    console.log("end while loop.");

    return n;

})();

// pe5();

