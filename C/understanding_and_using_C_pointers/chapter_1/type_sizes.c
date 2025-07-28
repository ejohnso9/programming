#include <stdio.h>
#include <stdlib.h>

// 2025Mar24 ej
//
// Familiarity exercize for sizes of primitive types and their pointers.

int main () {
    char c = 'c';
    short _s = 19;
    int i = 42;
    long l = 0xFFFFFFFE;  // min 4 bytes but may well be 8 bytes on 64-bit system
    long long ll = 0xFEDCBA9876543210;  // long long is min 8 bytes in size

    char* cp = &c;
    short* sp = &_s;
    int* ip = &i;
    long* lp = &l;
    long long* llp = &ll;

    // these format specifiers are not exactly intuitive
    printf(" c is: '%c'\n", c);
    printf("_s is: %d\n", _s);
    printf(" i is: %d\n", i);
    printf(" l is: %ld\n", l);   // or %li
    printf("ll is: %lld\n", ll); // or %lli
    printf("\n");

    // see: https://www.gnu.org/software/c-intro-and-ref/manual/html_node/Type-Size.html
    //      https://en.wikipedia.org/wiki/C_data_types
    //      https://cplusplus.com/reference/cstdio/printf/
    printf("  sizeof(c) is: %lu bytes\n", sizeof(c));
    printf(" sizeof(_s) is: %lu bytes\n", sizeof(_s));
    printf("  sizeof(i) is: %lu bytes\n", sizeof(i));
    printf("  sizeof(l) is: %lu bytes\n", sizeof(l));
    printf(" sizeof(ll) is: %lu bytes\n", sizeof(ll));
    printf("\n");


    printf("\n");

    return(EXIT_SUCCESS); // from <stdlib.h>
}

// EOF

