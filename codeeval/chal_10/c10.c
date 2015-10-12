#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// compiler command:
//  gcc c10.c -o c10 -lc

// s = "123\n";

int main(int argc, const char *argv[]) {
    char line[1024];
    char *c_ptr;
    int i, n, n_el, offset;

    FILE *file = fopen(argv[1], "r");
    while (fgets(line, 1024, file)) {
        offset = strlen(line) - 2;
        c_ptr = line + offset;

        // back up to 1 before first digit
        while (isdigit(*c_ptr)) {
            c_ptr--;
        }
        c_ptr++;

        n = atoi(c_ptr);
        n_el = (c_ptr - line) / 2;
        if (n_el >= n) {
            c_ptr -= 2 * n;
            printf("%c\n", *c_ptr);
        }
    }

    return 0;
}
