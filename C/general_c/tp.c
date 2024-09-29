#include <stdio.h>

// tp => test program
// reads a single line of text from the file 'line.txt',
// prints it on stdout

int main () {
    FILE *fp;
    char str[120];

    /* opening text file for reading */
    fp = fopen("line.txt" , "r");
    if (fp == NULL) {
       perror("Error opening file");
       return(-1);
    }

    /* write contents of file.txt to stdout */
    if (fgets(str, 120, fp) != NULL ) {
        puts(str);
    }

    fclose(fp);
    return(0);
}


