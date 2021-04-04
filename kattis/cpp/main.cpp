/*
DESCRIPTION
    starting template for a 
    Kattis.com problem ''.

AUTHOR
    Erik Johnson

REFERENCE
    https://open.kattis.com/problems/different

NOTES

    Simple compilation:

    $ g++ different.c -o diff_exe

HISTORY
    2021MonDD Created.
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
