// file: ref.cpp


#include <iostream>


// using namespace std;
using std::cout;
using std::endl;


int main() {

    int x = 42;
    int *ip;
    int &r = x;

    ip = &x;
    r = 20;

    cout << "x is: " << *ip << endl;
    cout << "r is: " << r << endl;
    cout << endl;
}

// EOF
