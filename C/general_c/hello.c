
#include <stdio.h>
#include <stdlib.h>

/*
In this simplest of programs, an executable can be compiled simply as:

    $ gcc hello.c -o hello

And then invoked as:

    $ ./hello
    Hello, World!
    $

*/

int main(int argc, char *argv[]) {

    printf("Hello, World!\n");

    // "Modern C", Jens Gustedt, pg 103 gives these constants as
    // something that should be universal on all C systems. That may be
    // sort of true, but they are not "built-in" - we can use them if
    // <stdlib.h> is #include'd
    // (found by simply grep'ing under /usr/include)
    return EXIT_SUCCESS; // #define EXIT_SUCCESS 0
    //return EXIT_FAILURE; // #define EXIT_FAILURE 1
}

/*
//Here is an alternative, allowable form of main():
main() {
    printf("Hello, World!\n");
}
//NB: this form declares no return type, and has no return statement.
*/

/* There is a bit of a curiosity here, in that main() actually has more
 * than one known prototype, and some exceptions are allowed in the case
 * of main() that normally don't apply to functions...
 *
 * Normally, it would be an error to get to the end of a function block
 * without using a return statement.
 *
 * You can check the last return code of the last invoked command via
 * bash as:
    $ echo $?

 * A second special case for main() is that a default of 0 is being
 * provided where you get to the end of the block without explicitly
 * providing a return value. (That does not happen, in general.)
 */

/* Here's two other main() declarations that work on my Mac:

int main(void) {
    printf("Hello, World!\n");
}

int main() {
    printf("Hello, World!\n");
}
*/

/*
// this form is NOT allowable:
void* main(void) {
    printf("Hello, World!\n");
}
*/

// EOF

