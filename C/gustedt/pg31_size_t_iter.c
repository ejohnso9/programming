/* -*- mode: C -*- */
// file: pg31_size_t_iter.c
// from "Modern C", Jens Gustedt, pg 31

# include <stdlib.h>
# include <stdio.h>

/* The main thing that this program does. */
int main(void) {

    for (size_t i = 9; i <= 9; --i) {
        // NB: %d does not work here, '%zu' will work w/ size_t
        printf("i is: %zu\n", i);
    }

    printf("Here we are, after the loop\n");

    return EXIT_SUCCESS;
}

// EOF

