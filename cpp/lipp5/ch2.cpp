// file: ch2.cpp
// vim: et ts=4 sw=4 tw=100

/*
 * Exercizes for Chapter 2 in "C++ Primer", Stanley Lippman, 5th Edition
 *
 * This was compiled with:
   $ g++ ch2.cpp -o ch2_EXE
 */

#include <iostream>

using namespace std;

// BC: is my own answer (b)efore (c)ompilation (just looking at book text)
// BCV: my answer is VALID (before avually checking)
// BCI: my answer is INVALID (before avually checking)
// [ ] - checkbox w/o status (yet)
// [v] - a checked checkbox (validated) (i.e., compilation confirms answer)
// [x] - checkbox, (invalidated) (i.e., comp. confirms wrong answer)

int main() {

    // Exercizes Section 2.3.1 (pg51)
    cout << "Chapter 2 Exercizes\n";
    cout << "-------------------\n";
    cout << "n";
    // cout << "NOT YET IMPLEMENTED.\n";


    //
    // Exercise 2.15:
    //
    cout << "Exercise 2.15\n";
    cout << "Which of the following definitions, if any, are valid? Why? (see source)\n";
    // if they are left uncommented, then they are compiling and valid
    
    // a)
    int ival = 1.01;  // VALID! NB: initializer is not an int value!  Silent narrowing!
    cout << "a) ival is: "  << ival << "\n"; 
    // OK, so I learned something here... I expected this would be a compiler error.
    // IT IS NOT!!! Silent, IMPLICIT conversion from double to int (round towards zero)
    //
    // ChatGPT tells me: "list initialization was introduced specifically to prevent accidental narrowing."
    // this *IS* an error:
    //     int i2{1.01};  // INVALID! NB: initializer is not an int value!
    //
    // ch2.cpp: In function ‘int main()’:
    // ch2.cpp:36:16: error: narrowing conversion of ‘1.01e+0’ from ‘double’ to ‘int’ [-Wnarrowing]
    //    36 |     int i2{1.01};  // VALID! NB: initializer is not an int value!  Silent narrowing!
    //       |                ^
 
    // b) NOT VALID
    // int &rval = 1.01; // 1.01 is double, rval type does not match! (neither the "base type" nor the "declarator" matches)
    // ch2.cpp: In function ‘int main()’:
    // ch2.cpp:46:17: error: cannot bind non-const lvalue reference of type ‘int&’ to an rvalue of type ‘int’
    //    46 |     int &rval = 1.01;
    //       |                 ^~~~

    // c)
    int &rval2 = ival; // BC: valid

    // d)
    // int &rval3; // BC: invalid: a ref type is an alias, not an obj: must always be initialized
    

    /*
    //
    // Exercise 2.16:
    //
    int i = 0, &r1 = i; double d = 0, &r2 = d;

    // Which, if any, of the follwoing assignments are invalid?
    // If they are valid, explain what they do.

    // a)
    r2 = 3.14159; // BCV: sets d to pi (approx.)

    // b)
    r2 = r1; // BCV: same as: d = 0;

    // c)
    i = r2; // BCV: same as: i = 3;

    // d)
    r1 = d; // BCV: same as: i = 3;
    // a) through d) all compile
    */
    
    //
    // Exercise 2.17:
    //

    //What does the following code print?
    int i, &ri = i; // The book intends this to be stand-alone, but i already declared in 2.16
    i = 5; ri = 10;
    cout << i << " " << ri << endl;
    // [v] BCV: "10 10\n"
    
}

// EOF

