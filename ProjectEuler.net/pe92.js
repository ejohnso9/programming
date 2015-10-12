// JS
// ProjectEuler.net Problem #92: Square Digit Chains
// Very curiously, when you add up the sums of the digits of a number
// and repeat this iteratively, all numbers end up in one of two cycles,
// either 1 or starting with 89.
// How many numbers below 10mil are on the 89 plan?
function pe92(N) {

    var 
        // helper to compute square of the digits in the number
        sumDigitsSq = function(n) {

            var digits = n.toString().split(''),
                sum = 0,
                d, i;

            for (i = 0; i < digits.length; i++) {
                d = digits[i];
                sum += d * d;
            }

            return sum;
        },

        // starting with N, run down to 1 or 89
        oneOr89 = function(n, returnList) {
            var numList = [];
            while (n !== 1 && n !== 89) {
                if (returnList) {
                    numList.push(n);
                }
                n = sumDigitsSq(n);
            }

            return returnList ? numList : n;
        },

        count89 = 0,
        i, n;


    for (i = 0; i < N; i++) {
        if (oneOr89(i) === 89) {
            count89 += 1;
        }
    }

    return count89;
}

pe92(1e7);

