// C++
// file: get_input2.cpp

/*
orig code by: Maggie Johnson (Google)
    https://developers.google.com/edu/c++/getting-started

DESCRIPTION:
    modified version to reset error stream and continue upon entry of non-numeric input

BUILD
    $ g++ get_input2.cpp -o get_input2

HISTORY
    2026Mar11 ej  modified as directed by tutorial
*/

#include <iostream>
#include <limits>
using namespace std;

int main() {
  int input_var = 0;
  // Enter the do while loop and stay there until either
  // a non-numeric is entered, or -1 is entered. Note that
  // cin will accept any integer, 4, 40, 400, etc.
  do {
    cout << "Enter a number (-1 = quit): ";
    // The following line accepts input from the keyboard into
    // variable input_var.
    // cin returns false if an input operation fails, that is, if
    // something other than an int (the type of input_var) is entered.
    if (!(cin >> input_var)) {
      cout << "Resetting to ignore non-numeric entry..." << endl;
      cin.clear();
      cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    if (input_var != -1) {
      cout << "You entered " << input_var << endl;
    }

    /*
    For reference, Google publishes this solution:
        https://developers.google.com/edu/c++/solutions/1-3
    // The following line accepts input from the keyboard into
    // variable input_var.
    // cin returns false if an input operation fails, that is, if
    // something other than an int (the type of input_var) is entered.
    if (!(cin >> input_var)) {
      cout << "Please enter numbers only." << endl;
      cin.clear();
      cin.ignore(10000,'\n');
    } else if (input_var != -1) {
      cout << "You entered " << input_var << endl;
    }
    */
  } while (input_var != -1);
  cout << "All done." << endl;
  return 0;
}
// EOF
