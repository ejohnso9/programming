// file: ch2.cpp
// vim: et ts=4 sw=4 tw=100 autoindent smartindent :

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
    cout << "Chapter 2 Exercizes" << endl;
    cout << "-------------------" << endl;
    cout << endl;
    // cout << "NOT YET IMPLEMENTED.\n";


    /* SEE NOTE BELOW ABOUT GROWING DECLARATIONS

    //
    // Exercise 2.15:
    //
    cout << "Exercise 2.15\n";
    cout << "Which of the following definitions, if any, are valid? Why? (see source)\n";
    // if they are left uncommented, then they are compiling and valid
    
    // a)
    // Surprisingly, this is somewhat environment dependent.
    // On PythonAnywhere, the following statement will pass silently w/
    // a data narrowing!
    // On my local Mac (clang), this will emit a compiler warning:
    int ival = 1.01;

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
    
    //
    // Exercise 2.17:
    //

    //What does the following code print?
    int i, &ri = i; // The book intends this to be stand-alone, but i already declared in 2.16
    i = 5; ri = 10;
    cout << i << " " << ri << endl;
    // [v] BCV: "10 10\n"
    
    //
    // Exercizes Section 2.3.2
    //

    // Ex. 2.18 Write code to change the value of a pointer.
    //      Write code to change the value to which a pointer points.
    cout << "Ex. 2.18:\n";
    int ary[3]{11, 12, 13};
    int *ip = &ary[0];
    cout << "BEFORE:\n";
    for (int i = 0; i < 3; ++i) {
        cout << " ary[" << i << "] = " << ary[i] << endl;
    }
    
    cout << "AFTER:\n";
    for (int i = 0; i < 3; ++i) {
        // NB: this loop satisfies both requirements of the problem
        *ip = *ip * 10;
        ip++;
        cout << " ary[" << i << "] = " << ary[i] << endl;
    }

    // Ex. 2.19
    // Explain the key differences between references and pointers.
    // References are name aliases, not "objects" (mean there is not
    // user-addressable memory associated with a reference - you cannot
    // take the address of it, you can't change its value - it is a C++
    // runtime "internal". Therefore, they must always be initialized in
    // the declaration and their value is static of the program
    // lifetime. In contrast, a pointer *IS* an object, you *CAN* take
    // the address of a pointer, you can change its value, etc.

    // Ex. 2.20 What does this program do?
    // BEFORE compilation: it sets i to square of 42 (1764)
    int i = 42;
    int *p1 = &i;
    *p1 = *p1 * *p1;
    cout << "Ex. 2.20: i is: " << i << endl;


    // Ex. 2.21 Explain each of the following definitions. Indicate
    // whether any are illegal and, if so, why.
    int i = 0;
    // (a)
    // double* dp = &i; // ILLEGAL: base types do not match
                        // ch2.cpp:152:13: error: cannot initialize a variable of type 'double *' with an rvalue of type 'int *'

    // (b)
    // int *ip = i; // ILLEGAL: (see page 54)
                    // ch2.cpp:155:10: error: cannot initialize a variable of type 'int *' with an lvalue of type 'int'

    // (c)
    int *p = &i; // LEGAL


    // Ex. 2.22
    // Assuming p is a pointer to int, explain the following code:
    // if (p) ... // same as: if (p != nullptr) or if (p != 0)
    // if (*p) ... // this is testing the value ref'ed by p as non-zero.

    // Ex. 2.23
    // Given a pointer to p, can you determine whether p points to a
    // valid object?
    // No... given the list at the bottom of pg. 52, I see how (in general).
    //
    // TODO: after structs, come back and show that you can increment a
    // pointer to one past end of valid array, then try to access data
    // (which I expect you can, w/o compiler error), yet the pointer is
    // not valid (make some other struct type to sit behind array - show
    // that you can get at data in it (even though pointer is for
    // different type)


    */ // CODE ABOVE was compiling and running fine on 2026Aug02
    // taking code out so I don't have a growing number of declarations
    // already in play for later problems.


    // Ex. 2.24
    // Why is the initialization of p legal but that of lp illegal?
    int i = 42; void *p = &i; // long *lp = &i;
    // As stated on pg 56, void pointers are allowed to reference any
    // type. Such priviledges are not extended to other pointer types.
    // ch2.cpp:183:37: error: cannot initialize a variable of type 'long *' with an rvalue of type 'int *'

} // main()

// EOF

