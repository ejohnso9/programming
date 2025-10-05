#include <stdio.h>
// file: ej.cpp
/*
2025Sep28
---------
sample code to answer some of my own questions
This file is being built via 'makefile'.
*/

int main () {
    //char str[120];
    //int i, j, k;
    double d = 1.234;
    double *pd = nullptr; // C++ only
    int v[] {1, 2, 3};  // '=' optional in C++ (req. in C)
    int *ip = &v;

    printf("10 x v...\n");
    for (int i=0; i < 3; i++)
        printf("10 * v[%d] is: %d\n", i, 10 * v[i]);

    pd = &d;
    printf("d is: %f\n", *pd);
    printf("2nd element of v is: %d\n", *(ip + 1));

    return(0);
}

// EOF
