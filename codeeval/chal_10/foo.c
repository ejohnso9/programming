#include <stdio.h>
#include <string.h>

int main(int argc, const char *argv[]) {
    char *s = "123\n";
    char *c_ptr;
    int i;
    int len = strlen(s) - 1;
    int offset = len - 1;

    c_ptr = s + offset;
    for (i = offset; i >= 0; i--) {
        printf("%c", *c_ptr);
        c_ptr--;
    }
    printf("\n");

    return 0;
}
