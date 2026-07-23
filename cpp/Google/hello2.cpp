// C++ (use g++)
// file: hello2.cpp
//
/*
DESCRIPTION

Google C++ Tutorial
    https://developers.google.com/edu/c++/getting-started

2025Sep24, 2026Mar11
Author: Erik Johnson (no relation to Maggie Johnson)

This can be compiled w:
$ g++ hello2.cpp -o hello2


2026Mar11
Google appears to have updated their published code?

// hello2.cpp: Maggie Johnson
// Description: a program that prints the immortal saying "hello world"
// many times
#include <iostream>
// we need the following include for setw() in some c++ implementations
#include <iomanip>
using namespace std;

int main() {
  // the first for-loop will handle the rows
  for (int i = 0; i < 6; i++) {
    // the second for loop will handle the columns
    for (int j = 0;  j < 4 ; j++)
      // setw(int) sets the column width
      cout << setw(17) << "Hello World!";
    // this  next line is a part of the first for loop
    // and causes the new line
    cout << endl;
  }
  return 0;
}

*/


#include <iostream>
#include <iomanip>
// NB: setw() is in 'std' NS (both header's functions are)
// Google's hint to go look at this link for cout alignment info:
//     https://cplusplus.com/reference/iostream/cout/
// is pretty useless - I got example code from ChatGPT which told
// me to include <iomanip>.

using namespace std;


// Experiments implemented
int main() {
    string hello = "Hello World!";

    // default aligned (right)
    // cout << "default alignment..." << endl;
    // ej: Does this really do anything?
    // A: 2026Mar11 Yes, w/ a formatted field (not with default output
    // of just 'hello').
    cout << std::setiosflags(ios::left);

    // for 6 lines...
    for (int line_i = 0; line_i < 6; line_i++) {
        // print "Hello World!" 4 times on a line
        for (int col_i = 0; col_i < 4; col_i++) {
            // 2026Mar11 This certainly does, though: each HW formatted
            // to 17 chars wide
            cout << setw(17) << hello;
        }
        cout << endl;
    }
    cout << endl;

    return 0; // int (as required)
}

// EOF
