/* -*- mode: C -*- */
// file: pg16_ej.c

# include <stdlib.h>
# include <stdio.h>

/*
 * I came up with some questions of my own that I wanted to text while
 * reading the book. I can't spot exactly where right now, but one thing
 * I think I read is that you can assign an int other than 0 to a
 * pointer. But you *can* assign 0. Most systems will implement the
 * preprocessor directive NULL as 0, and then you can assign NULL, but
 * the NULL value is actually not prescribed, and programmers shouldn't
 * have to worry about that detail.
 *
 * So, if I declare an array of 2 ints (I'm assuming to be 4 bytes, but
 * will check), Can I take the address of the first int, add 2
 * (straddling to the ints of my array), then print this out as an int
 * value?
 * In fact, this runs w/o error:
 
    int nums[2] = {42, 50};
    int* ip;

    ip = &nums[0];
    ip += 2;
    printf("int at *ip is: %d\n", *ip);
 
outputs: int at *ip is: -945116928
 */

int main(void) {
    int nums[2] = {42, 50};
    int x;
    int* ip;
    int* ip1;
    int* ip2;

    printf(" first element at: %p\n", &nums[0]);
    printf("second element at: %p\n", &nums[1]);

    // ip = 0x7ffe869d45a4; // causes compiler (c99) warning
    // pg16_ej.c: In function ‘main’:
    // pg16_ej.c:39:8: warning: assignment to ‘int *’ from ‘long int’ makes pointer from integer without a cast [-Wint-conversion]
    // 39 |     ip = 0x7ffe869d45a4;
    
    /* This also causes a compiler warning:
    x = 0;
    ip = x;

pg16_ej.c: In function ‘main’:
pg16_ej.c:46:8: warning: assignment to ‘int *’ from ‘int’ makes pointer from integer without a cast [-Wint-conversion]
   46 |     ip = x;

    I think it is generally true that the compiler understands types and
    not values, though there may be some exceptions for literals.

    This is allowable, as Gustedt says: you can assign 0 but not other
    values. Technically, I am assigning int value to var type: int*
    */
    ip = NULL;  // NB: ip = null; is not a legal statement
    ip1 = &nums[0];
    ip2 = &nums[0];

    if (ip1 == ip2) 
        printf("ip1 == ip2.\n");
    else
        printf("ip1 != ip2.\n");

    return EXIT_SUCCESS;
}

// EOF

