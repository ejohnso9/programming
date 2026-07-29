// C++
// file: hello.cpp

/*
 * DESCRIPTION
 *      First program presented on PG 45
 *
 * DATE
 *      2025Oct11
 * 
 * NOTES
 * To compile:
 *      $ g++ -o hello hello.cpp
 */

// This is the line on pg 45 of PPP: doesn't seem to work
//     include "std_lib_facilities.h"
//
// next two lines come from "Tour of C++" book, these *will* compile:

#include <iostream>

using namespace std;

int main()
{
    cout << "Hello, World!\n";
    return 0;
}
