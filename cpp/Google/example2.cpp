// C++
// vim: set shiftwidth=2
// 2025Sep24, ejohnson
//
// Google Tutorial, Example #2
// Orig code from:
//     https://developers.google.com/edu/c++/getting-started
//     (I'm editing comments)


// get_input.cpp: Maggie Johnson
// Description: Illustrate the use of cin to get input.

#include <iostream>
using namespace std;

int main() {
  // NB: cin is making the type conversion here to the var type.
  int input_var = 0;

  // while user enters accepted input...
  do {
    cout << "Enter a number (-1 = quit): ";
    // NB: cin returns false if an input operation fails
    if (!(cin >> input_var)) {
      cout << "BAD INT, exiting." << endl;
      break;
    }
    if (input_var != -1) {
      cout << "You entered " << input_var << endl;
    }
  } while (input_var != -1);

  cout << "done." << endl;

  return 0;
}

// EOF
