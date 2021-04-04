/*
DESCRIPTION
    starting template for a 
    Kattis.com problem ''.

AUTHOR
    Erik Johnson

REFERENCE
    https://open.kattis.com/problems/nastyhacks

NOTES
    Simple compilation:
    $ g++ nasty.cpp -o nasty

    Lessons learned:
        char * is old-school. 'string' is now a basic type - use that.

MAKEFILE

all: nasty.o
	g++ nasty.o -o nasty

nasty.o: nasty.cpp
	g++ -c nasty.cpp

clean: 
	rm nasty *.o

test:
	./nasty < 1.in

HISTORY
    2021Apr04 Created.
*/

#include <iostream>

using namespace std;

int main(void) {
    int n;        // number of test case lines
    long r, e, c; // rev w/ ads, rev w/o ads, ads cost
    long i = 0;   // loop counter

    const string ad     = "advertise";
    const string no_ad  = "do not advertise";
    const string either = "does not matter";
    string op;

    cin >> n;

    for (i = 0; i < n; i++) {
        cin >> r >> e >> c;

        if (e - c > r)
            op = ad;
        else if (e - c < r)
            op = no_ad;
        else
            op = either;

        cout << op << endl;
    }

    return 0;
}
