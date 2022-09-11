
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// #include <wchar.h>

/*
DESCRIPTION
    Simple program to read lines from a text input file and print out
    max length seen as we go.

AUTHOR
    Erik Johnson

DATE
    2022-May-01

    $ gcc read_line_lengths.c -o lengths
*/


#define MAXLINE 256


// GLOBAL vars


// ENTRY POINT
int main(int argc, char *argv[]) {

    int len = 0;
    int line_count = 0;
    int maxlen = 0;
    char *rc;
    FILE *fd = fopen(argv[1], "r");
    char line[MAXLINE];

    /*
    rc = fgets(line, MAXLINE, fd);
    printf("  rc is: %p\n", rc);
    printf("line is: %p\n", line);
    printf("'%s'\n", line);
    */

    while(fgets(line, MAXLINE, fd)) {
        line_count += 1;
        if ((len = strlen(line)) > maxlen) {
            maxlen = len;
            printf("%d: new max = %d\n", line_count, maxlen);
            printf("%s\n", line);
            printf("\n");
        }
    }

    printf("\n");
    return EXIT_SUCCESS; // 0
}


// EOF

