#include <stdio.h>

// compiler command:
//  gcc c15.c -o endian -lc


int main(int argc, const char *argv[]) {
    unsigned int x = 1;
    if ((int)(char *)&x == 0x1) {
        printf("BigEndian\n");
    }
    else {
        printf("LittleEndian\n");
    }

    return 0; // normal exit
}
