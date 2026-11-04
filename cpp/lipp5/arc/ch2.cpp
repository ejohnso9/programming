// file: ch2.cpp
// vim: et ts=4 sw=4 tw=100 autoindent smartindent :

/*
 * Exercizes for Chapter 2 in "C++ Primer", Stanley Lippman, 5th Edition
 *
 * This was compiled with:
   $ g++ ch2.cpp -o ch2_EXE
 */

#include <iostream>
#include <typeinfo>

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

    // Ex. 2.24
    // Why is the initialization of p legal but that of lp illegal?
    int i = 42; void *p = &i; // long *lp = &i;
    // As stated on pg 56, void pointers are allowed to reference any
    // type. Such priviledges are not extended to other pointer types.
    // ch2.cpp:183:37: error: cannot initialize a variable of type 'long *' with an rvalue of type 'int *'

    // My own notes: Verify that this is illegal(?)
    int i = 42; int &i_ref = i; int *ip = &i;
    cout << "&i is: " << &i << endl;
    ip = &i_ref; // <-- NO!!!! This compiles, runs w/o ERROR!
    // I take this to mean we're just taking address of i
    cout << "&i_ref is: " << ip << endl; // i.e., &i_ref == &i

    // "References to Pointers", pg 58
    // gives the example:
    int i = 42;
    int *p;
    int *&r = p; // r is reference to the pointer p
    r = &i;
    cout << "before *r = 0 ... i is: " << *p;
    *r = 0;
    cout << "after, i is: " << *p;

    // I had my own question: could: int *&r = p;
    // int &*r2 = p; // <-- just as well be this?
    // The answer to that is: NO! Read it RtoL and the declaration of
    // pointer to reference is illegal.

    // Ex. 2.25, pg 59
    cout << "Ex. 2.25, pg 59" << endl;
    // Determine the types and values of each of the following vars.
    // (a)
    int *ip, i, &r = i;
    // BEFORE compilation
    // ip is type: int*, value uninitialized
    //  i is type: int, value uninitialized
    //  r is type: int&; // value same as i (uninit)
    cout << "ip is: " << ip << ", type: " << typeid(ip).name() << endl;
    cout << "i is: " << i << ", type: " << typeid(i).name() << endl;
    cout << "r is: " << r << ", type: " << typeid(r).name() << endl;
    // above prints:
    // ip is: 0x101085bd0, type: Pi
    // i is: 1, type: i
    // r is: 1, type: i
    // which is a bit ambiguous... in the code, the r reference is used as
    // an alias for i, but obviously r has a modifier in the
    // declaration, so what is the type of r? I think: int& but I guess
    // you can't really see that in an introspective way?

    // (b)
    int i, *ip = 0;
    // i in simply an int
    // ip is: int*
    cout << " i is: " << i << ", type: " << typeid(i).name() << endl;
    cout << "ip is: " << ip << ", type: " << typeid(ip).name() << endl;

    // (c)
    int* ip, ip2; // ip is: int* while ip is just an int!
    cout << "ip is: " << ip << ", type: " << typeid(ip).name() << endl;
    cout << "ip2 is: " << ip2 << ", type: " << typeid(ip2).name() << endl;

    //
    // Exercizes Section 2.4 (pg 60)
    cout << "Exercize 2.26 (bottom pg 60)" << endl;
    //

    // Ex. 2.26
    // Which of the following are legal? For those that are illegal,
    // explain why.
    // const int buf; // (a) ILLEGAL: ch2.cpp:249:15: error: uninitialized const ‘buf’ [-fpermissive]
    int cnt = 0; // (b) this is, of course, LEGAL
    cout << "(b) int cnt = 0; // <- LEGAL" << endl;
    const int sz = cnt; // (c) LEGAL
    cout << "(c) const int sz = cnt; // <- LEGAL" << endl << endl;
    // ++cnt; ++sz; // (d) ILLEGAL: you can not modify const sz


    // Initialization and References to const (middle pg 61)
    cout << "Initialization and References to const (bottom pg 61)" << endl;
    int i = 42;
    const int &r1 = i; // OK: const ref bound to non-const value
    const int &r2 = 42; // "reference to const" AKA "const ref"
    const int &r3 = r1 * 2; // ref to temp (see pg 62)
    // int &r4 = r1 * 2; // error: cannot bind non-const lvalue reference of type ‘int&’ to an rvalue of type ‘int’
                         // does *NOT* work with i either: problem seems to be that it is a temp value!

    // 2026Oct16  This *COMPILES*!
    double dval = 3.14;
    const int &ri = dval; // LEGAL! "To ensure that the object to which ri is bound is an int,
                          // the compiler transformes this code into something like:
                          // const int temp = dval;
                          // const int &ri = temp;
                          // I think it would be better to simply say that ref to int does not bind
                          // to double? Seems like a basic type error? But they didn't ask me.
    cout << "ri is: " << ri << endl;

    // error: cannot bind non-const lvalue reference of type ‘int&’ to an rvalue of type ‘int’
    double pi = 3.14;
    // int &pi_ref = pi; // <- ILLEGAL (b/c bound to const, I believe)

    int foo = 42;
    cout << "foo was: " << foo << endl;
    int &foo_ref = foo;
    foo = 99;
    cout << "now is: " << foo << endl << endl;
    */ // CODE ABOVE was compiling and running w/o error on 2026Oct21


    // There's basically two kinds of 'const' when it comes to pointers...
    // 1) declaring the pointer itself to be const - i.e., disallowing code to change
    //    where (to what thing) the pointer points to (that does not disallow changing
    //    what is pointed at!)
    // 2) declaring a pointer to point to a const thing (that is, we are going
    //    to treat it as if the reffered thing is const (meaning disallow changing
    //    the referrent through the pointer) whether it is actually const or not.
    double pi = 3.1415926;
    double phi = 1.6180;
    cout << "pi is:" << pi << endl;
    const double *pi_p = &pi; // pointer is const, pointed-to is not!
    cout << "pi (through the pointer) is: " << *pi_p << endl;
    cout << "make pi_p point to phi." << endl;
    pi_p = &phi;
    cout << "                  pi is now: " << *pi_p << endl << endl; // NOT pi! phi!

    // but you can't do this: it's a pointer to const!
    // *pi_p = 3.1419;  // BAD VALUE!
    //  cout << "pi is now:" << *pi_p << endl; // NOT pi! phi!

    // the second notion of const: constant reference
    double *const phi_p = &phi;
    double const *phi_p2 = &phi; // this syntax also legal, same as line above
    cout << "phi (through the pointer) is:" << *phi_p << endl;
    // but I can't make that pointer point elsewhere:
    // like this: phi_p = &pi;
    // ch2.cpp:311:11: error: assignment of read-only variable ‘phi_p’
    // 311 |     phi_p = &pi;
    //     |     ~~~~~~^~~~~

    /*
    Though a reference is not an object (it's a name alias) and it has been said:
    "you can't take the address of a reference", I discovered today that that's 
    semantically slippery. You can't get an address value for the reference itself
    (it's internal to the C runtime system, not user-accessible memeory).
    You can, however "take address of a reference" - meaning the address of
    the object the reference refers to!
    */
    double &pi_ref = pi;
    cout << "address of pi (directly): " << &pi << endl;
    cout << "                 &pi_ref: " << &pi_ref << endl;

    // The two types of const are independent, and you can have one or the other,
    // both or neither. Bottom of pg 63 talks about:
    // 1) "Top-Level const" which is the first sense (above): the pointer itself is const
    //    (the pointer can't be changed to point elsewhere).
    // 2) "low level const" is the second notion above: pointer (or reference)
    //    can't be used to change what is pointed to (or referred to).

    cout << "EOF" << endl;

} // main()

// EOF

