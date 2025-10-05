#include <stdio.h>

/*
// 2025Sep28
// sample code to answer some of my own questions
// I am using the makefile for CPP code.
// This C file is just compiled on CLI as:
//   .$ gcc ej1.c -o ej1
// 
// Q1: how can I verify that a statement like:
//  int* ip, i;
//  is actually an int pointer and an int, not 2 pointers?
//  A: C doesn't actually support run time time info (RTTI).
//      There is the typeof() operator, a custom feature built into Gnu
//      compilers, but this is not standard, ANSI C.
//      You mayb be able to use sizeof() operator to infer the
//      difference in size between a pointer and a primitive value, but
//      that's a bit of a hack.
//
//      A more legible (human-parseable) declaration would be:
//          int *ip1, *ip2;
//      or:
//          int *ip, my_int;  # just one pointer
//
//      And that is why I don't like formatting like:
/          int* ip;
*/

int main () {
    //char str[120];
    //int i, j, k;
    //double *pd = nullptr; . // NO!  C++ only
    int v[] = {1, 2, 3};  // apparently, '=' is required here (optional in C++)
    printf("10 x v...\n");
    for (int i=0; i < 3; i++)
        printf("10 * v[%d] is: %d\n", i, 10 * v[i]);

    double a = 3.14;
    // NB: typeof() is a 'gcc' only (*NOT g++) extension!
    typeof(a + 1) b = a + 1;  // declare b to be same type as a

    // verify we can dump both vars
    printf("a is: %f\n", a);
    printf("b is: %f\n", b);

    return(0);
}

// EOF
