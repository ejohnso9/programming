/* -*- mode: C -*- */
/*
 * From "Modern C", Jens Gustedt, pg 4
 * Compiled and run @PythonAnywhere:
 *  $ c99 L_1.1.c   // produces a.out, which works
 *  c99 appears to be same as gcc
 *
 *  fixed to look more like Listing 1.1 so it will run
 */

# include <stdlib.h>
# include <stdio.h>

/* The main thing that this program does. */
int main() {
    // Declarations
    int i;
    double A[5] = {
        9.0,
        2.9,
        3.E+25,
        .00007,
    };

    // Void some work
    for (i = 0; i < 5; ++i) {
        printf("element %d is %g, \tits square is %g\n",
               i,
               A[i],
               A[i] * A[i]);
    }

    return EXIT_SUCCESS;
}
// EOF

