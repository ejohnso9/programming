// C++
// file: example3.cpp
//345678901234567890123456789012345678901234567890123456789012345678901234567890

/*
BUILD
    $ g++ example3.cpp -o example3

    # Just to make sure 'makefile' is generally still viable I, updated
    # it for this program (not generally doing so for all of them).
    $ make example3


DESCRIPTION
    Example 3: What does this program output?

    Prior to actually running it, I can tell that it creates a multiplication
    table where the first line headers are just int 1-9, tab-aligned.
    Then there are 9 rows, starting with: "{i}| " (Py formmating)
    following by the product of col and row number. Looks like single-digits
    ints will not be column-aligned as you would probably expect for numeric
    data?

    Indeed, after running it, that is confirmed. (Nor is the column header
    for col 1 aligned with column 1 data, b/c of the row header.)

18:26 ~/src/git/programming/cpp/Google$ ./example3
 1      2       3       4       5       6       7       8       9

1| 1    2       3       4       5       6       7       8       9
2| 2    4       6       8       10      12      14      16      18
3| 3    6       9       12      15      18      21      24      27
4| 4    8       12      16      20      24      28      32      36
5| 5    10      15      20      25      30      35      40      45
6| 6    12      18      24      30      36      42      48      54
7| 7    14      21      28      35      42      49      56      63
8| 8    16      24      32      40      48      56      64      72
9| 9    18      27      36      45      54      63      72      81

2026Mar11
LOL I figured there would be an exercize to go on to use formatted output to
get the table cleaned up but I guess that is left as a silent exercize to the
reader.
Maybe I will come back to this.
 */

#include <iostream>
using namespace std;

int main() {
  cout << " 1\t2\t3\t4\t5\t6\t7\t8\t9" << endl << "" << endl;
  for (int c = 1; c < 10; c++) {
    cout << c << "| ";
    for (int i = 1; i < 10; i++) {
      cout << i * c << '\t';
    }
    cout << endl;
  }
  return 0;
} 

// EOF
