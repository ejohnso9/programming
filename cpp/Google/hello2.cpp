// Orig code from Google Tutorial
//     https://developers.google.com/edu/c++/getting-started
//
// 2025Sep24
// Author: Erik Johnson (no relation to Maggie Johnson)


// hello.cpp: Maggie Johnson
// Description: a program that prints the immortal saying "hello world"
//
// #include <iostream>
// using namespace std;
// 
// int main() {
//   cout << "Hello World!" << endl;
//   return 0;
// }


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
    cout << "default alignment..." << endl;
    for (int line_i = 0; line_i < 6; line_i++) {
        for (int col_i = 0; col_i < 4; col_i++) {
            cout << setw(17) << hello;
        }
        cout << endl;
    }
    cout << endl;

    // left aligned
    // For the record, the given solution uses this at the top of main()
    //     set up cout to right-align
    //     cout <<  std::setiosflags(ios::left);
    // A) The comment is confused.
    // B) Appears to be global until set otherwise, whereas code below
    //    would presumably only apply left alignment to the one output.
    //    That seems a lot better?
    cout << "using left alignment..." << endl;
    for (int line_i = 0; line_i < 6; line_i++) {
        for (int col_i = 0; col_i < 4; col_i++) {
            cout << setw(17) << left << hello;
        }
        cout << endl;
    }
    cout << endl;

    return 0;
}

// EOF
