/*
DESCRIPTION
    Kattis.com problem 'different'.
    Print absolute different between two ints given on a line.

AUTHOR
    Erik Johnson

REFERENCE
    https://open.kattis.com/problems/different

NOTES
    NB:
        1) There is no N here, number of test cases on first line - prog
            just runs while loop.

        2) numbers in range 0 < x < 10^15. That is *far* outside range of
            'int' *OR* 'long'!!!

    Simple compilation:

    $ g++ different.c -o diff_exe

HISTORY
    2021Apr03 Created.
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    long long a, b;

    while (cin >> a >> b) {
        cout << abs(a-b) << endl;
    }

    return 0;
}
