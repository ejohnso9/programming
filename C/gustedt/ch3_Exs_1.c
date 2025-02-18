/* -*- mode: C -*- */
/*
 * From "Modern C", Jens Gustedt, pg 4
 * Compiled and run @PythonAnywhere:
 *  $ c99 L_1.1.c   // produces a.out, which works
 *  c99 appears to be same as gcc
 *  no: clang
 */

# include <stdlib.h>
# include <stdio.h>

/* The main thing that this program does. */
int main(void) {
    // Declarations
    double A[5] = {
        [0] = 9.0,
        [1] = 2.9,
        [4] = 3.E+25,
        [3] = .00007,
    };

    for (size_t i = 0; i < 5; ++i) {
        if (i) {
            printf("element %zu is %g, \tits square is %g\n",
                   i,
                   A[i],
                   A[i] * A[i]);
        }
    }

    return EXIT_SUCCESS;
}
// EOF

