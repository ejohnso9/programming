This directory is for C++ code exploratino and Exercizes.

There may be more than one subdirectory here, such as

'Lipp5': "C++ Primer", 5th Edition, by Stanley Lippman,
'Stroustrup_PPP': "Programming Pinciples and Practice Using C++",
    2009, Bjarne Stroustrup

'gcc' generally assumes C code. As we want to compile C++ code, we want
to invoke the compiler as: g++.

For example:

    $ g++ -o hello hello.cpp


// ask ChatGPT about std::bein(), std::end()
// [ ] play with these
for (auto x : v) {
    ...
}

This is basically equivalent to:

for (auto it = std::begin(v); it != std::end(v); ++it) {
    auto x = *it;
    ...
}
