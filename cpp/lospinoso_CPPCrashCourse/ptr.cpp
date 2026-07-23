// file: ref.cpp


#include <iostream>


// using namespace std;
using std::cout;
using std::endl;


int main() {

    // below demonstrates why I don't like lines like:
    // int* ip, ip2;

    // if you want 2 pointers, then do this:
    int *ip, *ip2;

    // both of these give you an int* and an int!
    // int* ip, ip2;
    // int *ip, ip2;


    ip2 = 42;
    ip = &ip2;

    cout << "      ip2 is: " << ip2 << endl;
    cout << "ip points to: " << *ip << endl;
    cout << "ip is itself: " << ip << endl;
    cout << " b/c &ip2 is: " << &ip2 << endl;
    cout << "      &ip is: " << &ip << endl;
    cout << endl;
}

// EOF
