// JS
// ProjectEuler.net Problem #6
// difference between square of sums and sum of squares 1-100
function pe6(N, dump) {

    var sumOfSquares = 0,
        sum = 0,
        squareOfSums,
        i;

    for (i = 1; i <= N; i++) {
        sum += i;
        sumOfSquares += i * i;
    }

    squareOfSums = sum * sum;

    if (dump) {
        console.log("sum: " + sum);
        console.log("square of sums: " + squareOfSums);
        console.log("sum of squares: " + sumOfSquares);
        console.log("difference: " + (squareOfSums - sumOfSquares));
        console.log();
    }

    return squareOfSums - sumOfSquares;

}
pe6(10, true);
pe6(100, true);

