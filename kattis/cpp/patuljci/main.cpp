/*
DESCRIPTION
    starting template for a 
    Kattis.com problem 'patuljci'.

AUTHOR
    Erik Johnson

REFERENCE
    https://open.kattis.com/problems/patuljci

NOTES
    NB: simple Makefile included at bottom

    Strategy:
    ----------
    If I had an array of N things, and I needed to check subsets of N-1
    items at a time, I could simply iterate i: 0 to (N-1), and check
    everything in the array except element i.

    If you want to look at all the N-2 sets of N total elements, you
    simply do the thing above on each of the N-1 sets.

    Q: Do I need two different functions, or can I do this cleverly with
        one recursive function?
    A: Ummm, using 2 funcs seems easier - they take different
        number of args. With better leverage of all of the
        iterators and so on in STL, maybe could do this in a
        more flexible way. For now, it works.

    Knuth Fasicle 2 of Volume 4, "Generating All Tuples and
    Permutations" gives a more complete treatment of the subject, and
    that is perhaps worth returning to but for now, let's try to just
    make my naieve approach work.

HISTORY
    2021Apr04 Created.
*/

#include <iostream>
#include <algorithm>

#define N 9
#define SUM 100

using namespace std;

// compute 7-element array sum, skipping i, j
int sum2(int *nums, int i, int j) {
    // nums: int* - ptr to base of int array
    // i, j: indices to ignore
    int sum = 0;
    for (int k = 0; k < N; k++) {
        if (k == i || k == j)
            continue;
        else
            sum += nums[k];
    }

    return sum;
}

// dump out 'nums' w/o i, j elements
int dump(int *nums, int i, int j) {
    for (int k = 0; k < N; k++) {
        if (k != i && k != j)
            cout << nums[k] << endl;
    }

    return 0;
}

// check each subset of implied 8-element set
int sum1(int *nums, int i) {
    // nums: int* - ptr to base of int array
    // i: index to ignore
    int total;

    for (int j = 0; j < N; j++) {
        if (j == i)
            continue;
        else {
            total = sum2(nums, i, j);
            if (total == SUM) {
                dump(nums, i, j);
                return total;
            }
        }
    }

    return 0;
}

// entry, init, drive the 8-element checker func
int main(void) {
    int nums[N];
    int rv;

    // read 9 int values from stdin
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    // process each N-1 subset (leaving nums[i] out)
    for (int i = 0; i < N; i++) {
        // call the 8-el check func
        rv = sum1(nums, i);
        if (rv == SUM)
            break; // if SUM found, we're done
    }

    return 0;
}

/* MAKEFILE
main: main.o
	g++ main.o -o main

main.o: main.cpp
	g++ -c main.cpp

clean: 
	rm main *.o

test:
	./main < test1.txt
	./main < test2.txt
*/

/* INPUT1 (should output: [7, 8, 10, 13, 19, 20, 23])
7
8
10
13
15
19
20
23
25
*/

/* input2 (out: [8, 6, 5, 1, 30, 28, 22])
8
6
5
1
37
30
28
22
36
*/
