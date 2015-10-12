// JS
// ProjectEuler.net Problem #14
// Find largest Collatz chain under 1e6 (1 mil)
function pe14() {

    var i,
        count,
        longN,
        maxCount = 1,
        collatz = function(n, returnSeq) {

            var count = 0, // # of steps to reach 1 including initial n
                seq = []; // all the terms

            while (n != 1) {
                if (returnSeq) {
                    seq.push(n);
                }

                if (n % 2 == 0) { // even
                    n = n / 2;
                } else {
                    n = 3 * n + 1;
                }

                count += 1;
            }

            // one more for the last 1
            if (returnSeq) {
                seq.push(1);
            }
            count += 1

            return returnSeq ? seq : count;
        };

    for (i = 1; i < 1e6; i++) {
        count = collatz(i);
        if (count > maxCount) {
            maxCount = count;
            longN = i;
        }
    }

    return longN;

    // console.log(collatz(13, true)); // 10
    // return collatz(27); // 112
}

