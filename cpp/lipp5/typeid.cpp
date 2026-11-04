#include <iostream>
#include <typeinfo>

// you can print out dynamic (runtime) information about var types
// but the encoding is compiler specific (and perhaps a bit cryptic)

using std::cout;
using std::endl;


int main()
{
    int i, *ip;
    float x = 1.05;
    double pi = 3.1415926;
    int j{6}, k{7};

    cout << "'i' is type: " << typeid(i).name() << endl;   // i
    cout << "'ip' is type: " << typeid(ip).name() << endl; // Pi
    cout << "'x' is type: " << typeid(x).name() << endl;   // f
    cout << "'pi' is type: " << typeid(pi).name() << endl; // d

    auto f = [&](int i1, int i2) -> int {
        return i1 * i2;
    };

    // this is not so pretty: f(j, k) is type: Z4mainEUliiE_
    // (use auto)
    cout << "f(j, k) is type: " << typeid(f).name() << endl;
}

