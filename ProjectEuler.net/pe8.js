// JS
// ProjectEuler.net Problem #8
// Find largest product of digits in 13-digit window
function pe8(dump) {

    var sList = [
            '73167176531330624919225119674426574742355349194934',
            '96983520312774506326239578318016984801869478851843',
            '85861560789112949495459501737958331952853208805511',
            '12540698747158523863050715693290963295227443043557',
            '66896648950445244523161731856403098711121722383113',
            '62229893423380308135336276614282806444486645238749',
            '30358907296290491560440772390713810515859307960866',
            '70172427121883998797908792274921901699720888093776',
            '65727333001053367881220235421809751254540594752243',
            '52584907711670556013604839586446706324415722155397',
            '53697817977846174064955149290862569321978468622482',
            '83972241375657056057490261407972968652414535100474',
            '82166370484403199890008895243450658541227588666881',
            '16427171479924442928230863465674813919123162824586',
            '17866458359124566529476545682848912883142607690042',
            '24219022671055626321111109370544217506941658960408',
            '07198403850962455444362981230987879927244284909188',
            '84580156166097919133875499200524063689912560717606',
            '05886116467109405077541002256983155200055935729725',
            '71636269561882670428252483600823257530420752963450'
        ],
        digits = sList.join('').split('').map(Number), // array of Number
        N = digits.length, // 1000
        w = 13, // window width
        hasZero,
        maxProduct = 0,
        product = 1,
        i, j; // array indices

    // start the window at 0 and slide forward to N - 13
    for (i = 0; i < (N - w + 1); i++) {

        // let's optimize this at least a little...
        // avoid multiplication if there is a 0 in the list
        // (I could jump the window forward when a 0 first
        //  appears, but this is still helpful.)
        hasZero = false;
        innerLoop:
        for (j = i; j < (i + w); j++) {
            if (digits[j] === 0) {
                hasZero = true;
                break innerLoop;
            }
        }

        if (!hasZero) {
            product = 1;
            for (j = i; j < (i + w); j++) {
                product *= digits[j];
            }

            if (product > maxProduct) {
                maxProduct = product;
            }
        }

    } // for i

    if (dump) {
        console.log("maxProduct = " + maxProduct);
    }

    return maxProduct;
}

pe8(true);

